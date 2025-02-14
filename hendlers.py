from aiogram import F
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile, CallbackQuery

from keyboard import *
from text import *
from callbacks import *
from bot import dp


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(text=f"{message.from_user.first_name}, " + text_inline, reply_markup=builder.as_markup())
    await message.answer(text=f"{message.from_user.first_name}, " + text_reply, reply_markup=keyboard)


@dp.message()
async def cmd_replay(message: Message):
    text = message.text
    if text == but1:
        await message.answer(f"{message.from_user.first_name}, " + txt)
    if text == but2:
        await message.answer_photo(photo=FSInputFile('16.jpg'), caption=ph)
    if text == but3:
        await message.answer_video(video=FSInputFile('17.mp4'), caption=vid)
    if text == but4:
        await message.answer_document(document=FSInputFile('18.pdf'), caption=pdf)


@dp.callback_query(F.data)
async def cmd_inline(callback: CallbackQuery):
    cbk = callback.data
    if cbk == cal1:
        await callback.message.answer(text=f"{callback.from_user.first_name}, " + cal_txt)
    if cbk == cal2:
        await callback.message.answer_photo(photo=FSInputFile('16.jpg'), caption=cal_ph)
    if cbk == cal3:
        await callback.message.answer_video(video=FSInputFile('17.mp4'), caption=cal_vid)
    if cbk == cal4:
        await callback.message.answer_document(document=FSInputFile('18.pdf'), caption=cal_pdf)
