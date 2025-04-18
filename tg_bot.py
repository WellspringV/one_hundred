import logging
import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command


logging.basicConfig(
    format="%(levelname)s: %(asctime)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    level=logging.INFO,
)

""" Token will be imported from env """
APP_TOKEN = ""
PATH_TO_TODO_TABLE = "todo_result/todo_list.csv"


bot = Bot(token=APP_TOKEN)
dp = Dispatcher()


@dp.message(Command("all"))
async def all_tasks(message: types.Message):
    try:
        1 / 0
    except Exception as e:
        logging.error(f"Error: {e}")
        await message.answer("❌ Ошибка при загрузке задач")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

print('hello dydy Vity')
