import asyncio
import random
from asyncua import Client


URL = 'opc.tcp://localhost:4840/freeopcua/server/'
URI = 'http://examples.freeopcua.github.io'


async def main():
    async with Client(url=URL) as client:
        idx = await client.get_namespace_index(URI)
        var = await client.nodes.root.get_child(['0:Objects',
                                                 f'{idx}:MyObject',
                                                 f'{idx}:MyVariable'])
        print(var.__class__.__name__)

        print('Read  MyObject/MyVariable =', await var.read_value())
        val = random.randint(1, 127)
        print('Write MyObject/MyVariable =', val)
        await var.write_value(val)
        print('Read  MyObject/MyVariable =', await var.read_value())


if __name__ == '__main__':
    asyncio.run(main())
