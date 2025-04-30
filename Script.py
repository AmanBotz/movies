# © TechifyBots (Rahul)
import asyncio
import re
import math
import logging
from pyrogram.errors.exceptions.bad_request_400 import MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty
from Script import script
from info import MAX_BTN, BIN_CHANNEL, USERNAME, URL, IS_VERIFY, LANGUAGES, AUTH_CHANNEL, SUPPORT_GROUP, SEARCH_GROUP, QR_CODE, DELETE_TIME, PM_SEARCH, ADMINS
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, WebAppInfo 
from pyrogram import Client, filters, enums
from pyrogram.errors import MessageNotModified
from utils import temp, get_settings, is_check_admin, get_status, get_hash, get_name, get_size, save_group_settings, get_poster, get_status, get_readable_time, get_shortlink, is_req_subscribed
from database.users_chats_db import db
from database.ia_filterdb import Media, get_search_results, get_bad_files, get_file_details

lock = asyncio.Lock()

logger = logging.getLogger(__name__)

BUTTONS = {}
FILES_ID = {}
CAP = {}


@Client.on_message(filters.private & filters.text & filters.incoming)
async def pm_search(client, message):
    if PM_SEARCH:
        await auto_filter(client, message)  
    else:
        await message.reply_text("⚠️Sσʀʀʏ I Cαɴ'ᴛ Wσʀᴋ Iɴ Pᴍ")
    
