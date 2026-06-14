import asyncio
from app import Service


# if __name__ == '__main__':
#     Service('default-name-app').start()


async def main():
    asyncio_loop = asyncio.get_event_loop()

    await Service('default-name-app').start(asyncio_loop)
    # listen_for_connection(server_socket, asyncio_loop)

if __name__ == '__main__':
    # srv = Service('default-name-app')
    # asyncio.run(main(), debug=True)
    asyncio.run(main())
