from aiogram import *
from aiogram.dispatcher.filters import Text  # подключаем библиотеки

bot = Bot(token='6219803057:AAGD34EaV6Lcno21ylTR8oil47abhHzSbJs')  # подключаем токен
bot = Dispatcher(bot)

@bot.message_handler(commands=['start'])  # задаём команду "старт"
async def send_welcome(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)  # реализовываем красивую разметку для кнопок
    buttons = ["Да", "/stop", "/help", "/about"]  # добавляем кнопки
    keyboard.add(*buttons)
    await message.answer("Привет! Можешь отправить мне любое сообщение и я его отправлю тебе, если ты нажмёшь на кнопку 'Да'",  # Нам отправляют сообщение
                         reply_markup=keyboard)

@bot.message_handler(Text(equals="Да"))
async def messi(message: types.Message):
    await message.reply("Отправь мне любое сообщение", reply_markup=types.ReplyKeyboardRemove())   # Нам отправляют сообщение, закрывают клавиатуру и дают
    @bot.message_handler()                                                                         # право на ввод слов
    async def soobshenie(msg: types.Message):  # начало эхо бота
        await msg.answer(msg.text)

@bot.message_handler(commands=['stop'])
async def messi(message: types.Message):
    await message.reply('Хорошо, напиши мне позже...', reply_markup=types.ReplyKeyboardRemove())

@bot.message_handler(commands=['help'])
async def pomosh(message: types.Message):
    await message.reply('Вы открыли справочник. \n/start: Запуск бота \n/stop: Остановка бота'
                        '\nКнопка "Да": Включится функция отправки эхо-сообщений')

@bot.message_handler(commands=['about'])
async def info(message: types.Message):
    await message.reply('Бот создан на языке Python с помощью фреймворка aiogram')


if __name__ == '__main__':  # запускаем бота
    executor.start_polling(bot)
