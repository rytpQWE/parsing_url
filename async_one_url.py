import asyncio
import aiohttp
import aiofiles
import time
import json
import shutil
import os


OUTPUT_DIRECTORY = 'output'

url = 'https://jsonplaceholder.typicode.com/photos'

shutil.rmtree(OUTPUT_DIRECTORY, ignore_errors=True) # remove previous output directory
os.makedirs(OUTPUT_DIRECTORY) # create output directory


async def get_api_data():
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def write_entity_to_file(item):
    async with aiofiles.open(f'{OUTPUT_DIRECTORY}/{item["id"]}.json', mode='w') as f:
        await f.write(json.dumps(item, indent=4, sort_keys=False, ensure_ascii=False))


async def main():
    data = await get_api_data()

    for item in data:
        await write_entity_to_file(item)


start_time = time.time()

asyncio.run(main())

end_time = time.time()
print(f'Execution time: {end_time - start_time} seconds')