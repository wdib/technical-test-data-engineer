import aiofiles
import json
from pathlib import Path
from datetime import datetime

async def load( data, endpoint ):
    data_dir = Path( 'data' )
    data_dir.mkdir( exist_ok=True )
    timestamp = datetime.now().strftime( '%Y_%m_%d_%H_%M_%S' )
    file_path = data_dir / f'{timestamp}-{endpoint}.json'
    async with aiofiles.open( file_path, 'w' ) as f:
        await f.write( json.dumps( data, ensure_ascii=False, indent=4 ) )