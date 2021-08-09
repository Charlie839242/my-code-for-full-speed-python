# code:utf-8

# 1. Initialize the string “abc” on a variable named “s”:
#     1. Use a function to get the length of the string.
#     2. Write the necessary sequence of operations to transform the string “abc” in
#     “aaabbbccc”. Suggestion: Use string concatenation and string indexes.
s = 'abc'
print(len(s))
s1 = (s[0]*3)+(s[1]*3)+(s[2]*3)
s2 = '{0}{0}{0}{1}{1}{1}{2}{2}{2}'.format('a','b','c')          # '{},{},{},{},......'.format('','','')
print(s1)
print(s2)


# 2. Initialize the string “aaabbbccc” on a variable named “s”:
#     1. Use a function that allows you to find the first occurence of “b” in the string,
#     and the first occurence of “ccc”.
#     2. Use a function that allows you to replace all occurences of “a” to “X”, and
#     then use the same function to change only the first occurence of “a” to “X”.
# solution 1
s = 'aaabbbccc'
number = 0
x = 1
y = 1
z = 0
for each in s:
    if (each == 'b') and (x == 1):
        x = 0
        print ('s[', number, '] is the first b')
    if (each == 'c') and (y == 1):
        z = z + 1
        if (z == 3):
            y = 0
            print('s[',number-2, ']is the first ccc')
    number = number + 1
# solution 2
s = 'aaabbbccc'
print(s.find('b'))
print(s.find('ccc'))
print(s.find('a'))
print(s.replace('a', 'X'))          # 没有第三个参数代表全部替换
print(s.replace('a', 'X', 1))

# 3. Starting from the string “aaa bbb ccc”, what sequences of operations do you need
# to arrive at the following strings? You can use the “replace” function.
#     1. “AAA BBB CCC”
#     2. “AAA bbb CCC”
s = 'aaa bbb ccc'
s1 = s.replace('a','A').replace('b','B').replace('c','C')
print(s1)
s2 = s.upper()                  # upper可以把字符串转化成大写,大写字母，数字，符号等保持不变
print(s2)
s3 = s1.replace('B','b')
print(s3)
print(s)


