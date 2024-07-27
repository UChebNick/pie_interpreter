import threading
import time
import asyncio
from concurrent.futures import ThreadPoolExecutor
from interpreter.image import client, tag
from interpreter.utils import utils, json_utils, container_utils

class code_runner:
    def __init__(self, code, message, mem='500M', nano_cpus=10000000, max_time=0.1):
        self.code = code
        self.message = message
        self.max_time = max_time
        self.mem = mem
        self.nano_cups = nano_cpus

    async def __aenter__(self):
        code = self.code.replace("\u00A0", " ")
        self.code = code.replace('\"', r'\"')

        return self
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass


    async def start(self):
        name = utils.generate_random_string(16)
        container = await container_utils.deploy_container(code=self.code, client=client, name=name, tag=tag, mem=self.mem, nano_cpus=self.nano_cups)

        self.container = container
        self.name = name


    async def json(self):
        file_path = f'interpreter\\container_json\\json_{self.name}.json'

        await json_utils.create_container_json(path=file_path, message=self.message, max_time=self.max_time)
        await container_utils.save_json(container=self.container, host_path=file_path, container_path='.')
        self.json_path = file_path


    async def handle(self):
        async def thread_handle():
            while True:
                await asyncio.sleep(1)
                await json_utils.json_handler(path=self.json_path, container=self.container)
        def start():
            pool = asyncio.new_event_loop()
            pool.create_task(thread_handle())
        threading.Thread(target=start, daemon=True).start()


    async def get_console(self):
        return self.container.logs()


    async def remove(self):
        self.container.stop()
        self.container.remove()







