# code:utf-8

# 1.
#     1. Implement an iterator class to return the square of all numbers from “a” to “b”.
#     2. Implement an iterator class to return all the even numbers from 1 to (n).
#     3. Implement an iterator class to return all the odd numbers from 1 to (n).
#     4. Implement an iterator class to return all numbers from (n) down to 0.
#     5. Implement an iterator class to return the fibonnaci sequence from the first element
#     up to (n). You can check the definition of the fibonnaci sequence in the function’s
#     chapter. These are the first numbers of the sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34,
#     55, 89, . . .
#     6. Implement an iterator class to return all consecutive pairs of numbers from 0 until
#     (n), such as (0, 1), (1, 2), (2, 3). . .
# 1.1
# Implement an iterator class to return the square of all numbers from “a” to “b”.
class Square:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __iter__(self):
        return self
    def __next__(self):
        if(self.a > self.b):
            raise StopIteration
        else:
            value = self.a
            self.a = self.a + 1
            return (value ** 2)
square = Square(1, 10)
for each in square:
    print(each,end=' ')

# 1.2
# Implement an iterator class to return all the even numbers from 1 to (n).
class Even:
    def __init__(self, m, n):
        self.start = m
        self.end = n
    def __iter__(self):
        return self
    def __next__(self):
        if(self.start > self.end):
            raise StopIteration
        else:
            if(self.start % 2 != 0):
                self.start = self.start + 1
            start = self.start
            self.start = self.start + 2
            return start
even = Even(1, 20)
print('')
for each in even:
    print(each, end=' ')


# 1.3
# Implement an iterator class to return all the odd numbers from 1 to (n).
class Odd:
    def __init__(self, m, n):
        self.start = m
        self.end = n
    def __iter__(self):
        return self
    def __next__(self):
        if(self.start > self.end):
            raise StopIteration
        else:
            if(self.start % 2 == 0):
                self.start = self.start + 1
            start = self.start
            self.start = self.start + 2
            return start
odd = Odd(1,20)
print('')
for each in odd:
    print(each, end=' ')


# 1.4
# Implement an iterator class to return all numbers from (n) down to 0.
class Dec:
    def __init__(self, m, n):
        self.start = m
        self.end =n
    def __iter__(self):
        return self
    def __next__(self):
        if(self.start < self.end):
            raise StopIteration
        else:
            value = self.start
            self.start = self.start - 1
            return value
dec = Dec(10,0)
print('')
for each in dec:
    print(each, end=' ')


# 1.5
# Implement an iterator class to return the fibonnaci sequence from the first element
class Fibonnaci:
    def __init__(self, n):
        self.n = n
        self.m = 0
        self.first = 0
        self.second = 1
    def sort(self,third):                           # first+second得到third后移到second
        self.first = self.second
        self.second = third
    def __iter__(self):
        return self
    def __next__(self):
        if(self.n > 0):
            if(self.m == 0):
                self.m = self.m + 1
                self.n = self.n - 1
                return 0
            elif(self.m == 1):
                self.m = self.m + 1
                self.n = self.n - 1
                return 1
            else:
                third = self.first + self.second
                self.sort(third)
                self.m = self.m + 1
                self.n = self.n - 1
                return self.second
        else:
            raise StopIteration
fib = Fibonnaci(10)
print('')
for each in fib:
    print(each, end=' ')


# 1.6
# Implement an iterator class to return all consecutive pairs of numbers from 0 until (n), such as (0, 1), (1, 2), (2, 3). . .
class Consec:
    def __init__(self,n):
        self.end = n
        self.start = 0
    def __iter__(self):
        return self
    def __next__(self):
        if(self.end > -1):
            value = self.start
            self.start = self.start + 1
            self.end = self.end - 1
            return (value, value + 1)
        else:
            raise  StopIteration
consec = Consec(10)
print('')
for each in consec:
    print(each, end=' ')








