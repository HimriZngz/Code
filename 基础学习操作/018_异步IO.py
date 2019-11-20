import asyncio

@asyncio.coroutine
def hello():
    print('随便打印一个')
    r = yield from asyncio.sleep(2)
    print('再随便打印一下')


loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
loop.close()
