#!/usr/bin/env python3
#
"""
- This python file
- Lecture 1
- Baisc python
"""
# 0x 2425
# +-----+
# |  4  | <- x
# +-----+
# var_1 = 1
# var_2 = 2
# var_3 = 3
# var_4 = 4
# var_5 = 5
# total = var_1 + var_2 + var_3
# # print(total)
# # # multi line
# total = var_1 + \
#         var_2 + \
#         var_3

# print(total)
# x = '4'
# print(type(x))
# x = 4
# print(type(x))
# x = 5.0
# print(type(x))
# x = 2j
# print(type(x))

# twice line
# input('\n\n Press the enter key to exist')

# diff type
# counter = 100
# miles = 100.0
# name = 'iti'
# print(type(counter))
# print(type(miles))
# print(type(name))

'''
variables
'''
# multi assign
# a=b=c=1
# a,b,c = 'ahmed', 'iti', 41
# x = 'ITI'
# # print('welcome ' + x)
# # #
# y = ' 41'
# #
# z = x + y
# # #
# print(z)
#
#
# x = 5
# y = 10
# print(x+y)
#
# # make error
# x = 5
# y = "BI"
# print(x+y)

# x = 5
# print(x)
# del x
# print(x)

# Numbers
# x = 1
# y = 2.8
# z = 1j
# print(type(x))
# print(type(y))
# print(type(z))

# casting numbers
#
# x = int(1)
# y = int(2.8)
# z = int("3")

# # float
# x = float(1) # casting float
# y = float(2.8)
# z = float("3")
# w = float("4.2")
# print(x)
# print(y)
# print(z)
# print(w)
#
# # casting string
# x = str("s1")
# y = str(2)
# z = str(3.0)
# print(type(x))
# print(type(y))
# print(type(z))
# print(x, y, z)
# some built-in method

# print(pow(2, 2))
# print(abs(-1))
# print(max(3, 2))
# print(min(3, 2))
# print(round(3.2))
# print(round(3.5))

# string
# welcome = "Welcome Python Course"
# print(welcome)
# print(welcome[0])
#[start:stop-1]
# +--+---+
# |w | e |
# +--+---+
# 0  1   2
# #  0   1
# print(welcome[1:5])

# updating strings
#
# print(welcome[:15] + 'BI')


# special operators in string

# x = '***ITI***'
# print(x*3)
#
# print('A' in 'ahmed')
# print('A' not in 'ahmed')
# print('a' is 'a')
# print('a' == 'a')
# print(str(4))

# string formatting (embded string)
# #%s -> string, %d -> integer
# # name = 'Ahmed'
# # age = 33
# # print('My name is %s and age is %d years old' % (name, age))
# # print('My name is {0} and age is {1} years old is {1}'.format(name, age))
# name = 'Ahmed'
# age=32
# print(f'My name is {name} and age is {age} years old')
#https://realpython.com/python-f-strings/

# docs = """Hello ITI
# this test doc string
# """
# print(docs)

#string operator

# x = eval(input('Enter any Thing'))
# x = input('Entery A number \n')
# print('x===', type(x))
# my_str = 'ITI track Bi'
# # print(len(my_str))
# # print(my_str.lower())
# # print(my_str.upper())
# # print(my_str.isalpha())
# my_str = '2'
# print(my_str.isdigit())
#
'''
collection
'''
# # list
# my_list = []
my_list = [10, 'ahmed', ['iti', 'BI']]
# my_list2 = [1,2,3,4,7,6]
# print(my_list[2][0])
# print(my_list2[1:5])
# print(my_list[2][0])
# # updating list
lis = ['apple', 'banana', 'cherry']
# print(lis)
# lis[1] = 'blue-berry'
# print(lis)
# del lis[1]
# print(lis)
#
# #list operation
# print(len(my_list))
# l = [1,2,3,4] + ['5','6',7]
# print(l)
# print(['hi'] * 4)
# print(5 in [1, 2, 3, 5])
# # iteration
# # for loop
# x = 2
# my_list = [1, 1]
# my_list.append(x)
# print(my_list)
# print(my_list.count(2))
# my_list = [1, 2]
# my_list2 = ['A', 'B', 'ITI']
# # li = [5, 3]
# my_list.extend(my_list2)
# # my_list.extend(li)
# print(my_list)
#
# my_list = [ 'a', 'b', 'c', 'a']
# # my_list.insert(0, 10)
# # print(my_list)
# # print(my_list)
# # my_list.pop()
# # x = my_list.pop()
# # print(my_list)
# # print(x)
# # my_list.append('a')
# # print(my_list)
# # my_list.remove('a')
# #
# # my_list.reverse()
# # print(my_list)
# #
# my_list = [10, 9, 8]
# my_list.sort()
# print(my_list)
# # len(my_list)
# # constructor list()
#
#
# '''
# Tuples
# '''
#
tup = ()
# tup = ('ahmed', 'iti', 'sys', 1, )
# print(tup[1])
# tup[0] = 100
# del tup[1]
# print(tup)
# del tup
# print(tup)
# tup = ()
#
# x = ("2", "3", "4",)
# # print(x)
# y = tuple(('e'))
# print(y)
# cmp(x, y)

