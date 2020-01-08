# python basics
# tutorial at youtube
# https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU

# this is a single line comment

"""This is a multiple
comment line example
"""

'''
this is another
multiple comment
line example
'''

print("Hello World")

# range() returns a list
nums = range(10)
# num retruns "range(0,10)"
print ("nums is", nums)
# *num returns 0 1 2 ... 9
print (*nums)
# print the list using ',' as delimiter
print (*nums, sep = ",")

# string list and for loop
strings = [ "one", "two", "three" ]
for i in range(3):
  # print "Item %d: %s" % (i, strings[i])
  print ("strings[i] is " + strings[i])

# string partition() returns a tuple
c = "The man in the moon is made out of green cheese"
cp = c.partition('moon')
print ("cp = ", cp)


# ---------------------------------------------------------------------
# % formatting
# ---------------------------------------------------------------------
format = "My %s Python class is %s! I am %s to be here."
var = ('first', 'great', 'glad')
print (format % var)

# ---------------------------------------------------------------------
# function and doc
# ---------------------------------------------------------------------
def showdoc():
     '''My first function using a docstring

     This function takes no argument and return None
     It prints out a message
     '''
     print ("this is my first documented Python function")
     return

showdoc()
print (showdoc.__doc__)

# you can create another reference to the same function
# now both my_showdoc and showdoc point to the same function
my_showdoc = showdoc
my_showdoc()

# you can delete the reference
del my_showdoc

# ---------------------------------------------------------------------
# function default arguments
# ---------------------------------------------------------------------
def add(a=0, b=0):
     print (a + b)
     return

num1 = 1
num2 = 2
add(num1, num2) # num1 + num2
add(num1)       # num1 + 0
add()           # 0 + 0

# use * to specify that a function can be called with any number of arguments. 
# The function can have regular parameters as well as this special parameter, 
# the extra arguments are placed in a tuple
def add_1(*args):
     print (args[0] + args[1])
     return
print ("calling add_1(*args)")
add_1(num1, num2)


# Any number of argument with **
# Another way to call function with an arbitrary number of arguments is to 
# pass "keyword equals value" pairs when you call the function. This is interpreted 
# as a dictionary. You define the function to take a** argument and you pass it key/value pairs.
# Example,
def add_2(**args):
     print (args["a"] + args["b"])
     return
print ("calling add_2(**args)")
add(a=num1, b=num2)

# ---------------------------------------------------------------------
# PyCharm, community edition
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# data types
# ---------------------------------------------------------------------
name = "Tom"   # string 
age = 50       # integer   
is_male = True # boolean
print("the character name is " + name + ".")
print("the character age is ",age,".")

# ---------------------------------------------------------------------
# string
# ---------------------------------------------------------------------
phrase = "Giraffe Academy"
print(phrase.lower())
# phrase is still "Giraffe Academy"
print(phrase.upper())
print(phrase.isupper())
print(len(phrase))   # length
print(phrase[0])   # the first character
print(phrase.index("G"))   # index of first "G" in the string
print(phrase.index("Acad"))   
# print(phrase.index("z"))   # return -1
print(phrase.replace("Giraffe", "Elephant"))

# ---------------------------------------------------------------------
# number
# ---------------------------------------------------------------------
print(2.09)
print(3 + 4 * 5)   # *, /, +, -, %
my_num = 5
# str() converts a integer to a string
print(str(my_num) + " is my favorite number")
print(abs(-5))    # absolute value
print(pow(5, 2))    # 5^2
print(max(4, 6))   # return 6
print(min(4, 6))   # return 4
print(round(3.2))  # return 3
print(round(3.7))  # return 4

# import more math function
#   from <module> import <function/class/variable...> 
from math import floor, ceil, sqrt
print(floor(3.7))  # return 3
print(ceil(3.1))   # return 4
print(sqrt(36))    # return 6.0

# ---------------------------------------------------------------------
# get the user input
# ---------------------------------------------------------------------
# user_name = input("this is a prompt, enter your name: ")
user_name = "fei"
print("Hello " + user_name)

