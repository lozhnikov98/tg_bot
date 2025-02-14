import asyncio

from bot import dp, bot
from hendlers import *


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