@Client.on_message(filters.group & filters.text & filters.incoming)
async def group_search(client, message):
    chat_id = message.chat.id
    settings = await get_settings(chat_id)
    if settings["auto_filter"]:  
        if 'hindi' in message.text.lower() or 'tamil' in message.text.lower() or 'telugu' in message.text.lower() or 'malayalam' in message.text.lower() or 'kannada' in message.text.lower() or 'english' in message.text.lower() or 'gujarati' in message.text.lower(): 
            return await auto_filter(client, message)

        if message.text.startswith("/"):
            return
        
        elif re.findall(r'https?://\S+|www\.\S+|t\.me/\S+', message.text):
            if await is_check_admin(client, message.chat.id, message.from_user.id):
                return
            await message.delete()
            return await message.reply('<b>‼️ Wʜʏ Yσᴜ Sєɴᴛ Lɪɴᴋ Hᴇʀᴇ \nLɪɴᴋ Nσᴛ Aʟʟσᴡєᴅ Hєʀє 🚫</b>')

        elif '@admin' in message.text.lower() or '@admins' in message.text.lower():
            if await is_check_admin(client, message.chat.id, message.from_user.id):
                return
            admins = []
            async for member in client.get_chat_members(chat_id=message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
                if not member.user.is_bot:
                    admins.append(member.user.id)
                    if member.status == enums.ChatMemberStatus.OWNER:
                        if message.reply_to_message:
                            try:
                                sent_msg = await message.reply_to_message.forward(member.user.id)
                                await sent_msg.reply_text(f"#Attention\n★ User: {message.from_user.mention}\n★ Group: {message.chat.title}\n\n★ <a href={message.reply_to_message.link}>Go to message</a>", disable_web_page_preview=True)
                            except:
                                pass
                        else:
                            try:
                                sent_msg = await message.forward(member.user.id)
                                await sent_msg.reply_text(f"#Attention\n★ User: {message.from_user.mention}\n★ Group: {message.chat.title}\n\n★ <a href={message.link}>Go to message</a>", disable_web_page_preview=True)
                            except:
                                pass
            hidden_mentions = (f'[\u2064](tg://user?id={user_id})' for user_id in admins)
            await message.reply_text('<code>Report sent</code>' + ''.join(hidden_mentions))
            return
        else:
            await auto_filter(client, message)   
    else:
        k=await message.reply_text('<b>⚠️ Aᴜᴛσ Fɪʟᴛєʀ Mσᴅє Is Oғғ...</b>')
        await asyncio.sleep(10)
        await k.delete()
        try:
            await message.delete()
        except:
            pass
                
@Client.on_callback_query(filters.regex(r"^next"))
async def next_page(bot, query):
    ident, req, key, offset = query.data.split("_")
    if int(req) not in [query.from_user.id, 0]:
        return await query.answer(script.ALRT_TXT.format(query.from_user.first_name), show_alert=True)
    try:
        offset = int(offset)
    except:
        offset = 0
    search = BUTTONS.get(key)
    cap = CAP.get(key)
    if not search:
        await query.answer(script.OLD_ALRT_TXT.format(query.from_user.first_name),show_alert=True)
        return
    files, n_offset, total = await get_search_results(search, offset=offset)
    try:
        n_offset = int(n_offset)
    except:
        n_offset = 0
    if not files:
        return
    temp.FILES_ID[key] = files
    grp_id = query.message.chat.id
    settings = await get_settings(query.message.chat.id)
    reqnxt  = query.from_user.id if query.from_user else 0
    temp.CHAT[query.from_user.id] = query.message.chat.id
    del_msg = f"\n\n⚠️ Tʜɪs Mєssαɢє Wɪʟʟ Bє Aᴜᴛσ Dєʟєᴛє Aғᴛєʀ <code>{get_readable_time(DELETE_TIME)}</code> Tᴏ Aᴠσɪᴅ Cσᴘʏʀɪɢʜᴛ Issᴜєs." if settings["auto_delete"] else ''
    links = ""
    if settings["link"]:
        btn = []
        for file_num, file in enumerate(files, start=offset+1):
            links += f"""<b>\n\n{file_num}. <a href=https://t.me/{temp.U_NAME}?start=file_{query.message.chat.id}_{file.file_id}>[{get_size(file.file_size)}] {' '.join(filter(lambda x: not x.startswith('[') and not x.startswith('@') and not x.startswith('www.'), file.file_name.split()))}</a></b>"""
    else:
        btn = [[InlineKeyboardButton(text=f"🔗 {get_size(file.file_size)}≽ {get_name(file.file_name)}", url=f'https://telegram.dog/{temp.U_NAME}?start=file_{query.message.chat.id}_{file.file_id}'),]
                for file in files
              ]

    if not settings["is_verify"]:
        btn.insert(0,[
            InlineKeyboardButton("⇌ Bᴜʏ Pʀєᴍɪᴜᴍ ⇋", url=f"https://t.me/{temp.U_NAME}?start=buy_premium")
        ])


    else:
        btn.insert(0,[
            InlineKeyboardButton("⇌ Bᴜʏ Pʀєᴍɪᴜᴍ ⇋", url=f"https://t.me/{temp.U_NAME}?start=buy_premium")
        ])

    if 0 < offset <= int(MAX_BTN):
        off_set = 0
    elif offset == 0:
        off_set = None
    else:
        off_set = offset - int(MAX_BTN)
    if n_offset == 0:

        btn.append(
            [InlineKeyboardButton("☚ Bαᴄᴋ", callback_data=f"next_{req}_{key}_{off_set}"),
             InlineKeyboardButton(f"Pαɢє {math.ceil(int(offset) / int(MAX_BTN)) + 1} / {math.ceil(total / int(MAX_BTN))}", callback_data="pages")]
        )
    elif off_set is None:
        btn.append(
            [InlineKeyboardButton(f"{math.ceil(int(offset) / int(MAX_BTN)) + 1} / {math.ceil(total / int(MAX_BTN))}", callback_data="pages"),
             InlineKeyboardButton("Nєxᴛ ☛", callback_data=f"next_{req}_{key}_{n_offset}")])
    else:
        btn.append(
            [
                InlineKeyboardButton("☚ Bαᴄᴋ", callback_data=f"next_{req}_{key}_{off_set}"),
                InlineKeyboardButton(f"{math.ceil(int(offset) / int(MAX_BTN)) + 1} / {math.ceil(total / int(MAX_BTN))}", callback_data="pages"),
                InlineKeyboardButton("Nєxᴛ ☛", callback_data=f"next_{req}_{key}_{n_offset}")
            ],
        )
    if settings["link"]:
        links = ""
        for file_num, file in enumerate(files, start=offset+1):
            links += f"""<b>\n\n{file_num}. <a href=https://t.me/{temp.U_NAME}?start=file_{query.message.chat.id}_{file.file_id}>[{get_size(file.file_size)}] {' '.join(filter(lambda x: not x.startswith('[') and not x.startswith('@') and not x.startswith('www.'), file.file_name.split()))}</a></b>"""
        await query.message.edit_text(cap + links + del_msg, disable_web_page_preview=True, parse_mode=enums.ParseMode.HTML, reply_markup=InlineKeyboardMarkup(btn))
        return        
    try:
        await query.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(btn)
        )
    except MessageNotModified:
        pass
    await query.answer()
    
