from bot import LOGGER
import os
import aiohttp
from aiohttp import client_exceptions
import asyncio
from .progress import progress_for_pyrogram
from swibots import BotApp
from config import TOKEN,COMMUNITY_ID,GROUP_ID

logger = LOGGER(__name__)

client_exceptions = (
    aiohttp.ClientResponseError,
    aiohttp.ClientConnectionError,
    aiohttp.ClientPayloadError,
)

#Switch
bot = BotApp(TOKEN)


async def progress_callback(bytes_sent, total_bytes,message,start):
    await progress_for_pyrogram(bytes_sent,total_bytes,message,start)

async def upload_progress_handler(progress,total,message,start):
    await progress_for_pyrogram(progress.current,total,message,start)


async def server_upload(url: str,file_path: str,message,size,start,put=None):
    if not os.path.isfile(file_path):
        raise Exception("File path not found")
    async def progress_reader(file, chunk_size=8192):
        total_size = os.path.getsize(file.name)
        bytes_read = 0
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            bytes_read += len(chunk)
            if progress_callback:
                await progress_callback(bytes_read,total_size,message,start)
            yield chunk

    try:
        async with aiohttp.ClientSession() as session:
            with open(file_path, 'rb') as file:
                data = aiohttp.FormData()
                data.add_field('file', progress_reader(file), filename=os.path.basename(file_path))
                if put:
                    response = await session.put(url, data=data)
                else:
                    response = await session.post(url, data=data)
                if response.headers.get('Content-Type', '').startswith('application/json'):
                    return await response.json()
                return await response.text()
    except client_exceptions.ClientError as e:
        raise Exception(e)



async def switch_upload(file_path,size,message,start):
    if os.path.isfile(file_path) is False:
        raise Exception("File path not found")
    try:
        res = await bot.send_media(
             message=f"{os.path.basename(file_path)}",
             community_id=COMMUNITY_ID,
             group_id=GROUP_ID,
             document=file_path,
             description=file_path,
             progress= upload_progress_handler,
             progress_args=(size,message,start))
        return res
    except Exception as e:
        raise Exception(e)
    
