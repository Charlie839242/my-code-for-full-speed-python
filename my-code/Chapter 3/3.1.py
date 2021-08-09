# coding:utf-8

# # 1
# Try the following mathematical calculations and guess what is happening: ((3 / 2)),((3 // 2)), ((3 % 2)), ((3**2)).
print(3/2)
print(3//2)                                 # 向下取整
print(3%2)                                  #
print(3**2)                                 # 3^2
print(divmod(3,2))                          # 输出(x,y), x=3//2, y=3%2


# 2
# Calculate the average of the following sequences of numbers: (2, 4), (4, 8, 9), (12,14/6, 15)
x = [2, 4]                                  # 一维数组相加后还是一维数组
y = [4, 8, 9]
z = [12, 14/6, 15]
print(x)

sum = 0
a = x+y+z
print(a)
for each in a:
    sum = sum + each
ave = sum/len(a)
print(ave)


# 3
# The volume of a sphere is given by (4/3 * pi * rˆ3). Calculate the volume of a sphere of radius 5. Suggestion: create a variable
# named “pi” with the value of 3.1415
pi = 3.1415
r = 5
volume = 4 / 3 * (pi * (r**3))
print(volume)


# 4
# Use the modulo operator (%) to check which of the following numbers is even or odd: (1, 5, 20, 60/7).
x = [1, 5, 20, 60/7]
for each in x:
    if (each % 2 == 0):
        print("even")
    elif (each % 2 == 1):
        print("odd")
    else:
        print("Neither")


# 5
# Find some values for (x) and (y) such that (x < 1/3 < y) returns “True” on the Python REPL. Suggestion: try (0 < 1/3 < 1) on the REPL
print(0 < 1/3 < 1)