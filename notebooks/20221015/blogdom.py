#!/usr/bin/env python3
import asyncio
import socket
from keyword import kwlist

MAX_KEYWORD_LEN = 4  # limit length of keyword to use for our domain names


async def probe(domain: str) -> tuple([str, bool]):  # returns a tuple with ddomain name and boolean
    loop = asyncio.get_running_loop()  # retrieve a reference to the event loop
    try:
        await loop.getaddrinfo(domain, None)  # returns a 5-part tuple to connect to the given address using a socket.
    except socket.gaierror:
        return (domain, False)
    return (domain, True)


async def main() -> None:  # must be a coroutine
    names = (kw for kw in kwlist if len(kw) <= MAX_KEYWORD_LEN)  # Generator to yield Python keywords 
    domains = (f'{name}.dev'.lower() for name in names)  # Generator to yield domain names
    coros = [probe(domain) for domain in domains]  # Build a list of coroutine objects.
    for coro in asyncio.as_completed(coros):  # asyncio.as_completed is a generator that yields coroutines in the order they are completed
        domain, found = await coro  # await will not block, as the coroutines are completed.
        mark = '+' if found else ' '
        print(f'{mark} {domain}')


if __name__ == '__main__':
    asyncio.run(main())  # starts the event loop
