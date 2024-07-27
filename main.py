import asyncio

import interpreter


async def m():
    async with interpreter.code_runner('while True: print(1)', message={"s": "s"}) as f:
        await f.start()
        await f.json()
        await f.handle()
        await asyncio.sleep(10)
        print(await f.get_console())

asyncio.run(m())