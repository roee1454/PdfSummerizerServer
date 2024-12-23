import asyncio
from services.net.socket import init_socket


if __name__ == "__main__":
    asyncio.run(init_socket())