@Client.on_callback_query(filters.regex(r"^languages"))
async def languages_cb_handler(client: Client, query: CallbackQuery):
    _, key, req, offset = query.data.split("#")
    if int(req) != query.from_user.id:
        return await query.answer(script.ALRT_TXT, show_alert=True)
    btn = [[
        InlineKeyboardButton(text=lang.title(), callback_data=f"lang_search#{lang}#{key}#{offset}#{req}"),
    ]
        for lang in LANGUAGES
    ]
    btn.append([InlineKeyboardButton(text="☚ Bαᴄᴋ Tᴏ Mαɪɴ Pαɢє", callback_data=f"next_{req}_{key}_{offset}")])
    d=await query.message.edit_text("Iɴ Wʜɪᴄʜ Lαɴɢᴜαɢє Yσᴜ Wαɴᴛ, Cʜσσsє Oɴє ☟☟", reply_markup=InlineKeyboardMarkup(btn), disable_web_page_preview=True)
    await asyncio.sleep(600)
    await d.delete()

@Client.on_callback_query(filters.regex(r"^lang_search"))
async def lang_search(client: Client, query: CallbackQuery):
    _, lang, key, offset, req = query.data.split("#")
    if int(req) != query.from_user.id:
        return await query.answer(script.ALRT_TXT, show_alert=True)	
    offset = int(offset)
    search = BUTTONS.get(key)
    cap = CAP.get(key)
    if not search:
        await query.answer(script.OLD_ALRT_TXT.format(query.from_user.first_name),show_alert=True)
        return 
    search = search.replace("_", " ")
    files, n_offset, total_results = await get_search_results(search, lang=lang)
    if not files:
        await query.answer(f"Sσʀʀʏ '{lang.title()}' Lαɴɢᴜαɢє Fɪʟєs Nσᴛ Fσᴜɴᴅ 😕", show_alert=1)
        return
    temp.FILES_ID[key] = files
    reqnxt = query.from_user.id if query.from_user else 0
    settings = await get_settings(query.message.chat.id)
    group_id = query.message.chat.id
    del_msg = f"\n\n⚠️ Tʜɪs Mєssαɢє Wɪʟʟ Bє Aᴜᴛσ Dєʟєᴛє Aғᴛєʀ <code>{get_readable_time(DELETE_TIME)}</code> Tᴏ Aᴠσɪᴅ Cσᴘʏʀɪɢʜᴛ Issᴜєs." if settings["auto_delete"] else ''
    links = ""
    if settings["link"]:
        btn = []
        for file_num, file in enumerate(files, start=1):
            links += f"""<b>\n\n{file_num}. <a href=https://t.me/{temp.U_NAME}?start=file_{query.message.chat.id}_{file.file_id}>[{get_size(file.file_size)}] {' '.join(filter(lambda x: not x.startswith('[') and not x.startswith('@') and not x.startswith('www.'), file.file_name.split()))}</a></b>"""
    else:
        btn = [[
                InlineKeyboardButton(text=f"🔗 {get_size(file.file_size)}≽ {get_name(file.file_name)}", callback_data=f'files#{reqnxt}#{file.file_id}'),]
                   for file in files
              ]
    if not settings["is_verify"]:
        btn.insert(0,[
            InlineKeyboardButton("⇌ Bᴜʏ Pʀєᴍɪᴜᴍ ⇋", url=f"https://t.me/{temp.U_NAME}?start=buy_premium")
        ])
    else:
        btn.insert(0,[
            InlineKeyboardButton("⇌ Bᴜʏ Pʀєᴍɪᴜᴍ ⇋", url=f"https://t.me/{temp.U_NAME}?start=buy_premium")
        ])
    if n_offset != "":
        btn.append(
            [InlineKeyboardButton(text=f"1/{math.ceil(int(total_results) / MAX_BTN)}", callback_data="buttons"),
             InlineKeyboardButton(text="Nєxᴛ ☛", callback_data=f"lang_next#{req}#{key}#{lang}#{n_offset}#{offset}")]
        )
    btn.append([InlineKeyboardButton(text="☚ Bαᴄᴋ Tᴏ Mαɪɴ Pαɢє", callback_data=f"next_{req}_{key}_{offset}")])
    await query.message.edit_text(cap + links + del_msg, disable_web_page_preview=True, parse_mode=enums.ParseMode.HTML, reply_markup=InlineKeyboardMarkup(btn))

