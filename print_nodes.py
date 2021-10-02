import asyncio
from asyncua import Client


URL = 'opc.tcp://localhost:4840/freeopcua/server/'


async def print_node(node, parent_node=None, path=''):
    children = await node.get_children()
    if not children:
        val = None
        try:
            val = await node.read_value()
        except Exception:
            val = None

        print(f'{path}({node}) = {val}')

    else:
        for n in children:
            bname = await n.read_browse_name()
            if path:
                new_path = path + '/' + bname.Name
            else:
                new_path = bname.Name
            await print_node(n, node, new_path)


async def main():
    async with Client(url=URL) as client:
        top_obj = client.get_objects_node()
        await print_node(top_obj)

if __name__ == '__main__':
    asyncio.run(main())
