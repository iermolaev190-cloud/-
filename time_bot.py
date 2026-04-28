import asyncio
from datetime import datetime
import pytz
from telethon import TelegramClient, events

# ===== НАСТРОЙКИ (ЗАМЕНИ НА СВОИ) =====
API_ID = 15309699295  # Твой api_id с my.telegram.org
API_HASH = '74c77ec5dc83b1bd8b99ecce1225b977'  # Твой api_hash
BOT_TOKEN = '7563966618:AAGrnq9umOuhBn2wySvOrsronXWymH41yos'  # Токен от BotFather
YOUR_USER_ID = 7697645186  # Твой Telegram ID (число)
# ======================================

# Создаём клиента для аккаунта и бота
client = TelegramClient('user_session', API_ID, API_HASH)

async def update_name():
    """Обновляет имя пользователя с текущим временем"""
    try:
        # Получаем московское время
        msk_tz = pytz.timezone('Europe/Moscow')
        now = datetime.now(msk_tz)
        time_str = now.strftime('%H:%M')
        
        # Новое имя с временем в квадратных скобках
        new_name = f"Илья [{time_str}]"
        
        # Обновляем имя профиля
        await client.edit_profile(first_name=new_name)
        print(f"[{now.strftime('%H:%M:%S')}] Имя обновлено: {new_name}")
        
    except Exception as e:
        print(f"Ошибка: {e}")

async def main():
    # Запускаем клиента
    await client.start(bot_token=BOT_TOKEN)
    print("Бот запущен! Обновляет имя каждую минуту...")
    
    # Первое обновление сразу
    await update_name()
    
    # Обновляем каждую минуту
    while True:
        await asyncio.sleep(60)  # Ждём 60 секунд
        await update_name()

if __name__ == '__main__':
    asyncio.run(main())
