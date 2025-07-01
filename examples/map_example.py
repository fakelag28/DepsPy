import asyncio
from depspy.client import DepsClient

async def main():
    client = DepsClient(api_key="your_api_key")
    async with client:
        map_data = await client.get_map(5)
        print("Дома:")
        print("  С владельцем:")
        for house in map_data.houses.hasOwner:
            print(f"    ID: {house.id}, Название: {house.name}, Владелец: {house.owner}, Аукцион: {'Да' if house.hasAuction else 'Нет'}")
            print(f"      Координаты: ({house.lx}, {house.ly})")
            print(f"      Ближайшая точка: {house.nearest_poi.name} ({house.nearest_poi.city}) [{house.nearest_poi.x}, {house.nearest_poi.y}]")
        print("  Без владельца:")
        for house in map_data.houses.noOwner:
            print(f"    ID: {house.id}, Название: {house.name}")
        print("  На аукционе:")
        for house in map_data.houses.onAuction:
            print(f"    ID: {house.id}, Название: {house.name}, Мин. ставка: {house.auMinBet}, Владелец: {house.owner}")
        print("  На маркете:")
        for house in map_data.houses.onMarketplace:
            print(f"    ID: {house.id}, Название: {house.name}, Владелец: {house.owner}")
        print("\nБизнесы:")
        print("  На аукционе:")
        for biz in map_data.businesses.onAuction:
            print(f"    ID: {biz.id}, Название: {biz.name}, Владелец: {biz.owner}, Мин. ставка: {biz.auMinBet}")
        print("  Без аукциона:")
        for biz_type, biz_list in map_data.businesses.noAuction.__root__.items():
            print(f"    Тип: {biz_type}")
            for biz in biz_list:
                print(f"      ID: {biz.id}, Название: {biz.name}, Владелец: {biz.owner}")
        print("  На маркете:")
        for biz in map_data.businesses.onMarketplace:
            print(f"    ID: {biz.id}, Название: {biz.name}, Владелец: {biz.owner}")

if __name__ == "__main__":
    asyncio.run(main()) 