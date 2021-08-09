# code:utf-8

# coroutine is waken by the send(), it is mainly achieved by putting yield on the right of the '='

# 1.
#     1. Create a coroutine named “square” that prints the square of any sent value.
#     2. Implement the “minimize” coroutine that keeps and prints the minimum value that
#     is sent to the function.
# 1.1
# Create a coroutine named “square” that prints the square of any sent value.
import time


def xxx():
    print('square:', end='')
    while True:
        value = yield
        print(value**2)
square = xxx()
next(square)
square.send(3)

# 1.2
# Implement the “minimize” coroutine that keeps and prints the minimum value that is sent to the function.
def xxxx():
    print('min:', end='')
    while True:
        list = yield 50
        print(min(list))
minimum = xxxx()
next(minimum)
minimum.send([2,3,1,7,9])
print('')


# 2.
#     1. Implement a producer-consumer pipeline where the values squared by the producer
#     are sent to two consumers. One should store and print the minimum value sent so
#     far and the other the maximum value.
#     2. Implement a producer-consumer pipeline where the values squared by the producer
#     are dispatched to two consumers, one at a time. The first value should be sent to
#     consumer 1, the second value to consumer 2, third value to consumer 1 again, and
#     so on. Closing the producer should force the consumers to print a list with the
#     numbers that each one obtained.
# 2.1
# Implement a producer-consumer pipeline where the values squared by the producer
# are sent to two consumers. One should store and print the minimum value sent so
# far and the other the maximum value.
def comsumer(name):
    print(name,'ready:')
    try:
        list = []
        while True:
            value = yield
            list.append(value)
            if(name == 'comsumer1'):
                print('The min is %f', min(list))
            if(name == 'comsumer2'):
                print('The max is %f', max(list))
    except GeneratorExit:
        print('%s closed' % name)

def producer(comsumers):
    print('producer ready:')
    try:
        while True:
            value = yield
            for comsumer in comsumers:
                comsumer.send(value**2)
    except GeneratorExit:
        for comsumer in comsumers:
            comsumer.close()
        print('all consumer closed')

com1 = comsumer('comsumer1')
com2 = comsumer('comsumer2')
prod = producer([com1,com2])
next(com1)
next(com2)
next(prod)
prod.send(2)
prod.send(3)
prod.send(1)
prod.send(5)
print('')
# time.sleep(2)               # after 2 seconds, 'GeneratorExit will occur

# 2.2
# Implement a producer-consumer pipeline where the values squared by the producer
# are dispatched to two consumers, one at a time. The first value should be sent to
# consumer 1, the second value to consumer 2, third value to consumer 1 again, and
# so on. Closing the producer should force the consumers to print a list with the
# numbers that each one obtained.
def consumer(name):
    print(name, 'ready:')
    m = 0    # 用来判断是第几个数
    try:
        list1 = []
        list2 = []
        while True:
            value = yield
            if(m % 2 == 0):
                list1.append(value)
            else:
                list2.append(value)
            m = m + 1
    except GeneratorExit:
        if(name == 'consumer1'):
            print(name, ' ',list1)
        if(name == 'consumer2'):
            print(name, ' ', list2)

def producers(consumers):
    print('producer ready:')
    try:
        while True:
            value = yield
            for consumer in consumers:
                consumer.send(value**2)
    except GeneratorExit:
        for consumer in consumers:
            consumer.close()
        print('all consumer closed')

con1 = consumer('consumer1')
con2 = consumer('consumer2')
pro  = producers([con1, con2])
next(pro)
next(con1)
next(con2)
pro.send(0)
pro.send(1)
pro.send(2)
pro.send(3)
pro.send(4)