# print(len(x))
# print(max((3, 4)))
# print(min((2, 5)))
# tup = (3, 4,5)
# tup = list(tup)
# print(tup)
# tup[0] = 'ITI'
# tup = tuple(tup)
# print(tup)
# x = [3]
# print(x)
# tuple(x)
# print(tuple(x))
#
# '''
# Set
# '''
sets = {'ahmed', '23', 2}
# acccess by looping
# can not change but can add new item by add
# sets.add('ITI') # one item
# print(sets)
# sets.update(['2', 'ax', 'az']) # more item
# print(sets)

# print(sets[0])

#
# print(len(sets))
# #
# sets.remove('2')
# sets.discard(2)
# print(sets)

# st = {'12', '13', '14', '14'}
# # st.clear()
# # print(st)
# del st
# print(st)
# # set()
# {'ahmed', 'iti'}
# dict
# dict = {
#     'Track': 'BI',
#     'Course': 'Python',
#     'Intake': '41'
# }
# dict = {'Track':{
#     'Names':['Ahmed', 'Nagham', 'Mona', 'Adel'],
#     'Course':('MySQl', 'Python', 'Node',),
#     'grade':[{
#         'names': ['Ahmed'],
#         'ages': [30]
#     },
#              {
#         'Ahmed': 'A',
#         'Adel': 'B',
#         'Mona': 'A',
#         'Hamada': 'c'
#     }, {
#         'A': 'MySql',
#         'B': 'Python',
#         'C': 'Node'
#     }]
# }}
# print('dict = ', dict)
# grade = dict['Track']['grade']
# print('grade =', grade)
# grade_ahmed = grade[1]['Ahmed']
# print('Ahmed Grade =', grade_ahmed)
# print('Course Grade', grade[0][grade_ahmed])
# course = grade[2][grade_ahmed]
# print(f"Ahmed Grad = {grade_ahmed} in Course {course}")
# print(dict['course'])
# print(dict.get('intake'))
# dict['Track']
# # dict.get('Track')
# #
# dict['Intake'] = 42
# # #
# print(dict)
# print(dict.get('Intake'))
# dict = {
#     '1':'noha',
#     '2': [1, 2,3, 4,],
#     'result':{
#         'k': 'v',
#         'k2': ['v']
#     }
# }
# dic = {
#     'Track': 'BI',
#     "Courses":['Python', 'Mysql'],
#     'students':{
#         "grade": ['A', 'B', 'C', 'F'],
#         "Names":{'Mahmoude': "A", "Bakr": "B"}
#     }
# }
# print(dic['students']['Names']['Mahmoude'])
# print(dic['students']['grade'][2])
# print(dic['Courses'][1])
# print(dict['result']['k2'][0])
# print(dict['result']['k2'][0])
# dic.clear()
# print(dic)
# d1 = dict.copy()
# print(d1)
# print(dict.items())
# print(dict.keys())
# print(dict.values())
# list_track = []
#
# dict = {
#     'Track': ['BI'],
#     'Course': 'Python',
#     'Intake': '41'
# }
# dict['Track'].append('MEARN')
# list_track.append(dict)
# # dict.update({'Track': 'Mearn',
# #              'Course': 'Node',
# #              'Intake': '42'})
# list_track.append({'Track': 'Mearn',
#              'Course': 'Node',
#              'Intake': '42'})
# print(list_track[0]['Track'])
# print(list_track[1]['Track'])
# print(list_track)
# print(dict)
# dict.popitem()
# print(dict)
# l = ['A', 'A', 'A', 'A', 'B']
# print(set(l))
# self study
# from array import array
# array('i', [1, 2, 3])