@Client.on_callback_query(filters.regex(r"^lang_next"))
async def lang_next_page(bot, query):
    ident, req, key, lang, l_offset, offset = query.data.split("#")
    if int(req) != query.from_user.id:
        return await query.answer(script.ALRT_TXT, show_alert=True)	
    try:
        l_offset = int(l_offset)
    except:
        l_offset = 0
    search = BUTTONS.get(key)
    cap = CAP.get(key)
    grp_id = query.message.chat.id
    settings = await get_settings(query.message.chat.id)
    del_msg = f"\n\n⚠️ Tʜɪs Mєssαɢє Wɪʟʟ Bє Aᴜᴛσ Dєʟєᴛє Aғᴛєʀ <code>{get_readable_time(DELETE_TIME)}</code> Tᴏ Aᴠσɪᴅ Cσᴘʏʀɪɢʜᴛ Issᴜєs." if settings["auto_delete"] else ''
    if not search:
        await query.answer(f"Sσʀʀʏ '{lang.title()}' Lαɴɢᴜαɢє Fɪʟєs Nσᴛ Fσᴜɴᴅ 😕", show_alert=1)
        return
    files, n_offset, total = await get_search_results(search, offset=l_offset, lang=lang)
    if not files:
        return
    temp.FILES_ID[key] = files
    try:
        n_offset = int(n_offset)
    except:
        n_offset = 0
    links = ""
    if settings['link']:
        btn = []
        for file_num, file in enumerate(files, start=l_offset+1):
            links += f"""<b>\n\n{file_num}. <a href=https://t.me/{temp.U_NAME}?start=file_{query.message.chat.id}_{file.file_id}>[{get_size(file.file_size)}] {' '.join(filter(lambda x: not x.startswith('[') and not x.startswith('@') and not x.startswith('www.'), file.file_name.split()))}</a></b>"""
    else:
        btn = [[
            InlineKeyboardButton(text=f"🔗 {get_size(file.file_size)}≽ {get_name(file.file_name)}", callback_data=f'file#{file.file_id}')
        ]
            for file in files
        ]
    if not settings['is_verify']:
        btn.insert(0,[
            InlineKeyboardButton("⇌ Bᴜʏ Pʀєᴍɪᴜᴍ ⇋", url=f"https://t.me/{temp.U_NAME}?start=buy_premium")
        ])
    else:
        btn.insert(0,[
            InlineKeyboardButton("⇌ Bᴜʏ Pʀєᴍɪᴜᴍ ⇋", url=f"https://t.me/{temp.U_NAME}?start=buy_premium")
        ])
    if 0 < l_offset <= MAX_BTN:
        b_offset = 0
    elif l_offset == 0:
        b_offset = None
    else:
        b_offset = l_offset - MAX_BTN
    if n_offset == 0:
        btn.append(
            [InlineKeyboardButton("☚ Bαᴄᴋ", callback_data=f"lang_next#{req}#{key}#{lang}#{b_offset}#{offset}"),
             InlineKeyboardButton(f"{math.ceil(int(l_offset) / MAX_BTN) + 1}/{math.ceil(total / MAX_BTN)}", callback_data="buttons")]
        )
    elif b_offset is None:
        btn.append(
            [InlineKeyboardButton(f"{math.ceil(int(l_offset) / MAX_BTN) + 1}/{math.ceil(total / MAX_BTN)}", callback_data="buttons"),
             InlineKeyboardButton("Nєxᴛ ☛", callback_data=f"lang_next#{req}#{key}#{lang}#{n_offset}#{offset}")]
        )
    else:
        btn.append(
            [InlineKeyboardButton("☚ Bαᴄᴋ", callback_data=f"lang_next#{req}#{key}#{lang}#{b_offset}#{offset}"),
             InlineKeyboardButton(f"{math.ceil(int(l_offset) / MAX_BTN) + 1}/{math.ceil(total / MAX_BTN)}", callback_data="buttons"),
             InlineKeyboardButton("Nєxᴛ ☛", callback_data=f"lang_next#{req}#{key}#{lang}#{n_offset}#{offset}")]
        )
    btn.append([InlineKeyboardButton(text="☚ Bαᴄᴋ Tᴏ Mαɪɴ Pαɢє", callback_data=f"next_{req}_{key}_{offset}")])
    await query.message.edit_text(cap + links + del_msg, reply_markup=InlineKeyboardMarkup(btn), disable_web_page_preview=True, parse_mode=enums.ParseMode.HTML)

@Client.on_callback_query(filters.regex(r"^spol"))
async def advantage_spoll_choker(bot, query):
    _, id, user = query.data.split('#')
    if int(user) != 0 and query.from_user.id != int(user):
        return await query.answer(script.ALRT_TXT, show_alert=True)
    movie = await get_poster(id, id=True)
    search = movie.get('title')
    await query.answer('Cʜєcᴋɪɴɢ Iɴ Mʏ Dαᴛαʙαsє...')
    files, offset, total_results = await get_search_results(search)
    if files:
        k = (search, files, offset, total_results)
        await auto_filter(bot, query, k)
    else:
        k = await query.message.edit(script.NO_RESULT_TXT)
        await asyncio.sleep(60)
        await k.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass

