import asyncio
from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram.client.session.aiohttp import AiohttpSession

session = AiohttpSession(api="https://jolly-mode-c61a.vanya-fyodorov-04.workers.dev/")
bot = Bot(token="7793645226:AAGETfsUttLsZwosS0lck2BwndkQ3yCQHPI", session=session)

# 1. Вставь свой токен сюда
BOT_TOKEN = "7793645226:AAGETfsUttLsZwosS0lck2BwndkQ3yCQHPI"

# 2. Вставь свой chat_id (узнаем на шаге 3)
MY_CHAT_ID = 1359579105

# 3. Настройка бота
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# 4. Функция, которая отправляет напоминание
async def send_reminder():
    text = (
        "🎸 **Время практики!**\n\n"
        "Сегодня учим песню: *I Love You*\n"
        "Аккорды: Am, F, C, G\n\n"
        "Попробуй сыграть комбинацию 3-6, 4-5, которую ты уже знаешь, и добавь аккорды. У тебя получится!"
    )
    await bot.send_message(chat_id=MY_CHAT_ID, text=text, parse_mode="Markdown")

# 5. Запуск планировщика
async def main():
    # Настраиваем ежедневный запуск в 19:00
    scheduler = AsyncIOScheduler(timezone="Europe/Moscow") # Укажи свой часовой пояс
    scheduler.add_job(send_reminder, trigger='cron', hour=19, minute=0)
    scheduler.start()

    print("Бот запущен. Жду времени отправки...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
