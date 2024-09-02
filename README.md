## What is about this bot ?

#### This bot uploads telegram files to a third-party server.
#### Usage: Send any file or bot. Then select the third-party server you want to upload to.

### Supported clouds
- [x] bashupload.com
- [x] file.io
- [x] gofile.io
- [x] PixelDrain

### Installation
#### Clone

```sh
git clone https://github.com/MrXAravind/TelegramFiletoCloud.git

cd TelegramFiletoCloud

```

#### Install Requirements

```sh
pip3 install -U -r requirements.txt
```
#### Edit Sample_config.py and replace it with your bot details like this

```python
class Config:
    BOT_USE = False                        # True is private use
    BOT_TOKEN = ''                         # from @botfather
    APP_ID = 1234567                       # from https://my.telegram.org/apps
    API_HASH = ''                          # from https://my.telegram.org/apps
    AUTH_USERS = []                        # Private users id
```

#### Run this bot
```sh
python3 -m bot
```

#### PIXELDRAIN Needs Api_Key,So Add Ur Key With /api Command
