import asyncio
import aiohttp

async def main():
    base_url = 'http://127.0.0.1:8000/tracks'
    page = 1
    all_list = []
    async with aiohttp.ClientSession() as session:
        while True:
            params = { 'page' : page }
            async with session.get( base_url, params=params ) as response:
                print( f'Page {page}, Status {response.status}' )
                fetch_json = await response.json()
                fetch_list = fetch_json[ 'items' ]
                all_list.extend( fetch_list )
                if page == fetch_json[ 'pages' ]:
                    break;
                page += 1

if __name__ == '__main__':
    asyncio.run(main())