# by default, input returns a string
# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
num1 = 1
num2 = 2.3
# int() only takes a "integer" string
result = int(num1) + float(num2)
print(result)

# ---------------------------------------------------------------------
# list, use []
# ---------------------------------------------------------------------
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
mixture = ["Kevin", 21, True]
print(friends)
print(friends[0])   # returs the first element - "Kevin"
print(friends[-1])   # returs the last element - "Toby"
# range/slice
# slice format: aList[start:end:step]
# the starting element is included but the ending element is not
print(friends[1:])   # returs "Karen", "Jim", "Oscar", "Toby"
print(friends[2:4])   # returs Jim", "Oscar"
print(friends[0:5:2]) # return "Kevin", "Jim", "Toby"
# reverse a list simply by calling aList[::-1]
print(friends[::-1]) #

# list can be "unpacked" into separate elements
name1, name2 = friends[2:4]
# see f-string for more info
print(f'name1 is {name1}; name2 is {name2}')

# replace "Karen" with "Mike"
friends[1] = "Mike"

# ---------------------------------------------------------------------
# list functions
# ---------------------------------------------------------------------
lucky_numbers = [4, 8, 15, 16, 23, 42]
# concatenate another list
friends.extend(lucky_numbers)
print(friends)
friends.append("Creed")
print(friends)
friends.insert(1, "Kelly")
print(friends)
friends.remove("Jim")
print(friends)
friends.pop() # remove the last element
print(friends)
friends.clear()
print(friends)

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
print(friends.index("Kevin"))

friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
print(friends.count("Jim"))   # return 2

# alphabetic order
friends.sort()
print(friends)

lucky_numbers.reverse()
print(lucky_numbers)

# friends is the copy of friend
friends2 = friends.copy()

# list can contain another list, or tuple
list_1 = [1, 2, 3, 4, 5]
# append a tuple
list_1.append((6, 7))
print('list_1 is {}'.format(list_1))
# append a list
list_1.append([8, 9])
print('list_1 is {}'.format(list_1))

# ---------------------------------------------------------------------
# zipping
# ---------------------------------------------------------------------
# Zip function creates an iterator that aggregates elements from multiple lists. 
# It allows traversing lists in parallel in a for-loop and sorting in parallel. 
# It can be unzipped using an asterisk.
numList = [0, 1, 2]
engList = ['zero', 'one', 'two']
espList = ['cero', 'uno', 'dos']
print ('zipping:')
# zip returns a zip object
# e.g. <zip object at 0x000001941AB40908>
print(zip(numList, engList, espList))
print(list(zip(numList, engList, espList)))
# [(0, 'zero', 'cero'), (1, 'one', 'uno'), (2, 'two', 'dos')]

for num, eng, esp in zip(numList, engList, espList):
    print(f'{num} is {eng} in English and {esp} in Spanish.')
# 0 is zero in English and cero in Spanish.
# 1 is one in English and uno in Spanish.
# 2 is two in English and dos in Spanish.

Eng = list(zip(engList, espList, numList))
Eng.sort() # sort by engList
# unzipped using an asterisk.
print ('unzipping:')
a, b, c = zip(*Eng)

print(a)
print(b)
print(c)
# ('one', 'two', 'zero')
# ('uno', 'dos', 'cero')
# (1, 2, 0)


# ---------------------------------------------------------------------
# tuple, use ()
# ---------------------------------------------------------------------
# tuple is like a list, but immutable, can't be modified once created
coord = (4, 5, 6)
print (coord[0])  # return 4
# coord[1] = 6    # python will error out

# list of tuples
listu = [(1, 2), (3, 4), ('a', 'b')]
# unpacking
for lisa, lisb in listu:
    print(lisa, lisb)

# ---------------------------------------------------------------------
# functions
# ---------------------------------------------------------------------
def cube(num):
    return num*num*num

result = cube(4)
print(result)

# ---------------------------------------------------------------------
# if statement
# ---------------------------------------------------------------------
is_male = False
is_tall = True

if is_male:
    print("you are a male")
