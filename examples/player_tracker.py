import asyncio
from depspy import DepsClient

async def main():
    client = DepsClient(api_key="your_api_key_here")
    server_id = 5
    nickname = "Nicolas_Reed"

    async def player_online_callback():
        print(f"Игрок {nickname} зашел на сервер!")

    async with client:
        print(f"Начинаем отслеживание игрока {nickname}...")
        await client.track_player_online(nickname, server_id, player_online_callback, check_interval=60)
        await asyncio.sleep(300)  # Держим скрипт запущенным в течение 5 минут

if __name__ == "__main__":
    asyncio.run(main())