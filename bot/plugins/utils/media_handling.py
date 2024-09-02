#!/usr/bin/env python3
# This is bot coded by Abhijith N T and used for educational purposes only
# https://github.com/abhint
# Copyright ABHIJITH N T
# Thank you https://github.com/pyrogram/pyrogram


from ...filetocloud import CloudBot, filters
from bot import LOGGER
from hurry.filesize import size
from ...helpers import server_select

# from ..use import VIDEO, DOCUMENT, AUDIO

BOT_USE = True
AUTH_USER = [1039959953,5443081541]

if BOT_USE:
    VIDEO = filters.video & filters.user(AUTH_USER)
    DOCUMENT = filters.document & filters.user(AUTH_USER)
    AUDIO = filters.audio & filters.user(AUTH_USER)
    LINK = filters.text & filters.user(AUTH_USER)
    PHOTO = filters.photo & filters.user(AUTH_USER)
    
else:
    VIDEO = filters.video
    DOCUMENT = filters.document
    AUDIO = filters.audio
    LINK = filters.text
    PHOTO = filters.photo

logger = LOGGER(__name__)


@CloudBot.on_message(VIDEO)
async def user_video(client, bot):
    logger.info(f"{bot.chat.id} - {bot.video.file_name}")
    file_name = bot.video.file_name
    await client.send_message(
        chat_id=bot.chat.id,
        text=(
            f"File Name: `{file_name}`"
            f"\nFile Size: `{size(bot.video.file_size)}`"
        ),
        reply_markup=server_select(bot.video.file_size),
        reply_to_message_id=bot.id
    )



@CloudBot.on_message(PHOTO)
async def user_photo(client, bot):
    logger.info(f"{bot.chat.id} - {bot.photo.file_id}")
    file_name = bot.photo.file_id
    await client.send_message(
        chat_id=bot.chat.id,
        text=(
            f"File Name: `{file_name}`"
            f"\nFile Size: `{size(bot.photo.file_size)}`" ),
        reply_markup=server_select(bot.photo.file_size,Photo=True),
        reply_to_message_id=bot.id
    )




@CloudBot.on_message(DOCUMENT)
async def user_document(client, bot):
    logger.info(f"{bot.chat.id} - {bot.document.file_name}")
    file_name = bot.document.file_name
    file_size = size(bot.document.file_size)
    await client.send_message(
        chat_id=bot.chat.id,
        text=(
            f"File Name: `{file_name}`"
            f"\nFile Size: `{file_size}`"
        ),
        reply_markup=server_select(bot.document.file_size),
        reply_to_message_id=bot.id
    )


@CloudBot.on_message(LINK)
async def user_link(client, bot):
    if bot.text.startswith("https://") or bot.text.startswith("http://"):
        logger.info(f"{bot.chat.id} - {bot.text}")
        await client.send_message(
        chat_id=bot.chat.id,
        text=(
            f"URL: `{bot.text}`"
        ),
        reply_markup=server_select(0),
        reply_to_message_id=bot.id
    )




@CloudBot.on_message(AUDIO)
async def user_audio(client, bot):
    logger.info(f"{bot.chat.id} - {bot.audio.file_name}")
    file_name = bot.audio.file_name
    file_size = size(bot.audio.file_size)
    await client.send_message(
        chat_id=bot.chat.id,
        text=(
            f"File Name: <code>`{file_name}`</code>"
            f"\nFile Size: <code>{file_size}</code>"
        ),
        reply_markup=server_select(bot.audio.file_size),
        reply_to_message_id=bot.id
    )
