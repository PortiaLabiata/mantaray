import asyncio
import time

async def greet(name: str):
    print(f'Hello, {name}!')
    await asyncio.sleep(5)
    return 42

async def bye(name: str):
    print(f'Bye, {name}')
    await asyncio.sleep(5)
    return 69

async def factorial(n: int):
    await asyncio.sleep(1)
    print(f'Factorial running, {n}')
    return n*(await factorial(n-1)) if n > 0 else 1

async def c(n: int, k: int):
    a = asyncio.create_task(factorial(n))
    b = asyncio.create_task(factorial(k))
    c = asyncio.create_task(factorial(n-k))
    await asyncio.gather(a, b, c)
    return a.result() // (b.result() * c.result())

def _factorial(n: int):
    return n*_factorial(n-1) if n > 0 else 1

def _c(n: int, k: int):
    return _factorial(n) // (_factorial(k) * _factorial(n-k))

async def very_long_task(delay):
    asyncio.sleep(delay)

async def main():
    '''
    task1 = asyncio.create_task(greet('God'))
    task2 = asyncio.create_task(bye('God'))

    await task1
    await task2

    print(f'Task 1 completed and returned {task1.result()}')
    print(f'Task 2 completed and returned {task2.result()}')

    '''
    #print(await c(100, 20))
    '''
    print(f"Started at {time.strftime('%X')}")
    print(await c(5, 3))
    print(f"Started at {time.strftime('%X')}")
    '''
    try:
        async with asyncio.timeout(5):
            await very_long_task(2)
    except TimeoutError:
        print('Task was cancelled due to timeout :(')
    finally:
        print('Anyway, bye!')


asyncio.run(main())
