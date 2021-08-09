# code:utf-8

# The example in the book:
# 在square函数中，若执行三次，按照同步执行，会等待3s，但异步执行只需要1s
# import asyncio
# async def square(x):
#     print('Square', x)
#     await asyncio.sleep(1)
#     print('End square', x)
#     return x * x
# # 创建一个事件循环。
# loop = asyncio.get_event_loop()              # loop类似一个专为异步执行设置的调度器
# # 执行异步函数直到其完成。
# results = loop.run_until_complete(asyncio.gather(square(1), square(2), square(3)))
# print(results)

# 1.
#     1. Implement an asynchronous coroutine function to add two variables and sleep for
#     the duration of the sum. Use the asyncio loop to call the function with two numbers.
#     2. Change the previous program to schedule the execution of two calls to the sum
#     function.
# 1.1
# Implement an asynchronous coroutine function to add two variables and sleep for
# the duration of the sum. Use the asyncio loop to call the function with two numbers.
import asyncio
async def add(a,b):
    print('add', a, b)
    print('executing time is %d s' % (a+b))
    await asyncio.sleep(a + b)
    print('end add', a, b)
    return a + b

loop = asyncio.get_event_loop()
results = loop.run_until_complete(asyncio.gather(add(0, 1)))    # 多个loop.run_until_complete之间是同步的，每个loop.run_until_complete之间是异步的
print(results)

# 1.2
# Change the previous program to schedule the execution of two calls to the sum function.
results = loop.run_until_complete(asyncio.gather(add(0, 1), add(1, 2), add(2, 3)))
print(results)