# control flow
# if exp
# elif exp
# else
# exp
# and, or
# position = 'Manager'
# age = 20
# if age >= 40 and position == 'Manager':
#     print('salary = 20000')
# elif age<= 30 or position == 'Junior':
#     print('salary = 10000')
# elif age == 50 and position == 'CTO':
#     print('50000')
# else:
#     print('unkwon position')
#


dict = {'Track':{
    'Names':['Ahmed', 'Nagham', 'Mona', 'Adel'],
    'Course':('MySQl', 'Python', 'Node',),
    'grade':[{
        'names': ['Ahmed'],
        'ages': [30]
    },
             {
        'Ahmed': 'A',
        'Adel': 'B',
        'Mona': 'A',
        'Hamada': 'c'
    }, {
        'A': 'MySql',
        'B': 'Python',
        'C': 'Node'
    }]
}}
# dict = {}
if dict and 'Track' in dict:
    get_track = dict['Track']
    if 'grade' in get_track:
        get_grade = get_track['grade']
        if len(get_grade) >= 3:
            student_name = get_grade[0]['names'][0]
            student_grade = get_grade[1][student_name]
            grade_course = get_grade[2][student_grade]
            print(f'Studend Name {student_name}, Student Grade {student_grade}, Course Grade {grade_course}')
        else:
            print('There is missing data')
    else:
        print('missing data grade')

elif dict and 'Result' in dict:
    get_track = dict['Result']
    if 'grade' in get_track:
        get_grade = get_track['grade']
        if len(get_grade) >= 3:
            student_name = get_grade[0]['names'][0]
            student_grade = get_grade[1][student_name]
            grade_course = get_grade[2][student_grade]
            print(f'Studend Name {student_name}, Student Grade {student_grade}, Course Grade {grade_course}')
        else:
            print('There is missing data')
else:
    print('Something Wrong')

# b = False
# z = 'B' if b else 'Not B'
# print(z)
# if x < 0:
#     print('Not allowed')
#     print(f'{x} < 0')
# elif x <= 10:
#     print(x)
# else:
#     print('X greater than 10')
# print('outer x')
# x = True
# # short
# if a > b: print('yes')
# # print('A') if a > b else print('B')
# a = 5 if x else 0
# print(a)
#
#try it
# # 3 conditions in one line
# print('A') if a > b else print('=') if a == b else print('b')

# and or
# if a > b and c > a:
#     print('both')
# if a > b or a > c:
#     print('at least')
#
# lis = ['a', 'v', 'c', 1, ['s', 'x'], {'k': 'v'}]

# for value in lis:
#     print(value)
# dic = {'k': 'v', 'k1':'v1'}
# looping
# for value in lis:
#     print(value)
# for key, value in dic.items():
#     print('key = ', key, 'value = ', value)
# for k , v in dict:
#     print(k, v)
# lis = [1, 2, 'a', 'v', 'b', '7']
# for v in range():
#     print('idx', v, 'value', lis[v])
# # range(start, end, step)
#
# for x in range(4):
#     print(x)
# else:
#     print('f')
# for x in range(5):
#     print('x', x)
#     print('------------')
#     for y in range(3):
#         print('y', y)

# flag = True
# x = 5
# i = 1
# lis = ['a', 'v', 'c']
# while i <= len(lis): # condition
#     print(lis[i])
#     i+=1
# li = ['sara', 'nahla', 'mohamed', 'salem',]
#
# for idx, value in enumerate(li):
#     print(idx, value)


# rev list

# li = []
# li = [1, 'a', [1.0, {'key1': 'val1'}]]
# li.append('ahmed')
# li.insert(0, 'sobhy')
# li2 = (['1', 1], ('a', 'b'),  {'key1': 'val1'})
# # li2.append('ahmed')
# # li2.insert(0, 'sobhy')
# # li2[0] = 'sobhy2'
# li2 = list(li2)
# li2.append('ahmed')
# li2 = tuple(li2)
# print(li2)
# #

# def greeting():
#     print('Hello')
#
# greeting()

# def take_input_from_user(dispaly_message):
#     take_input = input(dispaly_message + '\n')
#     return take_input
#
# print(take_input_from_user('please enter number'))
# print(take_input_from_user('please enter your name'))

def func():
    print('ex')
#
def my_func(x=0):
    return x
def my_func(x):
    return x
#
def my_func(*args):
    for val in args:
        print(val)
#
def my_func(var, *args):
    print(var)
    for val in args:
        print(val)
