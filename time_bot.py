import asyncio
from datetime import datetime
import pytz
from telethon import TelegramClient
import os

API_ID = int(os.environ['API_ID'])
API_HASH = os.environ['API_HASH']
BOT_TOKEN = os.environ['BOT_TOKEN']

async def main():
    client = TelegramClient('session', API_ID, API_HASH)
    await client.start(bot_token=BOT_TOKEN)
    print("✅ Бот запущен!")
    
    while True:
        try:
            msk = pytz.timezone('Europe/Moscow')
            now = datetime.now(msk)
            time_str = now.strftime('%H:%M')
            new_name = f"Илья [{time_str}]"
            
            await client.edit_profile(first_name=new_name)
            print(f"[{now.strftime('%H:%M:%S')}] Имя обновлено: {new_name}")
            
        except Exception as e:
            print(f"Ошибка: {e}")
        
        await asyncio.sleep(60)

if __name__ == '__main__':
    asyncio.run(main())
