from hypercorn.asyncio import serve
from hypercorn.config import Config
# from hypercorn.logging import Logger as HypercornLogger


async def main(app, config, shutdown_trigger):
    return await serve(app, config, shutdown_trigger=shutdown_trigger)