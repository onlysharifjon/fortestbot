import logging
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.middlewares.logging import LoggingMiddleware

API_TOKEN = "5284399613:AAEsTbSqPQ9MSKdRS9__Y9L-eqbhhI28Pcw"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware()


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer("ishladi ogola")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)