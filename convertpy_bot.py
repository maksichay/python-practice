import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
BOT_TOKEN = "8744682750:AAHDnSOqvJkdh4hpZ-7YKxPxWFPIoZBiRLc"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
@dp.message(Command("start"))
async def cmd_start(message:types.Message):
    await message.answer("Привет! я твой бот-конвертер валют")
async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())