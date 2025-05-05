import asyncio
import os
import time
from datetime import date, datetime

import aiohttp
import pytz
from aiohttp import web
from motor.motor_asyncio import AsyncIOMotorClient
from pyrogram import Client, filters, enums, __version__, types

from database.ia_filterdb import Media
from database.users_chats_db import db
from info import (
    API_ID,
    API_HASH,
    ADMINS,
    BOT_TOKEN,
    LOG_CHANNEL,
    PORT,
    SUPPORT_GROUP,
    DATABASE_URI,
    URL as PING_URL,
)
from plugins import web_server, check_expired_premium
from typing import Union, Optional, AsyncGenerator
from utils import temp


# -----------------------------
# MongoDB setup for settings
# -----------------------------
_mongo_client = AsyncIOMotorClient(DATABASE_URI)
_settings_coll = _mongo_client["autodeleter"]["settings"]


class Bot(Client):
    def __init__(self):
        super().__init__(
            name="aks",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            sleep_threshold=5,
            workers=150,
            plugins={"root": "plugins"},
        )

    async def start(self):
        # load banned lists
        b_users, b_chats = await db.get_banned()
        temp.BANNED_USERS = b_users
        temp.BANNED_CHATS = b_chats

        # record start time for logs
        self._start_time = time.time()

        # start pyrogram client
        await super().start()
        await Media.ensure_indexes()

        # bot identity
        me = await self.get_me()
        temp.ME = me.id
        temp.U_NAME = me.username
        temp.B_NAME = me.first_name
        temp.B_LINK = me.mention
        self.username = "@" + me.username

        # background tasks
        self.loop.create_task(check_expired_premium(self))
        self.loop.create_task(self._ping_loop())

        # start aiohttp server
        app_runner = web.AppRunner(await web_server())
        await app_runner.setup()
        await web.TCPSite(app_runner, "0.0.0.0", PORT).start()

        # send restart logs
        tz = pytz.timezone("Asia/Kolkata")
        today = date.today()
        now = datetime.now(tz).strftime("%H:%M:%S %p")
        restart_message = (
            f"<b>{me.mention} ʀᴇsᴛᴀʀᴛᴇᴅ 🤖\n\n"
            f"📆 ᴅᴀᴛᴇ - <code>{today}</code>\n"
            f"🕙 ᴛɪᴍᴇ - <code>{now}</code>\n"
            f"🌍 ᴛɪᴍᴇ ᴢᴏɴᴇ - <code>Asia/Kolkata</code></b>"
        )
        await self.send_message(chat_id=LOG_CHANNEL, text=restart_message)
        await self.send_message(chat_id=SUPPORT_GROUP, text=f"<b>{me.mention} ʀᴇsᴛᴀʀᴛᴇᴅ 🤖</b>")

        elapsed = int(time.time() - self._start_time)
        for admin in ADMINS:
            await self.send_message(
                chat_id=admin,
                text=f"<b>✅ ʙᴏᴛ ʀᴇsᴛᴀʀᴛᴇᴅ\n🕥 ᴛɪᴍᴇ ᴛᴀᴋᴇɴ - <code>{elapsed} sᴇᴄᴏɴᴅs</code></b>",
            )

    async def stop(self, *args):
        await super().stop()
        print("Bot stopped.")

    async def _ping_loop(self):
        """ Periodically ping the given URL to keep the bot alive. """
        async with aiohttp.ClientSession() as session:
            while True:
                try:
                    await session.get(PING_URL)
                except Exception:
                    pass
                await asyncio.sleep(30)

    async def is_admin(self, chat_id: Union[int, str], user_id: int) -> bool:
        """ Check if a user is an admin in the given chat. """
        async for member in self.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
            if member.user.id == user_id:
                return True
        return False

    async def iter_messages(
        self, chat_id: Union[int, str], limit: int, offset: int = 0
    ) -> Optional[AsyncGenerator["types.Message", None]]:
        current = offset
        while True:
            new_diff = min(200, limit - current)
            if new_diff <= 0:
                return
            messages = await self.get_messages(
                chat_id, list(range(current, current + new_diff + 1))
            )
            for message in messages:
                yield message
                current += 1


app = Bot()

# ------------------------
# /setdelay command handler
# ------------------------
@app.on_message(filters.command("setdelay") & filters.group)
async def set_delay(c: Bot, m: types.Message):
    if not m.from_user or not await c.is_admin(m.chat.id, m.from_user.id):
        return
    try:
        delay_sec = int(m.text.split()[1])
    except (IndexError, ValueError):
        return await m.reply("Usage: /setdelay <seconds>")

    await _settings_coll.update_one(
        {"chat_id": m.chat.id},
        {"$set": {"delay": delay_sec}},
        upsert=True,
    )
    await m.reply(f"✅ Auto-delete delay set to {delay_sec} seconds.")

# -----------------------------------
# Auto-delete other group messages
# Only delete non-bot user messages, if /setdelay was used
# -----------------------------------
@app.on_message(filters.group & ~filters.service)
async def delete_later(c: Bot, m: types.Message):
    # ignore messages from bots (including this bot)
    if m.from_user is None or m.from_user.is_bot:
        return

    # fetch custom delay; if not set, skip deletion
    setting = await _settings_coll.find_one({"chat_id": m.chat.id})
    if not setting or "delay" not in setting:
        return

    delay = setting["delay"]
    await asyncio.sleep(delay)
    try:
        await c.delete_messages(m.chat.id, m.id)
    except Exception:
        pass


if __name__ == "__main__":
    app.run()