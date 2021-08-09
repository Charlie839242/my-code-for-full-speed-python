# code:utf-8

# 1. Exercise with the for loop
#     1. Create a function “add” that receives a list as parameter and returns the sum of all
#     elements in the list. Use the “for” loop to iterate over the elements of the list.
#     2. Create a function that receives a list as parameter and returns the maximum value
#     in the list. As you iterate over the list you may want to keep the maximum value
#     found so far in order to keep comparing it with the next elements of the list.
#     3. Modify the previous function such that it returns a list with the first element being
#     the maximum value and the second being the index of the maximum value in the
#     list. Besides keeping the maximum value found so far, you also need to keep the
#     position where it occurred.
#     4. Implement a function that returns the reverse of a list received as parameter.
#     You may create an empty list and keep adding the values in reversed order as
#     they come from the original list.
#     5. Make the function “is_sorted” that receives a list as parameter and returns True if
#     the list is sorted in ascending order. For instance [1, 2, 2, 3] is ordered while [1, 2, 3,
#     2] is not. Suggestion: you have to compare a number in the list with the next one,
#     so you can use indexes or you need to keep the previous number in a variable as
#     you iterate over the list.
#     6. Implement the function “is_sorted_dec” which is similar to the previous one but
#     all items must be sorted by decreasing order.
#     7. Implement the “has_duplicates” function which verifies if a list has duplicate values.
#     You may have to use two “for” loops, where for each value you have to check for
#     duplicates on the rest of the list
# 1.1
def add(list):
    sum = 0;
    for element in list:
        sum = sum + element
    return sum
print(add([1,2,3]))
# 1.2
def max(list):
    if(list == []):
        return False
    else:
        max = list[0]
        for element in list:
            if(element > max):
                max = element
        return max
print(max([4,1,2,7,9]))
# 1.3
def max_index(list):
    if(list == []):
        return False
    else:
        max = list[0]
        index = 0
        for number,element in enumerate(list):
            if(element > max):
                max = element
                index = number
        return [max, index]
print(max_index([4,1,2,7,9]))
# 1.4
def reverse(list):
    if(list == []):
        return []
    else:
        rev = []
        for i in range(len(list)):
            rev.append(list[len(list)-i-1])
        return rev
print(reverse([4,1,2,7,9]))
# 1.5
def is_sorted(list):
    if(len(list) == 0 or len(list) == 1):
        return False
    else:
        for i in range(1,len(list)):
            while list[i] < list[i-1]:
                return False
        return True
print(is_sorted([0,1,2,3,2]))
print(is_sorted([0,1,2,3,4]))
# 1.6
def is_sorted_dec(list):
    if (len(list) == 0 or len(list) == 1):
        return False
    else:
        for i in range(1, len(list)):
            while list[i] > list[i - 1]:
                return False
        return True
print(is_sorted_dec([4,3,2,1]))
print(is_sorted_dec([9,5,2,7]))
# 1.7
def has_duplicates(list):
    if(list == []):
        return False
    else:
        duplicate = []
        for m,n in enumerate(list):
            for q in list[m+1:len(list)]:
                if q == n:
                    if((list == [])or(element != q for element in duplicate)):
                        duplicate.append(q)
        return duplicate
print(has_duplicates([1,1,2,2,3,4,4,5]),'are duplicate numbers')


# 2.
#     1. Implement a function that receives a number as parameter and prints, in decreasing
#     order, which numbers are even and which are odd, until it reaches 0.
def even_odd(n):
    result = []
    for x in range(n,-1,-1):
        result.append(x)
        if(x % 2 == 0):
            result.append('even')
        else:
            result.append('odd')
    return result
print(even_odd(10))


