@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data == "close_data":
        try:
            user = query.message.reply_to_message.from_user.id
        except:
            user = query.from_user.id
        if int(user) != 0 and query.from_user.id != int(user):
            return await query.answer(script.ALRT_TXT, show_alert=True)
        await query.answer("Tʜαɴᴋs Fσʀ Cʟσsє")
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass

    elif query.data.startswith("checksub"):
        ident, file_id = query.data.split("#")
        settings = await get_settings(query.message.chat.id)
        if AUTH_CHANNEL and not await is_req_subscribed(client, query):
            await query.answer("I Lɪᴋє Yσᴜʀ Sᴍαʀᴛɴєss Bᴜᴛ Dσɴ'ᴛ Bє OᴠєʀSᴍαʀᴛ 😒\nFɪʀsᴛ Jσɪɴ Oᴜʀ Uᴘᴅαᴛєs Cʜαɴɴєʟ😒", show_alert=True)
            return         
        files_ = await get_file_details(file_id)
        if not files_:
            return await query.answer('Nσ Sᴜᴄʜ Fɪʟє Exɪsᴛs 🚫')
        files = files_[0]
        CAPTION = settings['caption']
        f_caption = CAPTION.format(
            file_name = files.file_name,
            file_size = get_size(files.file_size),
            file_caption = files.caption
        )
        await client.send_cached_media(
            chat_id=query.from_user.id,
            file_id=file_id,
            caption=f_caption,
            protect_content=settings['file_secure'],
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('✠ Cʟσsє ✠', callback_data='close_data')
                    ]
                ]
            )
        )

    elif query.data.startswith("stream"):
        user_id = query.from_user.id
        if not await db.has_premium_access(user_id):
            d=await query.message.reply("💔Tʜɪs Fєαᴛᴜʀє Is Oɴʟʏ Fσʀ Bσᴛ Pʀєᴍɪᴜᴍ Usєʀs.\n\n Iғ Yσᴜ Wαɴᴛ Bσᴛ Sᴜʙᴄʀɪᴘᴛɪσɴ Tʜєɴ Sєɴᴅ /plan")
            await asyncio.sleep(120)
            await d.delete()
            return
        file_id = query.data.split('#', 1)[1]
        NOBITA = await client.send_cached_media(
            chat_id=BIN_CHANNEL,
            file_id=file_id)
        online = f"https://{URL}/watch/{NOBITA.id}?hash={get_hash(NOBITA)}"
        download = f"https://{URL}/{NOBITA.id}?hash={get_hash(NOBITA)}"
        btn= [[
            InlineKeyboardButton("Wαᴛᴄʜ Oɴʟɪɴє", url=online),
            InlineKeyboardButton("Fαsᴛ Dσᴡɴʟσαᴅ", url=download)
        ],[
            InlineKeyboardButton('🧿 Wαᴛᴄʜ Oɴ Tєʟєɢʀαᴍ 🖥', web_app=WebAppInfo(url=online))
        ]]
        await query.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(btn)
        )

    elif query.data == "buttons":
        await query.answer("Nσ Mσʀє Pαɢєs 😊", show_alert=True)

    elif query.data == "pages":
        await query.answer("Tʜɪs Is Pαɢєs Bᴜᴛᴛᴏɴ 😅")

    elif query.data.startswith("lang_art"):
        _, lang = query.data.split("#")
        await query.answer(f"Yσᴜ Sєʟєᴄᴛєᴅ {lang.title()} Lαɴɢᴜαɢє ⚡️", show_alert=True)
  
    elif query.data == "start":
        buttons = [[
            InlineKeyboardButton('👀 Sєαʀᴄʜ Gʀσᴜᴘ 👀', url=SEARCH_GROUP)
        ],[
            InlineKeyboardButton('💸 Pʀєᴍɪᴜᴍ', callback_data='buy_premium')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.START_TXT.format(query.from_user.mention, get_status(), query.from_user.id),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )      
    elif query.data == "features":
        buttons = [[
            InlineKeyboardButton('📸 Iᴍαɢє', callback_data='rahul'),
            InlineKeyboardButton('🆎️ Fσɴᴛ', callback_data='font')    
        ], [ 
            InlineKeyboardButton('☚ Bαᴄᴋ', callback_data='start')
        ]] 
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(                     
            text=script.HELP_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )

    elif query.data.startswith("techifybots"):
        ident, keyword = 