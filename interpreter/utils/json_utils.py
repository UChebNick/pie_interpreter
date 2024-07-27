import asyncio
import json
import time

import aiofiles
import os
from interpreter.utils import container_utils

async def create_container_json(path, message, max_time):


    container_json = {"container": {
      "contract_status": 0,
      "unix_time": time.time(),
      "max_time": max_time,
      "messages": [],
      "saved_cells": [],
      "cells": ['message'],
      "cells_data": [message]
    }}
    j = json.dumps(container_json)

    async with aiofiles.open(path, 'w') as f:
        await f.write(j)


async def del_json_file(path):
    print(path)
    os.unlink(path)


async def save_new_json(container, path, host_json, messages, cells, cells_data):
    print("ns")
    new_json = host_json
    new_json['container']['messages'] = messages
    new_json['container']['cells'] = cells
    new_json['container']['cells_data'] = cells_data
    print(new_json)
    j = json.dumps(new_json)
    async with aiofiles.open(path, 'w') as f:
        await f.write(j)
    await container_utils.save_json(container=container, host_path=path, container_path='.')


async def json_handler(path, container):
    json_name = path.split('\\')[-1]
    get_cells_data = []
    async with aiofiles.open(path, 'r') as f:
        json_data = await f.read()
    host_json = json.loads(json_data)
    start_time = host_json['container']['unix_time']
    max_time = host_json['container']['max_time']
    if time.time() - start_time < 2:
        return


    container_json = await container_utils.get_json(container=container, path=f'{json_name}')
    if container_json['container']['saved_cells']:
        pass
        # save cells
    print(start_time - time.time())
    if container_json['container']['contract_status'] == 1 or time.time() - start_time >= max_time:
        container.stop()

        if len(container_json['container']['messages']) == 0:

            await del_json_file(path)
            # send json
            return True




        else:
            pass
            # send json
    elif len(container_json['container']['cells']) > len(container_json['container']['cells_data']):
        get_cells = container_json['container']['cells'][len(container_json['container']['cells_data']):]
        pass
        # get cells data
        get_cells_data = None
    cells_data = container_json['container']['cells_data'] + get_cells_data
    await save_new_json(container=container, path=path, host_json=host_json, messages=container_json['container']['messages'], cells=container_json['container']['cells'], cells_data=cells_data)




