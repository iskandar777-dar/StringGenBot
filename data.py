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
Selamat datang {}
Bot ini Bekerja Untuk Mendapatkan String Session Via Bot.
By @kenapatagdar
    """
