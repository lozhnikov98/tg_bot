from aiogram import F
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile, CallbackQuery

from keyboard import *
from text import *
from callbacks import *
from bot import dp
import json


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(text=f"{message.from_user.first_name}, " + text_inline, reply_markup=keyboard_inline)
    await message.answer(text=f"{message.from_user.first_name}, " + text_reply, reply_markup=keyboard_reply)


# @dp.message()
# async def cmd_replay(message: Message):
#     text = message.text
#     if text == reply_button_text:
#         await message.answer(f"{message.from_user.first_name}, " + reply_text)
#     if text == reply_button_photo:
#         await message.answer_photo(photo=FSInputFile('media/16.jpg'))
#     if text == reply_button_video:
#         await message.answer_video(video=FSInputFile('media/17.mp4'), caption=reply_video)
#     if text == reply_button_pdf:
#         await message.answer_document(document=FSInputFile('media/18.pdf'), caption=reply_pdf)


@dp.callback_query(F.data)
async def cmd_inline(callback: CallbackQuery):
    cbk = callback.data
    if cbk == cal1:
        await callback.message.answer(text=f"{callback.from_user.first_name}, " + inline_text)
    if cbk == cal2:
        with open("json/foto_id.json", "r") as read_file:
            data = json.load(read_file)
        photo_id = data['id']
        await callback.message.answer_photo(photo=photo_id, caption=inline_photo)
    if cbk == cal3:
        with open("json/video_id.json", "r") as read_file:
            data = json.load(read_file)
        video_id = data['id']
        await callback.message.answer_video(video=video_id, caption=inline_video)
    if cbk == cal4:
        with open("json/documents_id.json", "r") as read_file:
            data = json.load(read_file)
        document_id = data['id']
        await callback.message.answer_document(document=document_id, caption=inline_pdf)


any_media_filter = F.photo | F.video | F.document


@dp.message(any_media_filter, ~F.caption)
async def cmd_media(message: types.Message):
    if message.photo:
        add_foto_to_json(message.photo[-1].file_id)
        await message.reply(text='Я считал file_id этой фотографии')
    elif message.video:
        add_video_to_json(message.video.file_id)
        await message.reply(text='Я считал file_id этого видео')
    elif message.document:
        add_document_to_json(message.document.file_id)
        await message.reply(text='Я считал file_id этого документа')


def add_foto_to_json(file_id):
    data = {"id": file_id}

    with open('json/foto_id.json', 'w') as file:
        json.dump(data, file)


def add_video_to_json(file_id):
    data = {"id": file_id}

    with open('json/video_id.json', 'w') as file:
        json.dump(data, file)


def add_document_to_json(file_id):
    data = {"id": file_id}

    with open('json/documents_id.json', 'w') as file:
        json.dump(data, file)
