import asyncio
from depspy import DepsClient

async def main():
    client = DepsClient(api_key="your_api_key_here")
    async with client:
        server_id = 5

        try:
            fractions = await client.get_fractions(server_id)
            print(f"Total fractions: {len(fractions.data)}")
            await asyncio.sleep(3)
            
            for fraction_name in fractions.data:
                print(f"\nFraction: {fraction_name}")
                print(f"ID: {await client.get_fraction_id_name(fraction_name)}")
                
                fraction_online = await client.get_fraction_online(server_id, fraction_name)
                print("Online members:")
                for player in fraction_online.data.values():
                    status = []
                    if player.isLeader:
                        status.append("Лидер")
                    if player.isZam:
                        status.append("Зам")
                    if player.inUniform:
                        status.append("В форме")
                    else:
                        status.append("Не в форме")
                    
                    print(f"- {player.name} (Level {player.level})")
                    if player.member:
                        print(f"  Member: {player.member}")
                    if player.position:
                        print(f"  Должность: {player.position}")
                    if status:
                        print(f"  Статус: {', '.join(status)}")
                await asyncio.sleep(3)

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main()) 