else:
    print("you are not a male")

# another keyword is "and"
if is_male and is_tall:
    print("you are a tall male")
elif is_male and not(is_tall):
    print("you are a short male")
else:
    print("you are not a male")

# comparison in if statment
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3, 4, 5))

# another example for comparison in if statement
# num1 = float(input("Enter first numer: "))
# op = input("Enter operator: ")
# num2 = float(input("Enter second numer: "))
num1 = 1.2
op = "+"
num2 = 2.3

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("invalid operator")

# ---------------------------------------------------------------------
# dictionaries (key-value pairs), use {}
# ---------------------------------------------------------------------
# keys have to be unique
monthConvert = {
    "Jan": "January",
    "Feb": "Feburary",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
}

print(monthConvert["Mar"])       # return "March"
print(monthConvert.get("Mar"))   # return "March"
# get() can have a default value, if the key doesn't exist
print(monthConvert.get("Luv", "Not a valid key"))   

# ---------------------------------------------------------------------
# while loop
# ---------------------------------------------------------------------
i = 1
while i <= 10:
    print (i)
    i = i + 1   # or "i += 1"
print ("done with loop")

# ---------------------------------------------------------------------
# for loop
# ---------------------------------------------------------------------
# loop over a string
for letter in "Giraffe Academy":
    print(letter)

# loop over a list
friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
    print(friend)

# loop over a number range
for index in range(10):    # 0 - 9, 10 will not be included
    print(index)
for index in range(3, 10): # 3 - 9
    print(index)

for index in range(len(friends)):
    print(friends[index])

# exponent function
print (2**3)   # 2^3

# two dimentinal list
# each element in the list is a list
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print (number_grid[1][1])   # return 5

# nested for loop to interate through two dimentional list
for row in number_grid:
    for col in row:
        print (col)

# ---------------------------------------------------------------------
# exercise: "translator"
# ---------------------------------------------------------------------
# Giraffe Language
# vowels -> g (e.g. dog -> dgg)
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":    # or letter.lower() in "aeiou"
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

# print (translate(input("Enter a phrase: ")))

# ---------------------------------------------------------------------
# try/except block
# ---------------------------------------------------------------------
try:
    value = 10/0
    num1 = int(input('Please enter a number:'))
    print(num1)
except ZeroDivisionError:
    print("Divided by zero")
except ValueError as err:
    print("Invalid input " + err)
except:
    print("other exceptions")


# ---------------------------------------------------------------------
# file IO
# ---------------------------------------------------------------------
# write a new file
emp_file = open("employee.txt", "w")
emp_file.write("Jim - Salesman\n")
emp_file.write("Karen - Salesman\n")
emp_file.close()

# ---------------------------------------------------------------------
# read file
# ---------------------------------------------------------------------
# read the file in the read mode, other modes are "w", "a", "r+" (r/w)
# emp_file has the content of the file
emp_file = open("employee.txt", "r")
print(emp_file.readable())

# print the whole file
print(emp_file.read())

# print the first line
# read() reads the whole file, without seek(0) which puts the current
# position back to the beginning of the file, the following function call 
# would return nothing
emp_file.seek(0)
print(emp_file.readline())

# realines() return an array
emp_file.seek(0)
print(emp_file.readlines())

# loop through each line of file
emp_file.seek(0)
for emp in emp_file.readlines():
    print(emp)

# close the file
emp_file.close()

# append to an existing file
# with mode "w", the exist file will be overwritten
emp_file = open("employee.txt", "a")
# without \n, next write() will write to the end of same line
emp_file.write("Toby - Human Resources\n")
emp_file.close()

# delete a file
import os
import os.path
from os import path
# delete a file if it exists
if path.exists("employee.txt"):
    os.remove("employee.txt")

# ---------------------------------------------------------------------
# modules and pip
# ---------------------------------------------------------------------

