import aiohttp

async def extract( endpoint, session ):
    base_url = 'http://127.0.0.1:8000/' + endpoint
    page = 1
    all_list = []
    while True:
        params = { 'page' : page }
        async with session.get( base_url, params=params ) as response:
            try:
                response.raise_for_status()
                fetch_json = await response.json()
                fetch_list = fetch_json[ 'items' ]
                page_limit = fetch_json[ 'pages' ]
                all_list.extend( fetch_list )
                print( f'{response.status} /{endpoint} {page}/{page_limit}' )
                if page == page_limit:
                    break
                page += 1
            except aiohttp.ClientResponseError as e:
                print( f'/{endpoint} page ({page}), Failed: {e.status} {e.message}' )
                break
    return all_list