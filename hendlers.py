from aiogram import F
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile, CallbackQuery

from keyboard import *
from text import *
from callbacks import *
from bot import dp


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(text=f"{message.from_user.first_name}, " + text_inline, reply_markup=keyboard_inline)
    await message.answer(text=f"{message.from_user.first_name}, " + text_reply, reply_markup=keyboard_reply)


@dp.message()
async def cmd_replay(message: Message):
    text = message.text
    if text == reply_button_text:
        await message.answer(f"{message.from_user.first_name}, " + reply_text)
    if text == reply_button_photo:
        await message.answer_photo(photo=FSInputFile('media/16.jpg'), caption=reply_photo)
    if text == reply_button_video:
        await message.answer_video(video=FSInputFile('media/17.mp4'), caption=reply_video)
    if text == reply_button_pdf:
        await message.answer_document(document=FSInputFile('media/18.pdf'), caption=reply_pdf)


@dp.callback_query(F.data)
async def cmd_inline(callback: CallbackQuery):
    cbk = callback.data
    if cbk == cal1:
        await callback.message.answer(text=f"{callback.from_user.first_name}, " + inline_text)
    if cbk == cal2:
        await callback.message.answer_photo(photo=FSInputFile('media/16.jpg'), caption=inline_photo)
    if cbk == cal3:
        await callback.message.answer_video(video=FSInputFile('media/17.mp4'), caption=inline_video)
    if cbk == cal4:
        await callback.message.answer_document(document=FSInputFile('media/18.pdf'), caption=inline_pdf)
