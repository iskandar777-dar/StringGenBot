from pyrogram.types import InlineKeyboardButton

class Data:
    generate_single_button = [InlineKeyboardButton("🙄 ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ 🙄", callback_data="generate")]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton(" sᴜᴩᴩᴏʀᴛ ", url="https://t.me/somedsupport"),
         InlineKeyboardButton(" ᴅᴇᴠᴇʟᴏᴩᴇʀ ", url="https://t.me/kenapatagdar"),
        ],
    ]
    
START = """
Halo {},
Selamat datang {}
Bot ini Bekerja Untuk Mendapatkan String Session Via Bot.
By @kenapatagdar

**About This Bot** 
Pyrogram dan telethon string session by @somedstringbot
Group Support : [support](https://t.me/kenapatagdar)
Framework : [Pyrogram](docs.pyrogram.org)
Language : [Python](www.python.org)
Developer : @kenapatagdar
    """
