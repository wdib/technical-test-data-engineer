import asyncio
import aiohttp

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get( 'http://127.0.0.1:8000/tracks' ) as response:
            print( 'Status', response.status )
            fetch_json = await response.json()
            print( 'Body', fetch_json )

if __name__ == '__main__':
    asyncio.run(main())