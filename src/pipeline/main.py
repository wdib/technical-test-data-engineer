import asyncio
import aiohttp
from extract import extract
from transform import transform
from load import load
import logging

logger = logging.getLogger( __name__ )
logger.setLevel( logging.INFO )

async def run_etl( endpoint, session ):
    extracted_data = await extract( endpoint, session )
    transformed_data = transform( extracted_data, endpoint )
    await load( transformed_data, endpoint )

async def main():
    endpoints = [ 'tracks', 'users', 'listen_history' ]
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(
            *( run_etl( endpoint, session ) for endpoint in endpoints )
        )

if __name__ == '__main__':
    logging.basicConfig( filename='pipeline.log' )
    logger.info( 'Started ETL pipeline' )
    asyncio.run(main())
    logger.info( 'Ended ETL pipeline' )