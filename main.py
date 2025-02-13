import asyncio
import os

from config import TOKEN

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.filters import CommandStart

from keyboard import *



bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(text=f"Привет, {message.from_user.first_name}! Выбери :", reply_markup=builder.as_markup())
    await message.answer(f"Привет, {message.from_user.first_name}! Выбери действие:", reply_markup=keyboard)


@dp.message(F.text.lower().contains('отправь фото'))
async def cmd_start(message: Message):
    await message.answer_photo(photo=FSInputFile('16.jpg', filename='Фото'), caption='Это фото!')


@dp.message(F.text.lower().contains('отправь видео'))
async def cmd_start(message: Message):
    await message.answer_video(video=FSInputFile('17.mp4', filename='Видео'), caption='Это Видео!')


@dp.message(F.text.lower().contains('отправь файл'))
async def cmd_start(message: Message):
    await message.answer_document(document=FSInputFile('18.pdf', filename='PDF'), caption='Это файл!')


@dp.message(F.text.lower().contains('отправь текст'))
async def cmd_start(message: Message):
    await message.answer(text=f"Привет, {message.from_user.first_name}! Это текст!")


@dp.callback_query(F.data == 'PDF')
async def cmd_start(callback: CallbackQuery):
    await callback.message.answer_document(document=FSInputFile('18.pdf', filename='PDF'), caption='Это файл!')


@dp.callback_query(F.data == 'Photo')
async def cmd_start(callback: CallbackQuery):
    await callback.message.answer_photo(photo=FSInputFile('16.jpg', filename='Фото'), caption='Это фото!')


@dp.callback_query(F.data == 'Text')
async def cmd_start(message: Message):
    await message.answer(text=f"Привет, {message.from_user.first_name}! Это текст!")


@dp.callback_query(F.data == 'Video')
async def cmd_start(callback: CallbackQuery):
    await callback.message.answer_video(video=FSInputFile('17.mp4', filename='Видео'), caption='Это Видео!')


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
