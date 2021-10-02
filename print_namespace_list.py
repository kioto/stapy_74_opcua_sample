import asyncio
from asyncua import Client


URL = 'opc.tcp://localhost:4840/freeopcua/server/'


async def main():
    async with Client(url=URL) as client:
        for idx, ns in enumerate(await client.get_namespace_array()):
            print(idx, ns)


if __name__ == '__main__':
    asyncio.run(main())
