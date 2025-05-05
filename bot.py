import asyncio
import os
import time
from datetime import date, datetime
import aiohttp
import pytz
from aiohttp import web
from motor.motor_asyncio import AsyncIOMotorClient
from pyrogram import Client, filters, enums, types
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

_mongo = AsyncIOMotorClient(DATABASE_URI)
_settings = _mongo["autodeleter"]["settings"]

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
        b_users, b_chats = await db.get_banned()
        temp.BANNED_USERS = b_users
        temp.BANNED_CHATS = b_chats
        await super().start()
        await Media.ensure_indexes()
        me = await self.get_me()
        temp.ME = me.id
        temp.U_NAME = me.username
        temp.B_NAME = me.first_name
        temp.B_LINK = me.mention
        self.username = "@" + me.username
        self.loop.create_task(check_expired_premium(self))
        self.loop.create_task(self._ping())
        runner = web.AppRunner(await web_server())
        await runner.setup()
        await web.TCPSite(runner, "0.0.0.0", PORT).start()
        tz = pytz.timezone("Asia/Kolkata")
        today = date.today()
        now = datetime.now(tz).strftime("%H:%M:%S %p")
        msg = (
            f"<b>{me.mention} ʀᴇsᴛᴀʀᴛᴇᴅ 🤖\n\n"
            f"📆 ᴅᴀᴛᴇ - <code>{today}</code>\n"
            f"🕙 ᴛɪᴍᴇ - <code>{now}</code>\n"
            f"🌍 ᴛɪᴍᴇ ᴢᴏɴᴇ - <code>Asia/Kolkata</code></b>"
        )
        await self.send_message(LOG_CHANNEL, msg)
        await self.send_message(SUPPORT_GROUP, f"<b>{me.mention} ʀᴇsᴛᴀʀᴛᴇᴅ 🤖</b>")
        elapsed = int(time.time() - self._start_time)
        for admin in ADMINS:
            await self.send_message(
                admin,
                f"<b>✅ ʙᴏᴛ ʀᴇsᴛᴀʀᴛᴇᴅ\n🕥 ᴛɪᴍᴇ ᴛᴀᴋᴇɴ - <code>{elapsed} sᴇᴄᴏɴᴅs</code></b>",
            )

    async def stop(self, *args):
        await super().stop()

    async def _ping(self):
        async with aiohttp.ClientSession() as s:
            while True:
                try:
                    await s.get(PING_URL)
                except:
                    pass
                await asyncio.sleep(30)

    async def is_admin(self, chat_id: Union[int, str], user_id: int) -> bool:
        async for m in self.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
            if m.user.id == user_id:
                return True
        return False

    async def iter_messages(
        self, chat_id: Union[int, str], limit: int, offset: int = 0
    ) -> Optional[AsyncGenerator["types.Message", None]]:
        current = offset
        while True:
            batch = min(200, limit - current)
            if batch <= 0:
                return
            msgs = await self.get_messages(chat_id, list(range(current, current + batch + 1)))
            for msg in msgs:
                yield msg
                current += 1

app = Bot()

@app.on_message(filters.command("setdelay") & filters.group)
async def set_delay(c: Bot, m: types.Message):
    if not m.from_user or not await c.is_admin(m.chat.id, m.from_user.id):
        return
    try:
        sec = int(m.text.split()[1])
    except:
        return await m.reply("Usage: /setdelay <seconds>")
    await _settings.update_one({"chat_id": m.chat.id}, {"$set": {"delay": sec}}, upsert=True)
    await m.reply(f"✅ Auto-delete delay set to {sec} seconds.")

@app.on_message(filters.group & ~filters.service)
async def delete_later(c: Bot, m: types.Message):
    if not m.from_user or m.from_user.is_bot:
        return
    setting = await _settings.find_one({"chat_id": m.chat.id})
    if not setting or "delay" not in setting:
        return
    await asyncio.sleep(setting["delay"])
    try:
        await c.delete_messages(m.chat.id, m.id)
    except:
        pass

if __name__ == "__main__":
    app._start_time = time.time()
    app.run()