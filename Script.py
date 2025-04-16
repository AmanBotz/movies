import os

class script(object):
    
    START_TXT = """<b>𝖨 𝖠𝗆 𝖠 𝖯𝗈𝗐𝖾𝗋𝖿𝗎𝗅 𝖬𝗈𝗏𝗂𝖾𝗌 𝖡𝗈𝗍. 𝖨 𝖢𝖺𝗇 𝖯𝗋𝗈𝗏𝗂𝖽𝖾 𝖬𝗈𝗏𝗂𝖾𝗌, 𝖲𝖾𝗋𝗂𝖾𝗌 𝖠𝗇𝖽 𝖮𝗍𝗁𝖾𝗋 𝖤𝗇𝗍𝖾𝗋𝗍𝖺𝗂𝗇𝗆𝖾𝗇𝗍 𝖲𝗍𝗎𝖿𝖿𝗌. 𝖲𝖾𝖺𝗋𝖼𝗁 𝖣𝗂𝗋𝖾𝖼𝗍𝗅𝗒 𝖧𝖾𝗋𝖾 𝖮𝗋 𝖨𝗇 𝖡𝖾𝗅𝗈𝗐 𝖦𝗋𝗈𝗎𝗉 ↓</b>"""
    
    HELP_TXT = """<b><i>ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴꜱ ᴛᴏ ɢᴇᴛ ᴅᴏᴄᴜᴍᴇɴᴛᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ꜱᴘᴇᴄɪꜰɪᴄ ᴍᴏᴅᴜʟᴇꜱ..</i></b>"""
    
    CODEXBOTS = """<b><i>/upload - sᴇɴᴅ ᴍᴇ ᴘɪᴄᴛᴜʀᴇ ᴏʀ ᴠɪᴅᴇᴏ ᴜɴᴅᴇʀ (5ᴍʙ)

ɴᴏᴛᴇ - ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴡᴏʀᴋ ɪɴ ᴘᴍ</i></b>"""
 
    STATUS_TXT = """<b><u>🗃 ᴅᴀᴛᴀʙᴀsᴇ 1 🗃</u>

» ᴛᴏᴛᴀʟ ᴜsᴇʀs - <code>{}</code>
» ᴛᴏᴛᴀʟ ɢʀᴏᴜᴘs - <code>{}</code>
» ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ - <code>{} / {}</code>

<u>🗳 ᴅᴀᴛᴀʙᴀsᴇ 2 🗳</u>

» ᴛᴏᴛᴀʟ ꜰɪʟᴇs - <code>{}</code>
» ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ - <code>{} / {}</code>

<u>🤖 ʙᴏᴛ ᴅᴇᴛᴀɪʟs 🤖</u>

» ᴜᴘᴛɪᴍᴇ - <code>{}</code>
» ʀᴀᴍ - <code>{}%</code>
» ᴄᴘᴜ - <code>{}%</code></b>"""

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

    FILE_CAPTION = """<b><a href=https://telegram.me/Haxoff>{file_name}</a></b>

<i>ᴘʟᴇᴀsᴇ ꜰᴏʀᴡᴀʀᴅ ᴛʜɪꜱ ꜰɪʟᴇ ᴛᴏ ᴛʜᴇ ꜱᴀᴠᴇᴅ ᴍᴇꜱꜱᴀɢᴇ ᴀɴᴅ ᴄʟᴏꜱᴇ ᴛʜɪꜱ ᴍᴇꜱꜱᴀɢᴇ</i>"""

    RESTART_TXT = """<b>
📅 Dᴀᴛᴇ: <code>{}</code>
⏰ Tɪᴍᴇ: <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ: <code>Asia/Kolkata</code></b>"""

    ALRT_TXT = """❌ 𝗧𝗵𝗮𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗳𝗼𝗿 𝘆𝗼𝘂 𝘀𝗶𝗿 ⛔️"""

    OLD_ALRT_TXT = """𝐘𝐨𝐮 𝐚𝐫𝐞 𝐮𝐬𝐢𝐧𝐠 𝐨𝐧𝐞 𝐨𝐟 𝐦𝐲 𝐨𝐥𝐝 𝐦𝐞𝐬𝐬𝐚𝐠𝐞𝐬, 𝐩𝐥𝐞𝐚𝐬𝐞 𝐬𝐞𝐧𝐝 𝐭𝐡𝐞 𝐫𝐞𝐪𝐮𝐞𝐬𝐭 𝐚𝐠𝐚𝐢𝐧"""

    NO_RESULT_TXT = """🗳 𝗧𝗵𝗶𝘀 𝗠𝗼𝘃𝗶𝗲 𝗶𝘀 𝗻𝗼𝘁 𝘆𝗲𝘁 𝗿𝗲𝗹𝗲𝗮𝘀𝗲𝗱 𝗼𝗿 𝗮𝗱𝗱𝗲𝗱 𝘁𝗼 𝗱𝗮ᴛᴀʙᴀꜱᴇ 🗳"""
    
    I_CUDNT = """🤧 𝗛𝗲𝗹𝗹𝗼 {}

𝗜 𝗰𝗼𝘂𝗹𝗱𝗻'𝘁 𝗳𝗶𝗻𝗱 𝗮ɴʏ ᴍᴏᴠɪᴇ ᴏʀ ꜱᴇʀɪᴇꜱ ɪɴ ᴛʜᴀᴛ ɴᴀᴍᴇ.. 😐"""

    I_CUD_NT = """😑 𝗛𝗲𝗹𝗹𝗼 {}

𝗜 𝗰𝗼𝘂𝗹𝗱𝗻'𝘁 𝗳𝗶𝗻𝗱 ᴀɴʏᴛʜɪɴɢ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ᴛʜᴀᴛ 😞... ᴄʜᴇᴄᴋ ʏ𝗼𝘂ʀ ꜱᴘᴇʟʟɪɴɢ."""
    
    CUDNT_FND = """🤧 𝗛𝗲𝗹𝗹𝗼 {}

𝗜 𝗰𝗼𝘂𝗹𝗱𝗻'𝘁 𝗳𝗶𝗻𝗱 ᴀɴʏᴛʜɪɴɢ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ᴛʜᴀᴛ. 𝗗𝗶𝗱 ʏ𝗼𝘂 𝗺𝗲𝗮𝗻 𝗮ɴʏ 𝗼𝗻𝗲 𝗼ғ ᴛʜ𝗲𝘀𝗲?? 👇"""
    
    FONT_TXT= """<b><i>ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪꜱ ᴍᴏᴅᴇ ᴛᴏ ᴄʜᴀɴɢᴇ ʏᴏᴜʀ ꜰᴏɴᴛꜱ ꜱᴛʏʟᴇ.</i></b>

<code>/font hi how are you</code>"""

    PREMIUM_TEXT = """<b><i><blockquote>ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴꜱ  ♻️</blockquote>

• 𝟷 ᴡᴇᴇᴋ  -  ₹𝟹𝟶
• 𝟷 ᴍᴏɴᴛʜ  -  ₹𝟻𝟶
• 𝟹 ᴍᴏɴᴛʜs  -  ₹𝟷𝟶𝟶
• 𝟼 ᴍᴏɴᴛʜs  -  ₹𝟸𝟶𝟶

•─────•─────────•─────•
<blockquote>ᴘʀᴇᴍɪᴜᴍ ꜰᴇᴀᴛᴜʀᴇꜱ 🎁</blockquote>

○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪꜰʏ
○ ᴅɪʀᴇᴄᴛ ꜰɪʟᴇꜱ   
○ ᴀᴅ-ꜰʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ 
○ ʜɪɢʜ-ꜱᴘᴇᴇᴅ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ                         
○ ᴍᴜʟᴛɪ-ᴘʟᴀʏᴇʀ ꜱᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋꜱ                           
○ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇꜱ, ꜱᴇʀɪᴇꜱ & ᴀɴɪᴍᴇ                                                                         
○ ꜰᴜʟʟ ᴀᴅᴍɪɴ ꜱᴜᴘᴘᴏʀᴛ                              
○ ʀᴇǫᴜᴇꜱᴛ ᴡɪʟʟ ʙᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ɪɴ 𝟷ʜ
•─────•─────────•─────•

✨ ᴜᴘɪ ɪᴅ - <code>TechifyBots@UPI</code>

ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ  /myplan

💢 ᴍᴜsᴛ ꭓᴇɴᴅ ᴄʟɪᴄᴋ ᴛᴏ ꜱᴇɴᴅ ᴛʜᴇ ʀᴇꜱᴘᴏɴꜱᴇ ᴏғ ᴛʜᴇ ᴘʀᴇᴍɪᴜᴍ ᴠᴇʀꜱɪᴏɴ</i></b>"""

    EARN_TEXT = """<b><i><blockquote>ʜᴏᴡ ᴛᴏ ᴇᴀʀɴ ᴍᴏɴᴇʏ ʙʏ ᴛʜɪꜱ ʙᴏᴛ 🤑</blockquote>

›› sᴛᴇᴘ 𝟷: ʏᴏᴜ ᴍᴜsᴛ ʜᴀᴠᴇ ᴀᴛʟᴇᴀꜱᴛ ᴏɴᴇ ɢʀᴏᴜᴘ ᴡɪᴛʜ ᴍɪɴɪᴍᴜᴍ 𝟹𝟶𝟶 ᴍᴇᴍʙᴇʀꜱ.

›› sᴛᴇᴘ 𝟸: ᴍᴀᴋᴇ <a href=https://telegram.me/{}</a> ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ.

›› sᴛᴇᴘ 𝟹: ᴍᴀᴋᴇ ᴀᴄᴄᴏᴜɴᴛ ᴏɴ <a href='https://tnshort.net/ref/devilofficial'>ᴛɴʟɪɴᴋ</a> ᴏʀ <a href='https://onepagelink.in/ref/Nobita'>ᴏɴᴇᴘᴀɢᴇʟɪɴᴋ</a>. [ ʏᴏᴜ ᴄᴀɴ ᴀʟꭓsᴏ ᴜsᴇ ᴏᴛʜᴇʀ ᴛʜᴇʀ ᴅᴏᴍᴀɪɴ ɴᴀᴍᴇ ]

›› sᴛᴇᴘ 𝟺: ɴᴏᴡ ꜱᴇᴛ ʏᴏᴜʀ ꜱʜᴏʀᴛɴᴇʀ, ᴛᴜᴛᴏʀɪᴀʟ, ꜰꜱᴜʙ ᴀɴᴅ ʟᴏɢ ᴄʜᴀɴɴᴇʟ.

›› sᴛᴇᴘ 𝟻: ꜰᴏʟʟᴏᴡ ᴛʜᴇsᴇ <a href='https://github.com/TechifyBots/Auto-Filter-Bot/blob/main/README.md'>ɪɴꜱᴛʀᴜᴄᴛɪᴏɴꜱ</a>.

ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴠᴀʟᴜᴇꜱ ʙʏ /ginfo ᴄᴏᴍᴍᴀɴᴅ.

💯 ɴᴏᴛᴇ - ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ꜰʀᴇᴇ ᴛᴏ ᴀʟʟ, ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪꜱ ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘꜱ ᴀɴᴅ ᴇᴀʀɴ ᴍᴏɴᴇʏ.</i></b>"""

    # Updated verification prompts and complete texts for the new three-tier cycle.
    # VERIFICATION_TEXT: prompts the user that they must complete Verification 1 of 3.
    VERIFICATION_TEXT = """<b>ʜʏ {} {},

ʏᴏᴜ ʏᴏᴜʀ ɪɴɪᴛɪᴀʟ (1/3) ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ʜᴀꜱ ᴇxᴘɪʀᴇᴅ.
ᴘʟᴇᴀꜱᴇ ᴛᴀᴋᴇ ᴛʜᴇ ɴᴇᴡ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ᴘʀᴏᴄᴇꜱꜱ (2/3).

ᴄʜᴇᴄᴋ /plan ᴛᴏ ᴍᴏʀᴇ ᴅᴇᴛᴀɪʟꜱ.</b>"""

    # SECOND_VERIFICATION_TEXT: prompt when requiring the second tier.
    SECOND_VERIFICATION_TEXT = """<b>ʜʏ {} {},

ʏᴏᴜ ʜᴀᴠᴇ ɴᴏᴛ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛʜᴇ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ.
ᴘʟᴇᴀꜱᴇ ᴛᴀᴋᴇ ᴛʜᴇ 2/3 ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ᴘʀᴏᴄᴇꜱꜱ.

ᴄʜᴇᴄᴋ /plan ᴛᴏ ᴍᴏʀᴇ ᴅᴇᴛᴀɪʟꜱ.</b>"""

    # THIRDT_VERIFICATION_TEXT: prompt when requiring the third tier.
    THIRDT_VERIFICATION_TEXT = """<b>ʜʏ {} {},

ʏᴏᴜ ʜᴀᴠᴇ ɴᴏᴛ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛʜᴇ 2/3 ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ.
ᴘʟᴇᴀꜱᴇ ᴛᴀᴋᴇ ᴛʜᴇ 3/3 ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ᴘʀᴏᴄᴇꜱꜱ.

ᴄʜᴇᴄᴋ /plan ᴛᴏ ᴍᴏʀᴇ ᴅᴇᴛᴀɪʟꜱ.</b>"""

    # Complete texts after verification is successful.
    VERIFY_COMPLETE_TEXT = """<b>ʜʏ {},

ʏᴏᴜ ʜᴀᴠᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛʜᴇ 1/3 ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ!
ᴛʜɪꜱ ɪᴠᴇ ɢʀᴀɴᴛᴇᴅ ʏᴏᴜ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇꜱꜱ ᴛɪʟʟ ʏᴏᴜ ʀᴇᴍᴀɪɴ ᴠᴇʀɪꜰɪᴇᴅ (ғᴏʀ 1/3 ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ᴘᴇʀɪᴏᴅ).</b>"""

    SECOND_VERIFY_COMPLETE_TEXT = """<b>ʜʏ {},

ʏᴏᴜ ʜᴀᴠᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛʜᴇ 2/3 ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ!
ᴛʜɪꜱ ɪᴠᴇ ɢʀᴀɴᴛᴇᴅ ʏᴏᴜ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇꜱꜱ ᴛɪʟʟ ʏᴏᴜ ʀᴇᴍᴀɪɴ ᴠᴇʀɪꜰɪᴇᴅ (ғᴏʀ 2/3 ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ᴘᴇʀɪᴏᴅ).</b>"""

    THIRDT_VERIFY_COMPLETE_TEXT = """<b>ʜʏ {},

ʏᴏᴜ ʜᴀᴠᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛʜᴇ 3/3 ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ!
ᴛʜɪꜱ ɪᴠᴇ ʀᴇꜱᴛ ᴛʜᴇ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ᴄʏᴄʟᴇ, ɴᴏᴡ ʏᴏᴜ ᴡɪʟʟ ʀᴇᴍᴀɪɴ ᴀᴄᴄᴇꜱꜱᴇᴅ ᴜɴʟɪᴍɪᴛᴇᴅʟʏ ᴜɴᴛɪʟ ᴛʜᴇ ᴛɪᴍᴇ ʙᴇɪɴɢ ᴇxᴘɪʀᴇᴅ.</b>"""

    VERIFIED_LOG_TEXT = """<b><u>☄ ᴜsᴇʀ ᴠᴇʀɪꜰɪᴇᴅ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ☄</u>

⚡️ ɴᴀᴍᴇ: {} [ <code>{}</code> ]
📆 ᴅᴀᴛᴇ: <code>{}</code>
➔ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ᴛɪᴇʀ: #verification_{}_completed</b>"""

    CUSTOM_TEXT = """<b><i>😊 <u>Your Group Commands</u> 😊
    
/shortlink - To set the shortener for 1st verification  
/shortlink2 - To set the shortener for 2nd verification  
/shortlink3 - To set the shortener for 3rd verification  
/time2 - To set the 2nd verification time  
/time3 - To set the 3rd verification time  
/log - To set the log channel for user data  
/tutorial - To set the 1st verification tutorial link  
/tutorial2 - To set the 2nd verification tutorial link  
/tutorial3 - To set the 3rd verification tutorial link  
/caption - To set custom file caption  
/template - To set custom IMDB template  
/fsub - To set your force subscribe channel  
/nofsub - To remove force subscribe channel  
/ginfo - To check your group details</i></b>

😘 If you do all this then your group will be very cool..."""

    FSUB_TXT = """{},

<i><b>🙁 First, join our channel; then you will get movies, otherwise you will not get them.
Click join now below.</b></i>"""

    DONATE_TXT = """<blockquote>❤️‍🔥 Thank You for showing interest in Donation</blockquote>

<b><i>💞 If you like our bot, feel free to donate any amount: ₹10, ₹20, ₹50, ₹100, etc.</i></b>

❣️ Donations are truly appreciated as they help in bot development

💖 UPI ID: <code>TechifyBots@UPI</code>
"""