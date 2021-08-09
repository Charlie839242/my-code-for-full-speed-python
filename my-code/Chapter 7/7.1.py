# code:utf-8

# 1.
#     Take the following Python dictionary:
ages = {
"Peter": 10,
"Isabel": 11,
"Anna": 9,
"Thomas": 10,
"Bob": 10,
"Joseph": 11,
"Maria": 12,
"Gabriel": 10,
}
#     1. How many students are in the dictionary? Search for the “len” function.
#     2. Implement a function that receives the “ages” dictionary as parameter and returns
#     the average age of the students. Traverse all items on the dictionary using the
#     “items” method as above.
#     3. Implement a function that receives the “ages” dictionary as parameter and returns
#     the name of the oldest student.
#     4. Implement a function that receives the “ages” dictionary and a number “n” and
#     returns a new dict where each student is (n) years older. For instance, new_ages(ages,
#     10) returns a copy of “ages” where each student is 10 years older.
# 1.1
print(len(ages))
# 1.2
def average(dict):
    sum = 0
    for name,age in dict.items():
        sum = sum + age
    return sum/len(dict)
print(average(ages))
# 1.3
def max_index(dict):
    list1 = []
    list2 = []
    for name, age in dict.items():
        list1.append(age)
        list2.append(name)
    return list2[list1.index(max(list1))]           # max找到最大值，index找到最大索引，
print(max_index(ages))
# 1.4
def ten_year(dict):
    for name, age in dict.items():
        dict[name] = dict[name] + 10
    return dict
print(ten_year(ages))


# 2.
#     Take the following dictionary:
students = {
"Peter": {"age": 10, "address": "Lisbon"},
"Isabel": {"age": 11, "address": "Sesimbra"},
"Anna": {"age": 9, "address": "Lisbon"},
}
#     1. How many students are in the “students” dict? Use the appropriate function.
#     2. Implement a function that receives the students dict and returns the average age.
#     3. Implement a function that receives the students dict and an address, and returns a
#     list with names of all students whose address matches the address in the argument.
#     For instance, invoking “find_students(students, ’Lisbon’)” should return Peter and
#     Anna.
# 2.1
print(len(students))
# 2.2
def average2(dict):
    sum = 0
    for name,info in dict.items():
        sum = sum + info['age']
    return sum/len(dict)
print(average2(students))
# 2.3
def find_students(dict, address):
    m = 0
    names = []
    for name, info in dict.items():
        if(info['address'] == address):
            names.append(name)
            m = m + 1
    if(names == []):
        return False
    return names
print(find_students(students,'Lisbon'))













