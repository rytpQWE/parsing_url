import requests
import time
import json
import shutil
import os


OUTPUT_DIRECTORY = 'output'

url = 'https://jsonplaceholder.typicode.com/photos'

shutil.rmtree(OUTPUT_DIRECTORY, ignore_errors=True) # remove previous output directory
os.makedirs(OUTPUT_DIRECTORY) # create output directory

start_time = time.time()

response = requests.get(url).json()
# print(response)

for item in response:
    with open(f'{OUTPUT_DIRECTORY}/{item["id"]}.json', 'w') as file:
        json.dump(item, file, sort_keys=False, indent=4, ensure_ascii=False)

end_time = time.time()
print(f'Execution time: {end_time - start_time} seconds')