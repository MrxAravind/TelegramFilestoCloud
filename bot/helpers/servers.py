from bot import LOGGER
from ..filetocloud import CloudBot
from .upload import server_upload,switch_upload
from ..helpers import download_media,download_link
from .shortener import shorten_link
from pyrogram.types import CallbackQuery
from hurry.filesize import size
import pixeldrain_reloaded as pixeldrain
from telegraph import Telegraph, exceptions
from config import PIXELDRAIN_APIKEY
import time,os


logger = LOGGER(__name__)

link = ""


async def upload_handler(client: CloudBot, message: CallbackQuery, callback_data: str):
    global link
    pi = None
    if not callback_data.startswith('mirror'):
            if message.message.reply_to_message.video:
                file_name = message.message.reply_to_message.video.file_name
                file_ize = size(message.message.reply_to_message.video.file_size)
                fize = message.message.reply_to_message.video.file_size
            elif message.message.reply_to_message.document:
                file_name = message.message.reply_to_message.document.file_name
                file_ize = size(message.message.reply_to_message.document.file_size)
                fize = message.message.reply_to_message.document.file_size
            elif message.message.reply_to_message.audio:
                file_name = message.message.reply_to_message.audio.file_name
                file_ize = size(message.message.reply_to_message.audio.file_size)
                fize = message.message.reply_to_message.audio.file_size
            elif message.message.reply_to_message.photo:
                file_name = str(message.message.reply_to_message.photo.file_id) + "png"
                file_ize = size(message.message.reply_to_message.photo.file_size)
                fize = message.message.reply_to_message.photo.file_size
                pi = True

        
            try:
                 file_path = await download_media(client, message)
                 if pi:
                    file_name = file_path.split('/')[-1]
                 status = await client.edit_message_text(
                     chat_id=message.from_user.id,
                     message_id=message.message.id,
                    text=f"Started Downloading.... ",
                    )
            except Exception as e:
                 logger.error(f"{e}")
                 status = await client.edit_message_text(
                     chat_id=message.from_user.id,
                     message_id=message.message.id,
                     text=f"**File downloading error:** `{e}`",
                     )
                 return
        
    else:
        url = message.message.reply_to_message.text
        status = await client.edit_message_text(
                     chat_id=message.from_user.id,
                     message_id=message.message.id,
                     text=f"Started Downloading.... ",
                     )
        file_name,file_path,fize = await download_link(client,status,url,time.time())
    try:
                status = await client.edit_message_text(
                    chat_id=message.message.chat.id,
                    text="Started uploading...",
                    message_id=message.message.id
                )
                start =  time.time()
                if callback_data.endswith('bashupload'):
                    url = f'http://bashupload.com/'
                    response = await server_upload(file_path=file_path, url=url,message=status,size=fize,start=start)
                    link = await bashupload(response)
                elif callback_data.endswith('fileio'):
                    url = 'https://file.io/'
                    response = await server_upload(file_path=file_path,url=url,message=status,size=fize,start=start)
                    link = await file_io(response)
                elif callback_data.endswith('gofile'):
                    url = 'https://store1.gofile.io/contents/uploadfile'
                    response = await server_upload(file_path=file_path, url=url,message=status,size=fize,start=start)
                    link = await gofile_io(response)
                elif callback_data.endswith('pixeldrain'):
                    response = pixeldrain.Sync.upload_file(file_path,returns="dict", filename=file_name, api_key=PIXELDRAIN_APIKEY)
                    link = await pixeldrain_com(response)
                elif callback_data.endswith('flashbang'):
                    url = f'https://w.flashbang.sh/t/{file_path.split("/")[-1][-10:-1]}'
                    response = await server_upload(file_path=file_path, url=url,message=status,size=fize,start=start,put=True)
                    link = await flashbang(response)
                elif callback_data.endswith('switch'):
                    response = await switch_upload(file_path=file_path,size=fize,message=status,start=start)
                    link = response.media_link
                    link = f"{shorten_link(link)}\nFull_URl: {link}"
                elif callback_data.endswith('telegraph'):
                        try:
                          telegraph = Telegraph()
                          telegraph.create_account(short_name='SpidyTelegramFiletoCloudBot')
                          with open(file_path, 'rb') as f:
                               response = telegraph.upload_file(f)[0]
                               link = await tgraph(response)
                        except exceptions.TelegraphException as e:
                            print(f"TelegraphException: {e}")
                        except Exception as e:
                            print(f"Error: {e}")
    



                await client.send_message(
                    chat_id=message.message.chat.id,
                    text=(f"File Name: `{file_name}`"
                        f"\nFile Size: `{size(fize)}`"
                        f'\nURL: {link}'),
                    reply_to_message_id=message.message.reply_to_message.id
                )
                await status.delete()
                os.remove(file_path)
    except Exception as e:
                logger.error(f'{e}')
                await client.edit_message_text(
                    chat_id=message.from_user.id,
                    message_id=message.message.id,
                    text=f"**File uploading error:** `{e}`",
                )
                return





async def gofile_io(response):
    return response['data']["downloadPage"]

async def pixeldrain_com(response):
    return f"https://pixeldrain.com/api/file/{response['id']}"

async def file_io(response):
    return response['link']

async def bashupload(response):
    for i in response.split():
        if i.startswith("http://") or i.startswith("https://"):
              return i
    
async def switchlink(response):
    return response["media_link"]

async def flashbang(response):
    return f"https://flashbang.sh/f/{response}"

async def tgraph(response):
    return f"https://graph.org{response["src"]}"
