import asyncio
import random
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.telegram import TelegramAPIServer


# --- Настройки ---
BOT_TOKEN = "7793645226:AAGETfsUttLsZwosS0lck2BwndkQ3yCQHPI"
MY_CHAT_ID = 1359579105
PROXY_URL = "https://jolly-mode-c61a.vanya-fyodorov-04.workers.dev/"

QUOTES = [
    "«Если ты не можешь изменить ситуацию, измени своё отношение к ней» — Субару Нацуки",
    "«Я не герой. Но я тот, кто не сдаётся, даже когда всё против меня» — Субару Нацуки",
    "«Даже если весь мир отвернётся, я буду кричать, пока не охрипну» — Субару Нацуки",
    "«Слабость — это не грех. Грех — это не пытаться стать сильнее» — Субару Нацуки",
    "«Я вернусь. Снова и снова, пока не найду правильный путь» — Субару Нацуки",
    "«Неважно, сколько раз ты упадёшь. Важно, сколько раз ты встанешь» — Субару Нацуки",
    "«Тот, кто не может спасти себя, не спасёт и других. Но тот, кто спас хотя бы одного — уже герой» — Субару Нацуки",
    "«Я не хочу быть особенным. Я хочу быть нужным» — Субару Нацуки",
    "«Если страх остановит тебя, ты никогда не узнаешь, что могло быть» — Эмилия",
    "«Даже в самой тёмной ночи есть звёзды. Главное — поднять голову» — Рем",
]

# --- Бот и диспетчер (один раз!) ---
session = AiohttpSession(api=TelegramAPIServer.from_base("https://jolly-mode-c61a.vanya-fyodorov-04.workers.dev/"))
bot = Bot(token=BOT_TOKEN, session=session)
dp = Dispatcher()

# --- Обработчик /start ---
@dp.message(CommandStart())
async def cmd_start(message: Message):
    photo_url = "https://static.wikia.nocookie.net/rezero/images/6/64/Beatrice_BD.png/revision/latest?cb=20170130163823&path-prefix=ru" 
    await message.answer_photo (
        photo=photo_url,
        caption="Привет! Бот на связи. Мотивация из Re:Zero придёт в 10:00 утра ☀️"
    )

# --- Функция напоминания ---
async def send_motivation():
    quote = random.choice(QUOTES)
    await bot.send_message(chat_id=MY_CHAT_ID, text=f"🌅 **Доброе утро!**\n\n{quote}", parse_mode="Markdown")

# --- Запуск ---
async def main():
    scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
    scheduler.add_job(send_motivation, trigger='cron', hour=10, minute=0)
    scheduler.start()

    print("Бот запущен. Жду 10:00...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
