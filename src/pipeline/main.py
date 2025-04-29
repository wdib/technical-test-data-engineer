import asyncio
import aiohttp
from extract import extract
from transform import transform
from load import load

async def run_etl( endpoint, session ):
    extracted_data = await extract( endpoint, session )
    transformed_data = await transform( extracted_data )
    await load( transformed_data )

async def main():
    endpoints = [ 'tracks' ]
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(
            *( run_etl( endpoint, session ) for endpoint in endpoints )
        )

if __name__ == '__main__':
    asyncio.run(main())