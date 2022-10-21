# Создайте программу для игры в ""Крестики-нолики"".

"""
This is a simple example of usage of CallbackData factory
For more comprehensive example see callback_data_factory.py
"""

import logging
import typing

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils.callback_data import CallbackData
from aiogram.utils.exceptions import MessageNotModified

logging.basicConfig(level=logging.INFO)

API_TOKEN = 'TOKEN'

EMPTY_BOX = u"\U0001F532"
CROSS_BOX = u"\u274C"
CIRCLE_BOX = u"\u26AA"

bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

vote_cb = CallbackData('vote', 'action')  # vote:<action>

turn = {}
count = {}
board = {}


def get_keyboard(theBoard):
    markup1 = types.InlineKeyboardMarkup(row_width=3)
    markup1.row(
        types.InlineKeyboardButton(
            theBoard['1'], callback_data=vote_cb.new(action='1')),
        types.InlineKeyboardButton(
            theBoard['2'], callback_data=vote_cb.new(action='2')),
        types.InlineKeyboardButton(
            theBoard['3'], callback_data=vote_cb.new(action='3')),
    )
    markup1.row(
        types.InlineKeyboardButton(
            theBoard['4'], callback_data=vote_cb.new(action='4')),
        types.InlineKeyboardButton(
            theBoard['5'], callback_data=vote_cb.new(action='5')),
        types.InlineKeyboardButton(
            theBoard['6'], callback_data=vote_cb.new(action='6')),
    )
    markup1.row(
        types.InlineKeyboardButton(
            theBoard['7'], callback_data=vote_cb.new(action='7')),
        types.InlineKeyboardButton(
            theBoard['8'], callback_data=vote_cb.new(action='8')),
        types.InlineKeyboardButton(
            theBoard['9'], callback_data=vote_cb.new(action='9')),
    )
    return markup1


@ dp.message_handler(commands=['reset'])
async def cmd_start(message: types.Message):
    # get value if key exists else set to 0
    turn[message.from_user.id] = CROSS_BOX
    count[message.from_user.id] = 0
    board[message.from_user.id] = {
        str(list1): EMPTY_BOX for list1 in range(1, 10)}
    theBoard = board.get(message.from_user.id, {str(
        list1): EMPTY_BOX for list1 in range(1, 10)})
    await message.reply(f'Игра началась ходит {CROSS_BOX}', reply_markup=get_keyboard(theBoard))


@ dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    # get value if key exists else set to 0
    myturn = turn.get(message.from_user.id, CROSS_BOX)
    mycount = count.get(message.from_user.id, 0)
    theBoard = board.get(message.from_user.id, {str(
        list1): EMPTY_BOX for list1 in range(1, 10)})
    await message.reply(f'Игра началась ходит {CROSS_BOX}', reply_markup=get_keyboard(theBoard))


@ dp.callback_query_handler(vote_cb.filter(action=['1', '2', '3', '4', '5', '6', '7', '8', '9']))
async def callback_vote_action(query: types.CallbackQuery, callback_data: typing.Dict[str, str]):
    # callback_data contains all info from callback data
    logging.info('Got this callback data: %r', callback_data)
    await query.answer()  # don't forget to answer callback query as soon as possible
    callback_data_action = callback_data['action']
    myturn = turn.get(query.from_user.id, CROSS_BOX)
    mycount = count.get(query.from_user.id, 0)
    theBoard = board.get(query.from_user.id, {str(
        list1): EMPTY_BOX for list1 in range(1, 10)})

    if theBoard[callback_data_action] == EMPTY_BOX:
        theBoard[callback_data_action] = myturn
        mycount = str(int(mycount)+1)

    won = 0
    if int(mycount) >= 5:
        if theBoard['7'] == theBoard['8'] == theBoard['9'] != EMPTY_BOX:
            won = 1

        elif theBoard['4'] == theBoard['5'] == theBoard['6'] != EMPTY_BOX:
            won = 1

        elif theBoard['1'] == theBoard['2'] == theBoard['3'] != EMPTY_BOX:
            won = 1

        elif theBoard['1'] == theBoard['4'] == theBoard['7'] != EMPTY_BOX:
            won = 1

        elif theBoard['2'] == theBoard['5'] == theBoard['8'] != EMPTY_BOX:
            won = 1

        elif theBoard['3'] == theBoard['6'] == theBoard['9'] != EMPTY_BOX:
            won = 1

        elif theBoard['7'] == theBoard['5'] == theBoard['3'] != EMPTY_BOX:
            won = 1

        elif theBoard['1'] == theBoard['5'] == theBoard['9'] != EMPTY_BOX:
            won = 1

    if won:
        await bot.send_message(query.from_user.id, f'Конец, выиграл {myturn}')

    if int(mycount) == 9 and won == 0:
        await bot.send_message(query.from_user.id, f'Конец, ничья')
        won = 1

    if myturn == CROSS_BOX:
        myturn = CIRCLE_BOX
    else:
        myturn = CROSS_BOX

    turn[query.from_user.id] = myturn
    count[query.from_user.id] = mycount
    board[query.from_user.id] = theBoard
    if not won:
        await bot.edit_message_text(
            f'Ваш ход {myturn}! Сделано ходов {mycount} Куда ходим?',
            query.from_user.id,
            query.message.message_id,
            reply_markup=get_keyboard(theBoard),
        )
    else:
        await bot.edit_message_text(
            f'Игра окончена Сделано ходов {mycount}',
            query.from_user.id,
            query.message.message_id,
            reply_markup=get_keyboard(theBoard),
        )
        turn[query.from_user.id] = CROSS_BOX
        count[query.from_user.id] = 0
        theBoard = {str(list1): EMPTY_BOX for list1 in range(1, 10)}
        board[query.from_user.id] = theBoard
        await bot.send_message(query.from_user.id, f'Для продолжения /start')

# handle the cases when this exception raises


@ dp.errors_handler(exception=MessageNotModified)
async def message_not_modified_handler(update, error):
    return True  # errors_handler must return True if error was handled correctly


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
