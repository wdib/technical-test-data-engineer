import aiofiles
import json
from pathlib import Path

async def load( data, filename ):
    data_dir = Path( 'data' )
    data_dir.mkdir( exist_ok=True )
    file_path = data_dir / f'{filename}.json'
    async with aiofiles.open( file_path, 'w' ) as f:
        await f.write( json.dumps( data, ensure_ascii=False, indent=4 ) )