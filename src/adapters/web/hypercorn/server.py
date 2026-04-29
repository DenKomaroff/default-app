from hypercorn.asyncio import serve
from hypercorn.config import Config
# from hypercorn.logging import Logger as HypercornLogger


async def main(app, config):
    return await serve(app, config)