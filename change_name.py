from telethon import TelegramClient, functions, errors
import asyncio
import logging
import os
from datetime import datetime
import pytz

# Берём из переменных окружения Railway
api_id = int(os.environ.get('API_ID', 123456))
api_hash = os.environ.get('API_HASH', 'your_api_hash')
session = 'my_userbot'

# Настройка логов
logging.basicConfig(
    filename='change_name.log',
    level=logging.INFO,
    format='%(asctime)s %(message)s'
)

# Интервал обновления (60 секунд = 1 минута)
INTERVAL = 60  # секунд

async def main():
    async with TelegramClient(
        session,
        api_id,
        api_hash,
        device_model="iPhone 55 Pro",
        system_version="iOS 100.1",
        app_version="Telegram 10.0",
        lang_code="en",
        system_lang_code="en"
    ) as client:
        print("✅ Бот запущен! Обновляем имя каждую минуту...")
        logging.info("Бот запущен")
        
        while True:
            try:
                # Получаем московское время
                msk_tz = pytz.timezone('Europe/Moscow')
                now = datetime.now(msk_tz)
                time_str = now.strftime('%H:%M')
                
                # Новое имя с временем
                new_name = f"𝚢𝚞𝚙𝚒-𝚢𝚘 [{time_str}]"
                
                # Обновляем имя
                await client(functions.account.UpdateProfileRequest(first_name=new_name))
                
                print(f"[{now.strftime('%H:%M:%S')}] Имя обновлено: {new_name}")
                logging.info(f"Имя изменено на: {new_name}")
                
                await asyncio.sleep(INTERVAL)
                
            except errors.FloodWaitError as e:
                print(f"⚠️ FloodWait: жду {e.seconds} секунд")
                logging.warning(f"FloodWaitError: жду {e.seconds} секунд")
                await asyncio.sleep(e.seconds)
                
            except Exception as e:
                print(f"❌ Ошибка: {e}")
                logging.error(f"Ошибка смены имени: {e}")
                await asyncio.sleep(60)

if __name__ == '__main__':
    asyncio.run(main())