# module is a python file that we can import
# you can find a huge list of python module by search "python module index"
# when you use the import statement to import part or all of a module, Python 
# automatically creates a new file. This new file is the compiled form of the 
# module and it has the same module name as the original one, but it ends with 
# .pyc instead of .py. In this case, it will generate test_module.pyc
import test_module
print(test_module.feet_in_miles)
print(test_module.roll_dice(10))

# to install a 3rd party module, run "pip install <module>" command in command prompt
# pip is avilable in python install


# ---------------------------------------------------------------------
# sets (use set() function)
# ---------------------------------------------------------------------
# set can not have duplicated 
# to create a set from a list
a = set([1, 2, 3, 4])
b = set([3, 4, 5, 6])
c = a | b # Union
print(c)
# returns {1, 2, 3, 4, 5, 6}

c = a & b # Intersection
# return {3, 4}

a < b # Subset
# returns False

c = a - b # Difference
# return {1, 2}

c = a ^ b # Symmetric Difference
# returns {1, 2, 5, 6}

c = a.intersection(b) # equivalent to c = a & b

# ---------------------------------------------------------------------
# convert a list to a set
# ---------------------------------------------------------------------
names = set(['Bob', 'Bill', 'Ted', 'Fred'])
# Test for membership in the set
print ('Bob' in names)

# ---------------------------------------------------------------------
# set operations
# ---------------------------------------------------------------------
a = set('abcde')
b = set('defgh')

# Difference: display items in a that aren't in b
a_dif_b = a - b  # or: a.difference(b)
print ("a - b = ", a_dif_b)

# Union: values in either a or b
a_uni_b =  a | b  # or: a.union(b)
print ("a | b = ", a_uni_b)
# set(['a', 'c', 'b', 'e', 'd', 'g', 'f', 'h'])

# Intersection: display values if they are in both a and b
a_int_b = a & b  # or: a.intersection(b)
print ("a & b = ", a_int_b)
# set(['e', 'd'])

# Exclusive OR: display vlaues only if they are in a or in b but not in both
a_exc_b = a ^ b
print ("a ^ b = ", a_exc_b)
# set(['a', 'c', 'b', 'g', 'f', 'h'])


# ---------------------------------------------------------------------
# classes and objects
# ---------------------------------------------------------------------
class Student:
    # initialize function to initialize the object attributes
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation


# create a student object
student1 = Student("Jim", "Math", 3.6, False) 
student2 = Student("Pam", "Art", 2.5, True) 
print(student1.name)
print(student2.major)


# ---------------------------------------------------------------------
# exercise - "a small quiz"
# ---------------------------------------------------------------------
question_prompts = [
    "what color are apples?\n(a) red\n(b) purple\n(c) orange",
    "what color are bananas?\n(a) red\n(b) yellow\n(c) orange",
    "what colors are strawberries?\n(a) red\n(b) purple\n(c) blue"
]

# how to represent the question? prompt and answer
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

# create three Question instances
questions = [
     Question(question_prompts[0], "a"),
     Question(question_prompts[1], "b"),
     Question(question_prompts[2], "c")
 ]       

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if (answer == question.answer):
            score += 1
    print("Your got" + str(score) + "/" + str(len(questions)) + "correct")

run_test(questions)


# ---------------------------------------------------------------------
# class functions
# ---------------------------------------------------------------------
class Student2:
    # initialize function to initialize the object attributes
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    # regular method takes the object instance as the first argument 
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False


s1 = Student2("Jim", "Math", 3.6) 
s2 = Student2("Pam", "Art", 2.5) 
print(s1.on_honor_roll())

# ---------------------------------------------------------------------
# class inheritance
# ---------------------------------------------------------------------
class Chef:
    def make_chicken(self):
        print("chef makes chicken")

    def make_salad(self):
        print("chef makes salad")

    def make_special_dish(self):
        print("chef makes bbq ribs")

myChef = Chef()
myChef.make_chicken()

# ChineseChef derives from classs Chef
class ChineseChef(Chef):
    # override the make_special_dish in Chef
    def make_special_dish(self):
        print("chef makes orange chicken")

    def make_fried_rice(self):
        print("chef makes fried rice")

