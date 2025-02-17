from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types
from callbacks import *
from name_buttons import *

reply_kb = [
    [
        types.KeyboardButton(text=reply_button_text),
        types.KeyboardButton(text=reply_button_photo),
    ],
    [
        types.KeyboardButton(text=reply_button_video),
        types.KeyboardButton(text=reply_button_pdf),
    ],
    [
        types.KeyboardButton(text="/start"), #добавил /start что не писать каждый раз
    ],
]

keyboard_reply = types.ReplyKeyboardMarkup(
    keyboard=reply_kb,
    resize_keyboard=True,
    input_field_placeholder="Выберите действие"
)


inline_kb = [
    [InlineKeyboardButton(text=inline_button_text, callback_data=cal1), InlineKeyboardButton(text=inline_button_photo, callback_data=cal2)],
    [InlineKeyboardButton(text=inline_button_video, callback_data=cal3), InlineKeyboardButton(text=inline_button_pdf, callback_data=cal4)],
]
keyboard_inline = InlineKeyboardMarkup(inline_keyboard=inline_kb)
