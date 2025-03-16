import asyncio
from bot import Bot
import pyrogram.utils
from pyrogram.errors import FloodWait

pyrogram.utils.MIN_CHANNEL_ID = -1009147483647  # Private channel ID fix

async def run_bot():
    while True:
        try:
            bot = Bot()
            await bot.start()
            print("✅ Bot started successfully!")
            await bot.idle()
        except FloodWait as e:
            print(f"⚠️ FloodWait detected! Waiting {e.value} seconds...")
            await asyncio.sleep(e.value)  # Telegram ki limit ka wait karega
        except Exception as ex:
            print(f"❌ Bot crashed! Error: {ex}")
            await asyncio.sleep(10)  # Crash hone ke baad 10s wait karega

if __name__ == "__main__":
    asyncio.run(run_bot())  # Async loop me run karna zaroori hai
