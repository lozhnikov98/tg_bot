from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types
from text import *
from callbacks import *

kb = [
    [
        types.KeyboardButton(text=but1),
        types.KeyboardButton(text=but2),
        types.KeyboardButton(text=but3),
        types.KeyboardButton(text=but4),
        types.KeyboardButton(text="/start"), #добавил /start что не писать каждый раз
    ],
]
keyboard = types.ReplyKeyboardMarkup(
    keyboard=kb,
    resize_keyboard=True,
    input_field_placeholder="Выберите действие"
)

builder = InlineKeyboardBuilder()
builder.button(text=cal1, callback_data=cal1)
builder.button(text=cal2, callback_data=cal2)
builder.button(text=cal3, callback_data=cal3)
builder.button(text=cal4, callback_data=cal4)
