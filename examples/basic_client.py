import asyncio
from datetime import datetime
from depspy import DepsClient

async def main():
    client = DepsClient(api_key="your_api_key")
    print(f"API Key: {client.api_key}")
    print(f"Corporate Key: {client.corporate_key}")
    print(f"Base URL: {client.base_url}")
    print(f"Timeout: {client.timeout}")
    print(f"Max Retries: {client.max_retries}")
    print(f"Cache TTL: {client.cache_ttl}")
    print(f"Proxy: {client.proxy}")
    print(f"Verify SSL: {client.verify_ssl}")
    print(f"Session: {client._session}")
    async with client:
        status = await client.get_status()
        if status and status.servers:
            for server_name, server_status in status.servers.items():
                print(f"\nСервер: {server_name}")
                print(f"Онлайн: {server_status.has_online}")
                print(f"Собесы: {server_status.has_sobes}")
                if server_status.last_update:
                    print(f"Последнее обновление: {datetime.fromtimestamp(server_status.last_update).strftime('%d.%m.%Y %H:%M:%S')}")

if __name__ == "__main__":
    asyncio.run(main()) 