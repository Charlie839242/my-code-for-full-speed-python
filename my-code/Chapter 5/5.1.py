# code:utf-8

# # 1.
#     1. Find the greatest common divisor of the following pairs of numbers: (15, 21), (152,
#     200), (1988, 9765).
#     2. Compute the base-2 logarithm of the following numbers: 0, 1, 2, 6, 9, 15.
#     3. Use the “input” function to ask the user for a number and show the result of the
#     sine, cosine and tangent of the number. Make sure that you convert the user input
#     from string to a number (use the int() or the float() function).
# 1.1
import math
x1 = math.gcd(15, 21)          # gcd接受两个参数，返回最大公约数，是greatest common divisor缩写
x2 = math.gcd(152, 200)
x3 = math.gcd(1988, 9765)
print(x1, x2, x3)
# 1.2
# y1 = math.log(0,2)          # first parameter mustn't be zero
y2 = math.log(1, 2)
y3 = math.log(2, 2)
y4 = math.log(6, 2)
y5 = math.log(9, 2)
y6 = math.log(15, 2)
print(y2, y3, y4, y5, y6)
# 1.3
print('Please input a number:')
z = math.radians(float(input()))                    # math接受的都是弧度制，当人输入角度时，应转化成弧度  radians是转弧度，degrees是转角度
                                                    # 对字符串int，float可以转成数字
z1 = math.sin(z)
z2 = math.cos(z)
z3 = math.tan(z)
print('sin(z)=',z1,'cos(z)=',z2,'tan(z)=',z3)


# 2.
#     1. Implement the “add2” function that receives two numbers as arguments and returns
#     the sum of the numbers. Then implement the “add3” function that receives and
#     sums 3 parameters.
#     2. Implement a function that returns the greatest of two numbers given as parameters.
#     Use the “if” statement to compare both numbers.
#     3. Implement a function named “is_divisible” that receives two parameters (named “a”
#     and “b”) and returns true if “a” can be divided by “b” or false otherwise. A number
#     is divisible by another when the remainder of the division is zero. Use the modulo
#     operator (“%”).
#     4. Create a function named “average” that computes the average value of a list passed
#     as parameter to the function. Use the “sum” and “len” functions.
# 2.1
def add2(x, y):
    return x+y
def add3(x, y, z):
    return x+y+z
# 2.2
def compare(x,y):
    if(x > y):
        return x
    else:
        return y
# 2.3
def is_divisible(a,b):
    if(a % b == 0):
        return True
    else:
        return False
# 2.4
def average(list):
    return sum(list)/len(list)


# 3.
#     1. Implement the factorial function and test it with several different values. Cross-check
#     with a calculator.
#     2. Implement a recursive function to compute the sum of the (n) first integer numbers
#     (where (n) is a function parameter). Start by thinking about the base case (the sum
#     of the first 0 integers is?) and then think about the recursive case.
#     3. The Fibonnaci sequence is a sequence of numbers in which each number of the
#     sequence matches the sum of the previous two terms.
#     Check your results for the first numbers of the sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, . . .
# 3.1
def factorial(m):
    if(m == 0):
        return 1
    else:
        return m*factorial(m-1)
print(factorial(5))
# 3.2
def sum(m):
    if(m == 0):
        return 0
    else:
        return m+sum(m-1)
print(sum(100))
# 3.3
def fibonnaci(m):
    if(m == 0):
        return 0
    elif(m ==1):
        return 1;
    else:
        return fibonnaci(m-1)+fibonnaci(m-2)
print(fibonnaci(8))












