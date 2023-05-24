import logging
from aiogram.dispatcher.filters import Text
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils.executor import start_webhook

API_TOKEN = '6219803057:AAGD34EaV6Lcno21ylTR8oil47abhHzSbJs'

WEBHOOK_HOST = 'https://d324-94-25-168-39.ngrok-free.app'
WEBHOOK_PATH = ''
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

WEBAPP_HOST = 'localhost'
WEBAPP_PORT = 8000

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)


async def on_shutdown(dp):
    logging.warning('Shutting down...')
    await bot.delete_webhook()
    logging.warning('Bye!')


@dp.message_handler(commands=['start'])  # задаём команду "старт"
async def send_welcome(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)  # реализовываем красивую разметку для кнопок
    buttons = ["Да", "/stop", "/help", "/about"]  # добавляем кнопки
    keyboard.add(*buttons)
    await message.answer("Привет! Можешь отправить мне любое сообщение и я его отправлю тебе, если ты нажмёшь на кнопку 'Да'",  # Нам отправляют сообщение
                         reply_markup=keyboard)


@dp.message_handler(Text(equals="Да"))
async def messi(message: types.Message):
    await message.reply("Отправь мне любое сообщение", reply_markup=types.ReplyKeyboardRemove())   # Нам отправляют сообщение, закрывают клавиатуру и дают
    @dp.message_handler()                                                                         # право на ввод слов
    async def soobshenie(msg: types.Message):  # начало эхо бота
        await msg.answer(msg.text)


@dp.message_handler(commands=['stop'])
async def messi(message: types.Message):
    await message.reply('Хорошо, напиши мне позже...', reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(commands=['help'])
async def pomosh(message: types.Message):
    await message.reply('Вы открыли справочник. \n/start: Запуск бота \n/stop: Остановка бота'
                   
                        '\nКнопка "Да": Включится функция отправки эхо-сообщений')


@dp.message_handler(commands=['about'])
async def info(message: types.Message):
    await message.reply('Бот создан на языке Python с помощью фреймворка aiogram')

start_webhook(
    dispatcher=dp,
    webhook_path=WEBHOOK_PATH,
    on_startup=on_startup,
    on_shutdown=on_shutdown,
    skip_updates=True,
    host=WEBAPP_HOST,
    port=WEBAPP_PORT
)
