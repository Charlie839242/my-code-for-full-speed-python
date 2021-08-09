# code:utf-8

# 1
# Create a list named “l” with the following values ([1, 4, 9, 10, 23]).
#     solve the following exercises:
#     1. Using list slicing get the sublists [4, 9] and [10, 23].
#     2. Append the value 90 to the end of the list “l”. Check the difference between list
#     concatenation and the “append” method.
#     3. Calculate the average value of all values on the list. You can use the “sum” and
#     “len” functions.
#     4. Remove the sublist [4, 9].
l = [1, 4, 9, 10, 23]
# 1.1
l1 = l[1:3]       # l[n:m]是l[n]到l[m-1]
l2 = l[3:5]
print(l1)
print(l2)
# 1.2
l3 = l + [90]
print(l3)
l.append(90)
print(l)
# 1.3
ave = sum(l)/len(l)
print(ave)
# 1.4
l.remove(4)                            # remove(4)只能移除第一个4
l.remove(9)
print(l)


# 2
#     1. Using list comprehensions, create a list with the squares of the first 10 numbers.
#     2. Using list comprehensions, create a list with the cubes of the first 20 numbers.
#     3. Create a list comprehension with all the even numbers from 0 to 20, and another
#     one with all the odd numbers.
#     4. Create a list with the squares of the even numbers from 0 to 20, and sum the list
#     using the “sum” function. The result should be 1140. First create the list using list
#     comprehensions, check the result, then apply the sum to the list comprehension.
#     5. Make a list comprehension that returns a list with the squares of all even numbers
#     from 0 to 20, but ignore those numbers that are divisible by 3. In other words,
#     each number should be divisible by 2 and not divisible by 3. Search for the “and”
#     keyword in the Python documentation. The resulting list is [4, 16, 64, 100, 196, 256]
# 2.1
x1 = [x*x for x in range(10)]       # range function: range(10)=range(0,10)=[0,1,2,...9],range(1,10)=[1,2,3...9]
print(x1)                           # range(0,10,3)=[0,3,6,9],range[0,-10]=[0,-1,-2...-9]
                                    # 注意 range返回的是一个对象，无法打印
# 2.2
x2 = [x**3 for x in range(20)]
print(x2)
# 2.3
x3 = [x for x in range(20) if(x % 2 == 0)]
x4 = [x for x in range(20) if(x % 2 != 0)]
print(x3)
print(x4)
# 2.3-solution-2
x7 = [x for x in range(0, 20, 2)]
print(x7)
x8 = [x for x in range(1, 20, 2)]
print(x8)
# 2.4
x5 = [x*x for x in range(20) if(x % 2 == 0)]
print(x5)
sum_x5 = sum(x5)
print(sum_x5)
# 2.5
x6 = [x*x for x in range(20) if((x % 2 == 0)and(x % 3 != 0))]
print(x6)

