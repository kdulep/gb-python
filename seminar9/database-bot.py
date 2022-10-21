# Создайте программу для игры в ""Крестики-нолики"".

"""
This is a simple example of usage of CallbackData factory
For more comprehensive example see callback_data_factory.py
"""
import csv
import fileio
import pandas as pd
import numpy as np
import dataframe_image as dfi

import logging
import typing

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils.callback_data import CallbackData
from aiogram.utils.exceptions import MessageNotModified

logging.basicConfig(level=logging.INFO)

API_TOKEN = '!!!!!!!!!!!!!!!!!!TOKEN_INSERT_HERE!!!!!!!!!!!!!!!!!!!!'

bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

vote_cb = CallbackData('vote', 'action')  # vote:<action>

turn = {}
count = {}
board = {}

message = {'0': ["View", "view_data"],
           '1': ["Add", "add_data"],
           '2': ["Del", "del_data"],
           '3': ["Edit", "edit_data"]}

# {str(list1): '' for list1 in range(1, 10)}


def get_keyboard2(display_text):
    markup = types.ForceReply()
    markup.input_field_placeholder = display_text
    return markup


def get_keyboard():
    markup1 = types.InlineKeyboardMarkup(row_width=3)
    markup1.row(
        types.InlineKeyboardButton(
            message['0'][0], callback_data=vote_cb.new(action=message['0'][1])),
        types.InlineKeyboardButton(
            message['1'][0], callback_data=vote_cb.new(action=message['1'][1])),
        types.InlineKeyboardButton(
            message['2'][0], callback_data=vote_cb.new(action=message['2'][1])),
        types.InlineKeyboardButton(
            message['3'][0], callback_data=vote_cb.new(action=message['3'][1])),

    )
    return markup1


@ dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    # get value if key exists else set to 0
    await message.reply(f'Что делаем?', reply_markup=get_keyboard())

# if the text starts with any string from the list


@ dp.message_handler(commands=['add'])
async def cmd_add(message: types.Message):
    # get value if key exists else set to 0
    data=[]
    bookreader = csv.reader([message.text], delimiter=' ', quotechar='"')
    
    for row in bookreader:
        data.append([row[0], row[1], row[2], row[3], row[4], row[5]])

    del data[0][0]
    #del data[0][0]
    print(data[0])
    fileio.write_data(data[0])
    await message.reply(f'Adding {data[0]}', reply_markup=get_keyboard())


@ dp.message_handler(commands=['del'])
async def cmd_del(message: types.Message):
    # get value if key exists else set to 0
    data=[]
    bookreader = csv.reader([message.text], delimiter=' ', quotechar='"')
    
    for row in bookreader:
        data.append([row[0], row[1]])

    #del data[0][0]
    fileio.delete_data(data[0][1])
    await message.reply(f'Deleting {data[0][1]}', reply_markup=get_keyboard())


@ dp.message_handler(commands=['edit'])
async def cmd_edit(message: types.Message):
    # get value if key exists else set to 0
    data=[]
    bookreader = csv.reader([message.text], delimiter=' ', quotechar='"')
    
    for row in bookreader:
        data.append([row[0], row[1], row[2], row[3], row[4], row[5], row[6]])

    del data[0][0]
    print(data[0])
    fileio.update_data(data[0])
    await message.reply(f'Editing {data[0]}', reply_markup=get_keyboard())


# @dp.message_handler(text_startswith=['add', 'del'])
# async def text_startswith_handler(message: types.Message):
#     await message.answer("The message text starts with any of prefixes")


@ dp.callback_query_handler(vote_cb.filter(action=[message['0'][1], message['1'][1], message['2'][1], message['3'][1]]))
async def callback_vote_action(query: types.CallbackQuery, callback_data: typing.Dict[str, str]):
    # callback_data contains all info from callback data
    logging.info('Got this callback data: %r', callback_data)
    await query.answer()  # don't forget to answer callback query as soon as possible
    callback_data_action = callback_data['action']

    if callback_data_action == 'view_data':
        df = fileio.pd_read_data()
        # df_styled = df.style.background_gradient()
        dfi.export(df, "table.png")
        with open('table.png', 'rb') as photo:
            await bot.send_photo(query.from_user.id, photo, caption="pandas", reply_to_message_id=query.message.message_id)

        await bot.send_message(query.from_user.id, f'Что делаем дальше?', reply_markup=get_keyboard())
    elif callback_data_action == 'add_data':
        await bot.send_message(query.from_user.id, f'type /add [five parameters]', reply_markup=get_keyboard2("/add [*args]"))
    elif callback_data_action == 'del_data':
        await bot.send_message(query.from_user.id, f'type /del [id to delete]', reply_markup=get_keyboard2("/del [*args]"))
    elif callback_data_action == 'edit_data':
        await bot.send_message(query.from_user.id, f'type /edit [six parameters]', reply_markup=get_keyboard2("/edit [*args]"))

    # await bot.edit_message_text(
    #     f'Что делаем дальше?',
    #     query.from_user.id,
    #     query.message.message_id,
    #     reply_markup=get_keyboard(),
# )
#    await bot.send_message(query.from_user.id, f'Для продолжения /start')

# handle the cases when this exception raises


@ dp.errors_handler(exception=MessageNotModified)
async def message_not_modified_handler(update, error):
    return True  # errors_handler must return True if error was handled correctly


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