myChineseChef = ChineseChef()
myChineseChef.make_chicken()
myChineseChef.make_fried_rice()

# ---------------------------------------------------------------------
# class method, static method, datetime, split
# ---------------------------------------------------------------------
class Student3:
    # class attribute (variable)
    # class attributes are shared (referenced) by all instances of the class.
    # each object instance of the class simply reference to class attributes unless the 
    # instance makes a change to a class attribute, which in this case, a instance attribute
    # is created.
    score_amt = 4

    # initialize function to initialize the object attributes
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    # regular (instance) method takes the object instance as the first argument
    # "self" is just a convention, it could be any non-keyword string 
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

    # you need @classemthod decarator to define a class method
    # "cls" is just convention, it could be any non-keyword string
    @classmethod
    def set_score_amount(cls, amt):
        cls.score_amt = amt

    # use class method as an alternative for contructing an object
    @classmethod
    def from_string(cls, s_str):
        name, major, gpa = s_str.split('-')
        return cls(name, major, gpa)

    # static method doesn't automatically take instance or class as first argument
    # static method doesn't access instance or class attributes
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True


s1 = Student3("Jim", "Math", 3.6) 
s2 = Student3("Pam", "Art", 2.5) 

# the following three calls all print 4
print(Student3.score_amt)
print(s1.score_amt)
print(s2.score_amt)

# __dict__ contains the all the attributes in the class or object intance
print(Student3.__dict__)
# s1 and s2 doesn't have "score_amt" in __dict__
print(s1.__dict__)
print(s2.__dict__)

# this changes the value of the class attribute
# note: you can run the class method from an instance, it behaves the same
#       but it doesn't make a lot of sense
Student3.set_score_amount(4.2)
# this would do the same thing, but it doens't make sense
s1.set_score_amount(4.2)

# this creates an instance attrbiute for s1
s1.score_amt = 4.5

print(Student3.__dict__)
# since we set score_amt for s1, it becomes an instance attribute for s1
# so s1 has "score_amt" in its __dict__
print(s1.__dict__)
print(s2.__dict__)

# class class method "from_string" to construct object
s3_string = "Jam-Physcis-3.6"
s4_string = "Pim-Medical-2.5"

s3 = Student3.from_string(s3_string)
s4 = Student3.from_string(s4_string)

print(s3.name)

import datetime
my_date = datetime.date(2019, 10, 12)  # 10/12/19
print(Student3.is_workday(my_date))

# ---------------------------------------------------------------------
# class special (dunder) methods: 
#  __repr__, __str__, __add__, __len__
# ---------------------------------------------------------------------
# by default, print(<object>) prints something like
#      TODO:
# once you define __repr__ or __str__, you can call repr(<object>)
# or str(<object>)
# str is a more readable representation of the object, it is meanted to be 
#     displayed to end user 
# repr is a unique representation of the object, which is often used by 
#     other developers
# str will use repr as fallback

class Student4:

    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def __repr__(self):
        return "Student('{}', '{}', {})".format(self.name, self.major, self.gpa)

    def __str__(self):
        return "'{}' - '{}'".format(self.name, self.major)

    def __add__(self, other):
        return self.gpa + other.gpa

    def __len__(self):
        return len(self.name)

s1 = Student4("Jim", "Math", 3.6) 
s2 = Student4("Pam", "Art", 2.5) 
# print will call __str__ if it exists, else it call __repr__
print(s1)

print(repr(s1))
# this is same as 
print(s1.__repr__())

# __add__
# print(1+2) internally calls int.__add__()
# it is same as print(int.__add__(1, 2))
# similarly, print("a" + "b") internally calls str.__add__()
# it is same as print(str.__add__("a", "b"))

# print(s1 + s2) is same as s1.__add__(s2)
print(s1 + s2)
print(Student4.__add__(s1, s2))

# __len__
# len() internally calls str.__len__()
# len("test") is same as "test".__len__()
# print(len(s1)) is same as print(s1.__len__())
print(len(s1))

# list of the special methods
# https://docs.python.org/3/reference/datamodel.html#special-method-names


