#!/usr/bin/env python3
"""Basics of asyncio"""


wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> float:
    """Wait for a random delay between 0 and max_delay seconds"""
    import asyncio
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return delays
