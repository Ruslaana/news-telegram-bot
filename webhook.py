import logging
from aiogram import executor
from bot import dp, bot
from config import WEBHOOK_URL, WEBAPP_HOST, WEBAPP_PORT

logging.basicConfig(level=logging.INFO)


async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)
    print(f"Webhook installed on {WEBHOOK_URL}")


async def on_shutdown(dp):
    await bot.delete_webhook()
    await dp.storage.close()
    await dp.storage.wait_closed()
    print("Бот вимкнено")

if __name__ == '__main__':
    executor.start_webhook(
        dispatcher=dp,
        webhook_path='/webhook',
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT
    )
