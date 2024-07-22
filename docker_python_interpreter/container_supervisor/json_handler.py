import asyncio
import json
import time

import aiofiles
import os
import docker
import container_utils


async def create_container_json(name, message):
    file_name = f'json_{name}.json'

    container_json = {"container": {
      "contract_status": 0,
      "unix_time": time.time(),
      "messages": [],
      "cells": ['message'],
      "cells_data": [message]
    }}
    j = json.dumps(container_json)
    async with aiofiles.open("container_json_socket\\" + file_name, 'w') as f:
        await f.write(j)

async def del_json_file(path):
    os.remove(path)

async def get_json(path):
    async with aiofiles.open(path, 'r') as f:
        json_data = await f.read()
        return json.loads(json_data)

async def json_handler(path, container):
    async with aiofiles.open(path, 'r') as f:
        json_data = await f.read()
    container_json = json.loads(json_data)
    unix_time = container_json['unix_time']


    if container_json['contract_status'] == 1:
        # send msg
        if len(container_json['messages']) == 0:
            await del_json_file(path)

    if



