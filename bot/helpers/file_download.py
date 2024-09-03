import logging 
from pyrogram.types import CallbackQuery
from pyrogram.errors import RPCError
from bot import LOGGER
from ..filetocloud import CloudBot
from .progress import progress_for_pyrogram
import  time
import os
import aiohttp
from aiohttp import client_exceptions
import re
import urllib.parse
import asyncio


# Set up the basic configuration for the logger
logging.basicConfig(level=logging.INFO)

# Create a logger object
logger = logging.getLogger(__name__)



async def progress_callback(done, total,status,start):
     await progress_for_pyrogram(done,total,status,start)
     

async def download_media(client: CloudBot, message: CallbackQuery, ) -> str:
    user_message = await client.edit_message_text(
        chat_id=message.from_user.id,
        message_id=message.message.id,
        text="Processing Your Request...",
    )
    try:
        media_id = message.message.reply_to_message
        user_message = await user_message.edit_text("Downloading Started...")
        start = time.time()
        download_file_path = await client.download_media(media_id,progress=progress_for_pyrogram,progress_args=(user_message,start))
        return download_file_path
    except RPCError as e:
        logger.error(e)
        raise Exception(e)



async def download_link(client: CloudBot, message: CallbackQuery,url: str,start):
    try:
        user_message = await message.edit_text(
             text="Processing Your Request..."
             )
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                dest = os.getcwd()
                response.raise_for_status()
                filename = None
                cd = response.headers.get('Content-Disposition')
                if cd:
                    fname = re.findall('filename="(.+)"', cd)
                    if fname:
                        filename = fname[0]
                if not filename:
                    filename = os.path.basename(urllib.parse.urlparse(url).path)
                dest_path = os.path.join(dest, filename)
                total_size = int(response.headers.get('Content-Length', 0))
                bytes_downloaded = 0
                with open(dest_path, 'wb') as dest_file:
                    async for chunk in response.content.iter_chunked(8192):
                        dest_file.write(chunk)
                        bytes_downloaded += len(chunk)
                        if progress_callback:
                            await progress_callback(bytes_downloaded,total_size,message,start)

                return filename,dest_path,total_size
    except Exception as e:
        logger.error(e)
        raise Exception(e)