# ---------------------------------------------------------------------
# property decorators 
# ---------------------------------------------------------------------
class Student5:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    # with @property decorator, email() function is accessible as an attrbiute
    # @property defines a getter function
    # whenever you try to get "email" as attribute, it calls this function
    @property
    def email(self):
        return "{}.{}@hotmail.com".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    # this defines a setter function
    # whenever you try to set "fullname" as an attribute, it calls this function
    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split(' ')
    
    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None

s1 = Student5("Jim", "Wang")
# instead of s1.email(), you can access email as an attribute
print(s1.email)

# this calls fullname() with @fullname.setter decorator
s1.fullname = "Andy Wu"
# s1.first should return "Andy" and s1.last should return "Wu"
print(s1.first + " " + s1.last)

# this calls fullname() with fullname.deleter decorator
del s1.fullname

# ---------------------------------------------------------------------
# string formatting 
# ---------------------------------------------------------------------
person = {'name': 'Jenny', 'age': 23}
# a non-formating example, not very readable
sentence1 = "My name is " + person['name'] + " and I am " + str(person['age']) + " years old"
print("sentence1: " + sentence1)

# {} as placeholder
sentence2 = "My name is {} and I am {} years old".format(person['name'], person['age'])
print("sentence2: " + sentence2)

# you can number the placeholder
sentence3 = "My name is {0} and I am {1} years old".format(person['name'], person['age'])
print("sentence3: " + sentence3)

# you can access the dict dirctly from placeholder
# note there is no quote around "name" and "age" in placeholder
sentence4 = "My name is {0[name]} and I am {0[age]} years old".format(person)
print("sentence4: " + sentence4)

# placeholder can be use more than once
tag = "h1"
text = "hell world"
sentence5 = "<{0}>{1}</{0}>".format(tag, text)
print("sentence5: " + sentence5)

# you can access the list too
li = ["Jenny", 23]
sentence6 = "My name is {0[0]} and I am {0[1]} years old".format(li)
print("sentence6: " + sentence6)

# you can access attribute in class
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Jenny", 23)
sentence7 = "My name is {0.name} and I am {0.age} years old".format(p1)
print("sentence7: " + sentence7)

# access the keywords defined in format
sentence8 = "My name is {name} and I am {age} years old".format(name="Jenny", age=23)
print("sentence8: " + sentence8)
 
 # you can unpack the dictionary
 # this is equivalent to setence8
sentence9 = "My name is {name} and I am {age} years old".format(**person)
print("sentence9: " + sentence9)
 
# format numbers
for i in range(1, 11):
    # this prints 1, 2, 3 ...
    sentence = "the value is {}".format(i)
    # this prints 01, 02, 03 ...
    sentence2 = "the value is {:02}".format(i)
    print (sentence)

# decimal point
pi = 3.14156926
# this prints "3.14"
sentence_pi = "Pi is equal to {:.2f}".format(pi)
# this prints "3.1415"
sentence_pi2 = "Pi is equal to {:.4f}".format(pi)

# print large number with , separtor 
# this prints "1,000,000"
sentence_ln = "1M is equal to {:,} byte".format(1000**2)
# this prints "1,000,000.00"
sentence_ln2 = "1M is equal to {:,.2f} byte".format(1000**2)

# print date
# make sure to "import datetime"
my_date = datetime.datetime(2019, 10, 16, 10, 53, 35)
# this prints "2019-10-16 10:53:35"
print (my_date)

# more info is available at https://docs.python.org/3/library/datetime.html
# search for "Format Codes"
# this prints "October 10, 2019"
sentence_dt = "{:%B %d, %Y}".format(my_date)
print (sentence_dt)

sentence_dt = "{0:%B %d, %Y} fell on a {0:%A} and was the day {0:%j} of the year".format(my_date)
print (sentence_dt)


# ---------------------------------------------------------------------
# first class function
# https://www.youtube.com/watch?v=kr0mpwqttM0 
# ---------------------------------------------------------------------
def square(x):
    return x * x

