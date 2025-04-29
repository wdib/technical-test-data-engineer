import aiohttp
import pytest
from aioresponses import aioresponses
from src.pipeline.extract import extract

async def test_extract_success():
    base_url = 'http://127.0.0.1:8000/'
    endpoint = 'tracks'
    response_page_1 = {
        'items' : [ { 'id': 49920, 'name': 'thus', } ],
        'pages' : 3
    }
    response_page_2 = {
        'items' : [ { 'id': 46292, 'name': 'account', } ],
        'pages' : 3
    }
    response_page_3 = {
        'items' : [ { 'id': 31873, 'name': 'argue', } ],
        'pages' : 3
    }
    response_all_pages = []
    response_all_pages.extend( response_page_1[ 'items' ] )
    response_all_pages.extend( response_page_2[ 'items' ] )
    response_all_pages.extend( response_page_3[ 'items' ] )

    with aioresponses() as m:
        m.get( base_url + endpoint + '?page=1', payload=response_page_1 )
        m.get( base_url + endpoint + '?page=2', payload=response_page_2 )
        m.get( base_url + endpoint + '?page=3', payload=response_page_3 )

        async with aiohttp.ClientSession() as session:
            result = await extract( endpoint, session )
            assert result == response_all_pages

async def test_extract_failure():
    base_url = 'http://127.0.0.1:8000/'
    endpoint = 'tracks'

    with aioresponses() as m:
        m.get( base_url + endpoint + '?page=1', status=500 )

        async with aiohttp.ClientSession() as session:
            result = await extract( endpoint, session )
            assert result == []