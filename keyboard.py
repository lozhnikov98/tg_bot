from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types


kb = [
    [
        types.KeyboardButton(text="Отправь текст"),
        types.KeyboardButton(text="Отправь фото"),
        types.KeyboardButton(text="Отправь видео"),
        types.KeyboardButton(text="Отправь файл")
    ],
]
keyboard = types.ReplyKeyboardMarkup(
    keyboard=kb,
    resize_keyboard=True,
    input_field_placeholder="Выберите действие"
)

builder = InlineKeyboardBuilder()
builder.button(text='Text', callback_data='Text')
builder.button(text='Photo', callback_data='Photo')
builder.button(text='Video', callback_data='Video')
builder.button(text='PDF', callback_data='PDF')
