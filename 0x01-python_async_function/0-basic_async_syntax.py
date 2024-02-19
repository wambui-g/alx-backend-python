#!/usr/bin/env python3
"""asynchronous coroutine that takes an integer arguement, waits for random delat then returns"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Waits for a random number of seconds.
    '''
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
