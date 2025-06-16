import asyncio
from depspy import DepsClient

async def main():
    client = DepsClient(api_key="your_api_key_here")
    async with client:
        server_id = 5
        nickname = "Nicolas_Reed"

        try:
            is_online = await client.is_player_online(nickname, server_id)
            print(f"Player {nickname} is {'online' if is_online else 'offline'}")

            level = await client.get_player_level(nickname, server_id)
            money = await client.get_player_money(nickname, server_id)
            org = await client.get_player_organization(nickname, server_id)
            property = await client.get_player_property(nickname, server_id)
            vip = await client.get_player_vip_info(nickname, server_id)

            print(f"Level: {level}")
            print(f"Money: {money.hand}$ cash, {money.bank}$ bank, {money.deposit}$ deposit, {money.phone_balance}$ phone, {money.donate_currency} donate, {money.total}$ total")
            if org:
                print(f"Organization: {org.name} (Rank: {org.rank})")
            print(f"Property: Houses - {property.houses}, Businesses - {property.businesses}")
            print(f"VIP: {vip.level}, ADDVIP: {vip.add_vip} (Expires: {vip.expiration_date})")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main()) 