import asyncio
from depspy.client import DepsClient

async def main():
    client = DepsClient(api_key="your_api_key")
    async with client:
        ghetto_data = await client.get_ghetto(5)
        if ghetto_data and ghetto_data.data and ghetto_data.data.data:
            print("Квадраты гетто:")
            for idx, square in ghetto_data.data.data.items():
                print(f"  Квадрат {idx}:")
                if square.squareStart:
                    print(f"    Начало: ({square.squareStart.x}, {square.squareStart.y})")
                if square.squareEnd:
                    print(f"    Конец:  ({square.squareEnd.x}, {square.squareEnd.y})")
                print(f"    Цвет: {square.color} (hex: {hex(square.color)})")

if __name__ == "__main__":
    asyncio.run(main()) 