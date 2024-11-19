#!/usr/bin/env python3
# This is bot coded by Abhijith N T and used for educational purposes only
# https://github.com/abhint
# Copyright ABHIJITH N T
# Thank you https://github.com/pyrogram/pyrogram

from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


def server_select(file_size: int,Photo=None):
    prefix = ""
    if file_size == 0:
        prefix = "mirror"
    upload_selection = [
        [
            InlineKeyboardButton(
                "bashupload.com",
                callback_data=f"{prefix}bashupload"
            )
        ],
        [
            InlineKeyboardButton(
                "Gofile.io",
                callback_data=f"{prefix}gofile"
            )
        ],
        [
            InlineKeyboardButton(
                "PixelDrain",
                callback_data=f"{prefix}pixeldrain"
            )
        ],
    ]
    if file_size < 2e+8:
        # 2e+8 is 200000000.0
        upload_selection.append([
            InlineKeyboardButton(
                "File.io",
                callback_data=f"{prefix}fileio"
            )
        ])
    if Flase:
                upload_selection.append([
                    InlineKeyboardButton(
                        "Telegraph",
                        callback_data=f"{prefix}telegraph"
                    )
                ])
    if False:
                upload_selection.append([
            InlineKeyboardButton(
                "FlashBang",
                callback_data=f"{prefix}flashbang"
            )
        ])
    if False:
                upload_selection.append([
            InlineKeyboardButton(
                "Switch",
                callback_data=f"{prefix}switch"
            )
        ])
    
    return InlineKeyboardMarkup(upload_selection)
