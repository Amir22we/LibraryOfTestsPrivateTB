import asyncio

from aiogram import Bot, Dispatcher 

from config import TOKEN
from app.handlers import router
from keep_alive import keep_alive

bot = Bot(token=TOKEN)
dp = Dispatcher()
keep_alive()
async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        print("Бот запущен")
        asyncio.run(main())
    except KeyboardInterrupt:
        print('EXit')
