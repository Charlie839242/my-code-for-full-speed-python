# code:utf-8

# generator is in the form of a funciton, iterator is in the form of a class

# 1.
#     1. Implement a generator called “squares” to yield the square of all numbers from (a)
#     to (b). Test it with a “for” loop and print each of the yielded values.
#     2. Create a generator to yield all the even numbers from 1 to (n).
#     3. Create another generator to yield all the odd numbers from 1 to (n).
#     4. Implement a generator that returns all numbers from (n) down to 0.
#     5. Create a generator to return the fibonnaci sequence starting from the first element
#     up to (n). The first numbers of the sequence are: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,
#     89, . . .
#     6. Implement a generator that returns all consecutive pairs of numbers from 0 to (n),
#     such as (0, 1), (1, 2), (2, 3). . .
# 1.1
# Implement a generator called “squares” to yield the square of all numbers from (a)
# to (b). Test it with a “for” loop and print each of the yielded values.
def squares(a,b):
    if(a > b):
        raise StopIteration
    while(a <= b):
        yield a**2
        a = a + 1
for each in squares(0,10):
    print(each,end=' ')
print('')

# 1.2
# Create a generator to yield all the even numbers from 1 to (n).
def even(a,b):
    if(a > b):
        StopIteration
    while(a <= b):
        if(a % 2 == 0):
            yield a
            a = a + 2
        else:
            a = a + 1
for each in even(1,10):
    print(each, end=' ')
print('')

# 1.3
# Create another generator to yield all the odd numbers from 1 to (n).
def odd(a,b):
    if(a > b):
        StopIteration
    while(a <= b):
        if(a % 2 == 1):
            yield a
            a = a + 2
        else:
            a = a + 1
for each in odd(1,10):
    print(each, end=' ')
print('')

# 1.4
# Implement a generator that returns all numbers from (n) down to 0.
def dec(a,b):
    if(a < b):
        raise StopIteration
    while(a >= b):
        yield a
        a = a - 1
for each in dec(10,0):
    print(each, end=' ')
print('')

# 1.5
# Create a generator to return the fibonnaci sequence starting from the first element
# up to (n). The first numbers of the sequence are: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, . . .
def fibo(n):
    first = 0
    second = 1
    number = 0
    if(n < 0):
        StopIteration
    while(n >= 0):
        if(number == 0):
            yield 0
            number = number + 1
            n = n - 1
        elif(number == 1):
            yield 1
            number = number + 1
            n = n - 1
        else:
            third = first + second
            first = second
            second = third
            yield second
            number = number + 1
            n = n - 1
for each in fibo(10):
    print(each, end=' ')
print('')

# 1.6
# Implement a generator that returns all consecutive pairs of numbers from 0 to (n), such as (0, 1), (1, 2), (2, 3). . .
def consec(n):
    if(n < 0):
        StopIteration
    number = 0
    while(n >= 0):
        yield (number, number + 1)
        number = number + 1
        n = n - 1
for each in consec(10):
    print(each, end=' ')
print('')


