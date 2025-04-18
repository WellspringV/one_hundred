# Python modules
import asyncio
import logging
import os
import re

# Third-party modules
from aiogram import (
    Bot,
    Dispatcher,
    F,
    Router,
    types
)

# Local modules
from utils.csvutils import csv_write


logging.basicConfig(
    format="%(levelname)s: %(asctime)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    level=logging.INFO,
)


APP_TOKEN = os.getenv("BOT_TOKEN")
PATH_TO_STAT_TABLE = "stat/detail.csv"


router = Router()


@router.message(
        F.chat.type.in_({"group"}),
        F.text.regexp(re.compile(r'/add \S+\s+(\d+\s+){3,}\d+',))
)
async def handle_add(message: types.Message):
    """ Parse standart message /add sto A B C D"""
    # A - Pull ups
    # B - Squats
    # C - Push ups
    # D - Squats

    username = message.from_user.username
    cmd, option,  *_ = message.text.split()

    if cmd == '/add' and option == 'sto':
        pull_ups, squats_1, push_ups, squats_2 = _
        # wod mean Workout of Day
        wod = { 
            "username": username,
            "pull_ups": pull_ups,
            "squats_1": squats_1,
            "push_ups": push_ups,
            "squats_2": squats_2,
        }
        with open(PATH_TO_STAT_TABLE, 'a', newline='') as f:
            csv_write(f, [wod])
    await message.answer(f"Результаты тренировки сохранены")


async def main():
    bot = Bot(token=APP_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
