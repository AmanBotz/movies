import os
class script(object):
    
    START_TXT = """<blockquote>Hєʏ {} {}</blockquote>
    
I Aᴍ A Pσᴡєʀғᴜʟ Mσᴠɪє Pʀσᴠɪᴅєʀ Bσᴛ. I Cαɴ Pʀσᴠɪᴅє Yσᴜ Mσᴠɪєs, Sєʀɪєs & Aɴɪᴍєs Dɪʀєᴄᴛʟʏ Hєʀє Oʀ Yσᴜ Cαɴ Sєαʀᴄʜ Iɴ Oᴜʀ Gʀσᴜᴘ...
"""
    
    HELP_TXT = """<b><i>ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴꜱ ᴛᴏ ɢᴇᴛ ᴅᴏᴄᴜᴍᴇɴᴛᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ꜱᴘᴇᴄɪꜰɪᴄ ᴍᴏᴅᴜʟᴇꜱ..</i></b>"""
    
    CODEXBOTS = """<b><i>/upload - sᴇɴᴅ ᴍᴇ ᴘɪᴄᴛᴜʀᴇ ᴏʀ ᴠɪᴅᴇᴏ ᴜɴᴅᴇʀ (5ᴍʙ)

ɴᴏᴛᴇ - ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴡᴏʀᴋ ɪɴ ᴘᴍ</i></b>"""
 
    STATUS_TXT = """<b><u>🗃 Dᴀᴛᴀʙᴀsᴇ 1 🗃</u>

» Tᴏᴛᴀʟ Usᴇʀs - <code>{}</code>
» Tᴏᴛᴀʟ Gʀᴏᴜᴘs - <code>{}</code>
» Usᴇᴅ Sᴛᴏʀᴀɢᴇ - <code>{} / {}</code>

<u>🗳 Dᴀᴛᴀʙᴀsᴇ 2 🗳</u></b>

» Tᴏᴛᴀʟ Fɪʟᴇs - <code>{}</code>
» Usᴇᴅ Sᴛᴏʀᴀɢᴇ - <code>{} / {}</code>

<u>🤖 Bᴏᴛ Dᴇᴛᴀɪʟs 🤖</u>

» Uᴘᴛɪᴍᴇ - <code>{}</code>
» Rᴀᴍ - <code>{}%</code>
» Cᴘᴜ - <code>{}%</code></b>"""

    NEW_USER_TXT = """<b>#New_User

≈ ɪᴅ:- <code>{}</code>
≈ ɴᴀᴍᴇ:- {}</b>"""

    NEW_GROUP_TXT = """#New_Group

Group name - {}
Id - <code>{}</code>
Group username - @{}
Group link - {}
Total members - <code>{}</code>
User - {}"""

    IMDB_TEMPLATE_TXT = """<b>📻 ᴛɪᴛʟᴇ - <a href={url}>{title}</a>
🎭 ɢᴇɴʀᴇs - {genres}
🎖 ʀᴀᴛɪɴɢ - <a href={url}/ratings>{rating}</a> / 10 (ʙᴀsᴇᴅ ᴏɴ {votes} ᴜsᴇʀ ʀᴀᴛɪɴɢ.)
📆 ʏᴇᴀʀ - {release_date}
❗️ ʟᴀɴɢᴜᴀɢᴇ - {languages}</b>
"""

    FILE_CAPTION = """<a href=https://telegram.me/Haxoff> {file_name} </a>

<blockquote>Tʜɪs Fɪʟє Wɪʟʟ Bє Dєʟєᴛєᴅ Iɴ 2 Mɪɴᴜᴛєs Tσ Aᴠσɪᴅ Cσᴘʏʀɪɢʜᴛ. Sᴏ Pʟєαsє Fᴏʀᴡαʀᴅ Tʜɪs Fɪʟє Tσ Sαᴠєᴅ Mєssαɢєs.</blockquote>"""

    RESTART_TXT = """<b>
📅 Dᴀᴛᴇ : <code>{}</code>
⏰ Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code></b>"""

    ALRT_TXT = """❌ Tʜɪs Is Nσᴛ Fσʀ Yσᴜ Sɪʀ ⛔️"""

    OLD_ALRT_TXT = """Yσu Aʀє Usíɴɢ Oɴє Oғ Mʏ Oʟᴅ Mєssαɢєs, Pʟєαsє Sєɴᴅ Tʜє Rєǫᴜєsᴛ Aɢαɪɴ."""

    NO_RESULT_TXT = """🗳 Tʜɪs Rєǫᴜєsᴛ Is Nσᴛ Avαɪʟαвʟє. Yσᴜʀ Rєǫᴜᴇsᴛ Sєnt Tσ Aᴅᴍɪɴs, Iᴛ Wɪʟʟ Bє Aᴅᴅєᴅ As Sσσɴ As Pσssɪвʟє, Yσᴜ Wɪʟʟ Bє Nσᴛɪғɪєᴅ.🗳"""
    
    I_CUDNT = """<blockquote>🤧 Hєʟʟᴏ {}</blockquote>

I Cσᴜʟᴅɴ'ᴛ Fɪɴᴅ Aɴʏ Mσvɪє Oʀ Sєʀɪєs Iɴ Tʜαᴛ Nαᴍє.. 😐"""

    I_CUD_NT = """<blockquote>😑 Hєʟʟᴏ {} </blockquote>

I Cσᴜʟᴅ'ᴛ Fɪɴᴅ Aɴʏᴛʜɪɴɢ Rєʟᴀᴛєᴅ Tᴏ Tʜαᴛ 😞... Cʜєᴄᴋ Yσᴜʀ Sᴘєʟʟɪɴɢ."""
    
    CUDNT_FND = """<blockquote>✯ Hєʟʟσ {}</blockquote>

I Cσᴜʟᴅɴ'ᴛ Fɪɴᴅ Aɴʏᴛʜɪɴɢ Rєʟᴀᴛєᴅ Tσ Tʜαᴛ. Dɪᴅ Yσᴜ Mєαɴ Aɴʏ Oɴє Oғ Tʜєsє ?? ☟ ☟"""
    
    FONT_TXT= """<b><i>ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴍᴏᴅᴇ ᴛᴏ ᴄʜᴀɴɢᴇ ʏᴏᴜʀ ꜰᴏɴᴛs sᴛʏʟᴇ.</i></b>

<code>/font hi how are you</code>"""

    PREMIUM_TEXT = """<blockquote>Avαɪʟαвʟє Pʟαɴs  ️☟</blockquote>

◆ 𝟷 Wєєᴋ  -  ₹𝟹𝟶
◆ 𝟷 Mσɴᴛʜ  -  ₹𝟻𝟶
◆ 𝟹 Mσɴᴛʜs  -  ₹𝟷𝟶𝟶
◆ 𝟼 Mσɴᴛʜs  -  ₹𝟸𝟶𝟶

•─────•─────────•─────•
<blockquote>Pʀєᴍɪᴜᴍ Fєαᴛᴜʀєs  🎁</blockquote>

☛ Nσ NєєD Tᴏ Vєʀɪғʏ
☛ Dɪʀєᴄᴛ Fɪʟєs
☛ Aᴅ-Fʀєє Exᴘєʀɪєɴᴄє
☛ Uɴʟɪᴍɪᴛєᴅ Mσᴠɪєs, Sєʀɪєs & Aɴɪᴍєs

☛ Fᴜʟʟ Aᴅᴍɪɴ Sᴜᴘᴘσʀᴛ
☛ Rєǫᴜєsᴛ Wɪʟʟ Bє Cσᴍᴘʟєᴛєᴅ Iɴ 𝟷Hσᴜʀ
•─────•─────────•─────•

⇢ Cʜєᴄᴋ Yσᴜʀ Aᴄᴛɪᴠє Pʟαɴ /myplan

‼️ Cσɴᴛαcᴛ Us Oɴ Oᴜʀ Bσᴛ @HaxoffBot Fσʀ Bᴜʏɪɴɢ Pʀєᴍɪᴜᴍ Oʀ Aɴʏ Oᴛʜєʀ Qᴜєʀʏ"""

    EARN_TEXT = """<b><i><blockquote>ʜᴏᴡ ᴛᴏ ᴇᴀʀɴ ᴍᴏɴᴇʏ ʙʏ ᴛʜɪs ʙᴏᴛ  🤑</blockquote>

›› sᴛᴇᴘ 𝟷 : ʏᴏᴜ ᴍᴜsᴛ ʜᴀᴠᴇ ᴀᴛʟᴇᴀsᴛ ᴏɴᴇ ɢʀᴏᴜᴘ ᴡɪᴛʜ ᴍɪɴɪᴍᴜᴍ 𝟹𝟶𝟶 ᴍᴇᴍʙᴇʀs.

›› sᴛᴇᴘ 𝟸 : ᴍᴀᴋᴇ <a href=https://telegram.me/{}</a> ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ.

›› sᴛᴇᴘ 𝟹 : ᴍᴀᴋᴇ ᴀᴄᴄᴏᴜɴᴛ ᴏɴ <a href='https://tnshort.net/ref/devilofficial'>ᴛɴʟɪɴᴋ</a> ᴏʀ <a href='https://onepagelink.in/ref/Nobita'>ᴏɴᴇᴘᴀɢᴇʟɪɴᴋ</a>. [ ʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴜsᴇ ᴏᴛʜᴇʀ sʜᴏʀᴛɴᴇʀ ᴡᴇʙsɪᴛᴇ ]

›› sᴛᴇᴘ 𝟺 : ɴᴏᴡ ꜱᴇᴛ ʏᴏᴜʀ ꜱʜᴏʀᴛɴᴇʀ, ᴛᴜᴛᴏʀɪᴀʟ, ꜰꜱᴜʙ ᴀɴᴅ ʟᴏɢ ᴄʜᴀɴɴᴇʟ.

›› sᴛᴇᴘ 𝟻 : ꜰᴏʟʟᴏᴡ ᴛʜᴇsᴇ <a href='https://github.com/TechifyBots/Auto-Filter-Bot/blob/main/README.md'>ɪɴꜱᴛʀᴜᴄᴛɪᴏɴꜱ</a>.

ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴠᴀʟᴜᴇꜱ ʙʏ /ginfo ᴄᴏᴍᴍᴀɴᴅ.

💯 ɴᴏᴛᴇ - ᴛʜɪs ʙᴏᴛ ɪs ꜰʀᴇᴇ ᴛᴏ ᴀʟʟ, ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘs ᴀɴᴅ ᴇᴀʀɴ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏɴᴇʏ.</i></b>"""

    VERIFICATION_TEXT = """<blockquote>Hєʏ {} {}</blockquote>

❝Yσᴜʀ Aʀє Nσᴛ Vєʀɪғɪєᴅ Tσᴅαʏ❞

Cʟɪᴄᴋ Oɴ Vєʀɪғʏ Aɴᴅ Gєᴛ Uɴʟɪᴍɪᴛєᴅ Aᴄᴄєss Tɪʟʟ Mɪᴅɴɪɢʜᴛ 12αᴍ.

<blockquote>Iғ Yσᴜ Wαɴᴛ Dɪʀєᴄᴛ Fɪʟєs Tʜєɴ Yσᴜ Cαn Bᴜʏ Pʀєᴍɪᴜᴍ. [Nσ Nєєᴅ Tσ Vєʀɪғʏ]</blockquote>

Cʜєᴄᴋ /plan Fσʀ Mσʀє Dєᴛαɪʟs..."""

    VERIFY_COMPLETE_TEXT = """<blockquote>Hєʏ {}</blockquote>

☑️ Yσᴜ Hαvє Cσᴍᴘєʟєᴛєᴅ Tʜє Vєʀɪғɪᴄαᴛɪσɴ ...

☛ Nσᴡ Yσᴜ Hαᴠє Uɴʟɪᴍɪᴛєᴅ Aᴄᴄєss Tɪʟʟ Mɪᴅɴɪɢʜᴛ 12αᴍ ❤️ 🔥

<blockquote>Iғ Yσᴜ Wαɴᴛ Dɪʀєᴄᴛ Fɪʟєs Wɪᴛʜσᴜᴛ Vєʀɪғɪᴄαᴛɪσɴ Tʜєɴ Bᴜʏ Oᴜʀ Sᴜʙᴄʀɪᴘᴛɪσɴ</blockquote>

💶 Cʜєᴄᴋ /plan Fσʀ Bᴜʏ Sᴜʙᴄʀɪᴘᴛɪσɴ"""

    SECOND_VERIFICATION_TEXT = """<b>ʜʏ {} {},

ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴠᴇʀɪꜰɪᴇᴅ ᴛᴏᴅᴀʏ 😐
ᴄʟɪᴄᴋ ᴏɴ ᴠᴇʀɪꜰʏ ᴀɴᴅ ɢᴇᴛ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇꜱꜱ ᴛɪʟʟ ɴᴇxᴛ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ

#ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ:- 2/3

<blockquote>ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴅɪʀᴇᴄᴛ ꜰɪʟᴇs ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴛᴀᴋᴇ ᴘʀᴇᴍɪᴜᴍ sᴇʀᴠɪᴄᴇ. (ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪꜰʏ)</blockquote>

ᴄʜᴇᴄᴋ /plan ꜰᴏʀ ᴍᴏʀᴇ ᴅᴇᴛᴀɪʟꜱ...</b>"""

    SECOND_VERIFY_COMPLETE_TEXT = """<b>ʜʏ {},

ʏᴏᴜ ʜᴀᴠᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛʜᴇ 𝟸ɴᴅ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ...

ɴᴏᴡ ʏᴏᴜ ʜᴀᴠᴇ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ᴛɪʟʟ ɴᴇxᴛ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ❤️‍🔥

ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴅɪʀᴇᴄᴛ ꜰɪʟᴇꜱ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴꜱ ᴛʜᴇɴ ʙᴜʏ ᴏᴜʀ ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ 😁

💶 ᴄʜᴇᴄᴋ /plan ᴛᴏ ʙᴜʏ ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ</b>"""

    THIRDT_VERIFICATION_TEXT = """<b>ʜʏ {} {},

ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴠᴇʀɪꜰɪᴇᴅ ‼️
ᴛᴀᴘ ᴏɴ ᴛʜᴇ ᴠᴇʀɪꜰʏ ʟɪɴᴋ ᴀɴᴅ ɢᴇᴛ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ꜰᴏʀ ᴛᴏᴅᴀʏ 😇

#ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ:- 3/3

<blockquote>ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴅɪʀᴇᴄᴛ ꜰɪʟᴇs ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴛᴀᴋᴇ ᴘʀᴇᴍɪᴜᴍ sᴇʀᴠɪᴄᴇ. (ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪꜰʏ)</blockquote>

ᴄʜᴇᴄᴋ /plan ꜰᴏʀ ᴍᴏʀᴇ ᴅᴇᴛᴀɪʟꜱ...</b>"""

    THIRDT_VERIFY_COMPLETE_TEXT= """<b>ʜʏ {},

ʏᴏᴜ ᴀʀᴇ ɴᴏᴡ ᴠᴇʀɪꜰɪᴇᴅ ꜰᴏʀ ᴛᴏᴅᴀʏ ☺️

ᴇɴᴊᴏʏ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇꜱ, ꜱᴇʀɪᴇꜱ ᴏʀ ᴀɴɪᴍᴇ 💥

ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴅɪʀᴇᴄᴛ ꜰɪʟᴇꜱ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴꜱ ᴛʜᴇɴ ʙᴜʏ ᴏᴜʀ ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ 😁

💶 ᴄʜᴇᴄᴋ /plan ᴛᴏ ʙᴜʏ ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ</b>"""

    VERIFIED_LOG_TEXT = """<b><u>☄ ᴜsᴇʀ ᴠᴇʀɪꜰɪᴇᴅ sᴜᴄᴄᴇssꜰᴜʟʟʏ ☄</u>

⚡️ ɴᴀᴍᴇ:- {} [ <code>{}</code> ] 
📆 ᴅᴀᴛᴇ:- <code>{} </code></b>

#verification_{}_completed"""

    CUSTOM_TEXT = """<b><i>😊 <u>ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅꜱ</u> 😊
    
/shortlink - ᴛᴏ ꜱᴇᴛ ꜱʜᴏʀᴛᴇɴᴇʀ
/shortlink2 - ᴛᴏ ꜱᴇᴛ ꜱʜᴏʀᴛᴇɴᴇʀ ꜰᴏʀ 𝟸ɴᴅ ᴠᴇʀɪꜰʏ
/shortlink3 - ᴛᴏ ꜱᴇᴛ ꜱʜᴏʀᴛᴇɴᴇʀ ꜰᴏʀ 𝟹ʀᴅ ᴠᴇʀɪꜰʏ
/time2 - ᴛᴏ ꜱᴇᴛ 𝟸ɴᴅ ꜱʜᴏʀᴛᴇɴᴇʀ ᴠᴇʀɪꜰʏ ᴛɪᴍᴇ
/time3 - ᴛᴏ ꜱᴇᴛ 𝟹ʀᴅ ꜱʜᴏʀᴛᴇɴᴇʀ ᴠᴇʀɪꜰʏ ᴛɪᴍᴇ
/log - ᴛᴏ ꜱᴇᴛ ʟᴏɢ ᴄʜᴀɴɴᴇʟ ꜰᴏʀ ᴜꜱᴇʀꜱ ᴅᴀᴛᴀ
/tutorial - ᴛᴏ ꜱᴇᴛ 𝟷ꜱᴛ ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ ʟɪɴᴋ
/tutorial2 - ᴛᴏ ꜱᴇᴛ 𝟸ɴᴅ ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ ʟɪɴᴋ
/tutorial3 - ᴛᴏ ꜱᴇᴛ 𝟹ʀᴅ ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ ʟɪɴᴋ
/caption - ᴛᴏ ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ꜰɪʟᴇ ᴄᴀᴘᴛɪᴏɴ
/template - ᴛᴏ ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ɪᴍᴅʙ ᴛᴇᴍᴘʟᴀᴛᴇ
/fsub - ᴛᴏ ꜱᴇᴛ ʏᴏᴜʀ ꜰᴏʀᴄᴇ ꜱᴜʙꜱᴄʀɪʙᴇ ᴄʜᴀɴɴᴇʟ
/nofsub - ᴛᴏ ʀᴇᴍᴏᴠᴇ ꜰᴏʀᴄᴇ ꜱᴜʙ ᴄʜᴀɴɴᴇʟ
/ginfo - ᴛᴏ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴅᴇᴛᴀɪʟꜱ</i></b>

😘 𝑰𝒇 𝒚𝒐𝒖 𝒅𝒐 𝒂𝒍𝒍 𝒕𝒉𝒊𝒔 𝒕𝒉𝒆𝒏 𝒚𝒐𝒖𝒓 𝒈𝒓𝒐𝒖𝒑 𝒘𝒊𝒍𝒍 𝒃𝒆 𝒗𝒆𝒓𝒚 𝑪𝒐𝒐𝒍..."""

    FSUB_TXT = """{},

🙁 Fɪʀsᴛ Jσɪɴ Oᴜʀ Cʜαɴɴєʟ Tʜєɴ Yσᴜ Wɪʟʟ Gєᴛ Fɪʟє, Oᴛʜєʀᴡɪsє Yσᴜ Wɪʟʟ Nσᴛ Gєᴛ Iᴛ.

☟☟ Jσɪɴ Nσᴡ ☟☟"""

    DONATE_TXT = """<blockquote>❤️‍🔥 𝐓𝐡𝐚𝐧𝐤𝐬 𝐟𝐨𝐫 𝐬𝐡𝐨𝐰𝐢𝐧𝐠 𝐢𝐧𝐭𝐞𝐫𝐞𝐬𝐭 𝐢𝐧 𝐃𝐨𝐧𝐚𝐭𝐢𝐨𝐧</blockquote>

<b><i>💞  ɪꜰ ʏᴏᴜ ʟɪᴋᴇ ᴏᴜʀ ʙᴏᴛ ꜰᴇᴇʟ ꜰʀᴇᴇ ᴛᴏ ᴅᴏɴᴀᴛᴇ ᴀɴʏ ᴀᴍᴏᴜɴᴛ ₹𝟷𝟶, ₹𝟸𝟶, ₹𝟻𝟶, ₹𝟷𝟶𝟶, ᴇᴛᴄ.</i></b>

❣️ 𝐷𝑜𝑛𝑎𝑡𝑖𝑜𝑛𝑠 𝑎𝑟𝑒 𝑟𝑒𝑎𝑙𝑙𝑦 𝑎𝑝𝑝𝑟𝑒𝑐𝑖𝑎𝑡𝑒𝑑 𝑖𝑡 ℎ𝑒𝑙𝑝𝑠 𝑖𝑛 𝑏𝑜𝑡 𝑑𝑒𝑣𝑒𝑙𝑜𝑝𝑚𝑒𝑛𝑡

💖 @HaxoffBot
"""