# f gets the result of the function call
f1 = square(5)
# this prints something like "<function square at 0x000002CA04365F28>"
print (square)
print (f1)

# however, you can assign the function itself to a variable
# f2 is like function pointer in C++
f2 = square
# you can see f2 is exactly same as  square
print (square)
print (f2)

# f2 can be used exactly as square
print (f2(5))

# pass a function as argument to another function
def my_map (func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

# you can replace "square" with "f2"
squares = my_map(square, [1, 2, 3, 4, 5])
print (squares)

def cube(x):
    return x * x * x

cubes = my_map(cube, [1, 2, 3, 4, 5])
print (cubes)

# return a function from a function
def logger(msg):
    def log_message():
        print ('Log:', msg)
    return log_message

# this also demonstrates the closure
# see the next section for more info 
log_hi = logger('Hi!')
log_hi()

# a slightly complex example
def html_tag(tag):
    def wrap_text(msg):
        print ('<{0}>{1}</{0}>'.format(tag, msg))
    return wrap_text

print_h1 = html_tag('h1')
# this prints something like "<function html_tag.<locals>.wrap_text at 0x000001F01D7BDC80>"
# print(print_h1)
print_h1('Test Headline!')
print_h1('Another Headline!')

print_p = html_tag('p')
print_p('Test Paragraph')


# ---------------------------------------------------------------------
# closure
# https://www.youtube.com/watch?v=swU3c34d2NQ 
# ---------------------------------------------------------------------
def outer_func ():
    message = 'Hi'

    def inner_func():
        print (message)
    return inner_func

my_func = outer_func()
# what happens if we run my_func
# my_func is still able to access 'message'
# a closure is inner function that rememembers and has access to variables
# in the local scope in which they were created even after outer function
# finished executing
# so the following still prints "Hi"
my_func()

def outer_func_2 (message):
    def inner_func_2():
        print(message)
    return inner_func_2

my_func_2 = outer_func_2("Foo")
# my_func_2 has access to the message variable when it was created
# so it prints "Foo"
my_func_2()
my_func_3 = outer_func_2("Bar")
my_func_3()

# ---------------------------------------------------------------------
# f-string formatting
# https://www.youtube.com/watch?v=nghuHvKLhJA
# f-string is new way of formatting string in python 3.6
# ---------------------------------------------------------------------

# old way of using format() 
first_name = "Corey"
last_name = "Shaft"
print('format(): My name is {} {}'.format(first_name, last_name))

# using f-string
print(f'f-string: My name is {first_name} {last_name}')

# we can call funciton/method directly inside f-string
print(f'My name is {first_name.upper()} {last_name.lower()}')

# use f-string with dictionary
# person dictionary was defined earlier
# person = {'name': 'Jenny', 'age': 23}
print(f"My name is {person['name']}, and I am {person['age']} years old")

# you can do calculation directly in f-string
calculation = f'4 times 11 equals {4 * 11}'
print(calculation)

for n in range (1, 10):
    # 0 padding and 3 digits
    # so "1" will be displayed as "001"
    sentence = f'the current value is {n:03}'
    print(sentence)

# print 4 digits after dicimal point for floating point number
print(f'Pi is equal to {pi:.4f}')

# date
birthday = datetime.date(1984, 10, 11)
# October 11, 1984
print(f'Jen has a birthday of {birthday:%B %d, %Y}')


# ---------------------------------------------------------------------
# generator
# https://www.youtube.com/watch?v=bD05uGo_sVI
# "yield" makes a generator
# ---------------------------------------------------------------------
def sqaure_number(numw):
    for i in nums:
        yield i*i

my_squares = sqaure_number([1, 2, 3, 4, 5])
# my_squares is just a generator object
print(my_squares)
# to print the new numbers in generator
print(next(my_squares))   # this prints 1
print(next(my_squares))   # this prints 4 (2*2)
print(next(my_squares))   # this prints 9 (3*3)
print(next(my_squares))   # this prints 16
print(next(my_squares))   # this prints 25

# alternatively, you can still use for loop to iterate through the new numbers in generator
for new_num in my_squares:
    print(new_num)

# generator above can be simplified as
my_squares_2 = (x*x for x in [1, 2, 3, 4, 5])
# my_squares_2 is exactly same as my_square

# to convert a generator object to a list
print(list(my_squares_2))

# generator is better in terms of the memory consumption
# since it does NOT store all the data in memory as list comprehension
# use the following example to demonstrate the difference

# you need to install memory_profiler package first
# pip install memory_profiler
import memory_profiler as mem_profile
import random
import time

pnames = ['John', 'Steve', 'David', 'Joseph', 'Howard', "Adam"]
pmajors = ['Math', 'Physics', 'Chemistry', 'Civil', 'Mechnical']

print ('Memory (before) {}MB'.format(mem_profile.memory_usage()))

def people_list(num_people):
    result = []
    for i in range(num_people):
        people = {
            'id': i,
            'name': random.choice(pnames),
            'major': random.choice(pmajors)
        }
        result.append(people)
    return result

def people_gen(num_people):
    for i in range(num_people):
        people = {
            'id': i,
            'name': random.choice(pnames),
            'major': random.choice(pmajors)
        }
        yield people

t1 = time.process_time()
people_list(1000000)
t2 = time.process_time()

# t1 = time.clock()
# people_gen(1000000)
# t2 = time.clock()

print ('Memory (before) {}MB'.format(mem_profile.memory_usage()))
print ('Took {} seconds'.format(t2-t1))

# ---------------------------------------------------------------------
# list comprehension
# https://www.youtube.com/watch?v=3dt4OGnU5sM
# an easier and readable to create list
# also lambda, map(), filter()
# ---------------------------------------------------------------------
# list comprehension does NOT crate a generator object, it creates a new list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# my_new_list is  the copy of my_list
my_new_list = [x for x in my_list]
print (my_new_list)

# my_new_list_2 is the square of my_list
my_new_list_2 = [x*x for x in my_list]
print (my_new_list_2)

# using map + lambda
# map each item in my_list using the lambda function
my_new_list_3 = map(lambda n: n*n, my_list)
# <map object at 0x000002822734C908>
print (my_new_list_3)

# what if I am only interested in the even numbers in my_list
my_new_list_4 = [x for x in my_list if x%2 == 0]
print (my_new_list_4)

# this can also be done with filter + lambda
# filter() returns a filter object, in order to print the list content
# use list(<filter object>)
my_new_list_5 = filter(lambda n: n%2 == 0, my_list)
print (list(my_new_list_5))

# a more complicated example
# create a list of tuples of two items 
my_letter_num = [(letter, num) for letter in 'abcd' for num in range(4)]



# ---------------------------------------------------------------------
# lambda
# ---------------------------------------------------------------------
sqrt_func = lambda z: z ** 2
print (sqrt_func(2))
# or
print ((lambda z: z ** 2)(3))

# lambda with two parameters
full_name_func = lambda first, last: f'Full name: {first.title()} {last.title()}'
print (full_name_func('Claude', 'Monet'))

# lambda used in a high order function which 
# is also a lambda
high_ord_func = lambda x, func: x + func(x)
# 2 + 2 * 2
print (high_ord_func(2, lambda x: x * x))
# 2 + 2 + 3
print (high_ord_func(2, lambda x: x + 3))


# reduce() function
# https://www.geeksforgeeks.org/reduce-in-python/
# At first step, first two elements of sequence are picked and the result is obtained.
# Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
# This process continues till no more elements are left in the container.
# This function is defined in “functools” module.

from functools import reduce
# initializing list 
lis = [ 1, 3, 5, 6, 2] 
# using reduce to compute sum of list 
# print end keyword
# https://www.journaldev.com/15182/python-print#python-print-end-keyword
# The end key of print function will set the string that needs to be appended when printing is done.
# By default the end key is set by newline character. So after finishing printing all the 
# variables, a newline character is appended. Hence, we get the output of each print 
# statement in different line. 
print ("The sum of the list elements is : ", end="") 
print (reduce(lambda a, b : a+b, lis)) 



