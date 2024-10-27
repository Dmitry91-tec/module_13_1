import asyncio
import time


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for j in range(1,shar+1):
        await asyncio.sleep(1/power)
        print(f'Силач {name} поднял {j}')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    print('Начало соревнований')
    task1 = asyncio.create_task(start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task1
    await task2
    await task3
    print('Конец соревнований')


shar = 5
start = time.time()
asyncio.run(start_tournament())
finish = time.time()