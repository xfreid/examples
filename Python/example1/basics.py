# python basics

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
print ("nums is", nums)
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
# print format
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

# ---------------------------------------------------------------------
# function default arguments
# ---------------------------------------------------------------------
def add(a=0, b=0):
     print (a + b)
     return

num1 = 1
num2 = 2
add(num1, num2)
add(num1)
add()

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
print(str(my_num) + " is my favorite number")
print(abs(-5))    # absolute value
print(pow(5, 2))    # 5^2
print(max(4, 6))   # return 6
print(min(4, 6))   # return 4
print(round(3.2))  # return 3
print(round(3.7))  # return 4

# import more math function
#   from <a file> import <class(es)> 
from math import *
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
print(friends[0])   # returs "Kevin"
print(friends[-1])   # returs "Toby"
# range
print(friends[1:])   # returs "Karen", "Jim", "Oscar", "Toby"
print(friends[2:3])   # returs Jim", "Oscar"
# replace "Karen" with "Mike"
friends[1] = "Mike"

# ---------------------------------------------------------------------
# list functions
# ---------------------------------------------------------------------
lucky_numbers = [4, 8, 15, 16, 23, 42]
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

# ---------------------------------------------------------------------
# tuple, use ()
# ---------------------------------------------------------------------
# tuple is like a list, but immutable, can't be modified once created
coord = (4, 5, 6)
print (coord[0])  # return 4
# coord[1] = 6    # python will error out

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
# read file
# ---------------------------------------------------------------------
# read the file in the read mode, other modes are "w", "a", "r+" (r/w)
# emp_file has the content of the file
emp_file = open("C:/Git/Python/example1/employee.txt", "r")
print(emp_file.readable())

# print the whole file
print(emp_file.read())

# print the first line
print(emp_file.readline())

# realines() return an array
print(emp_file.readlines())

# loop through each line of file
for emp in emp_file.readlines():
    print(emp)

# close the file
emp_file.close()


# ---------------------------------------------------------------------
# write to a file
# ---------------------------------------------------------------------
# append to an existing file
# emp_file = open("employee.txt", "a")
# without \n, next write() will write to the end of same line
# emp_file.write("Toby - Human Resources\n")
# emp_file.close()

# with mode "w", the exist file will be overwritten

# write a new file
# emp_file1 = open("employee1.txt", "w")
# emp_file1.write("Toby - Human Resources\n")
# emp_file1.close()


# ---------------------------------------------------------------------
# modules and pip
# ---------------------------------------------------------------------

# module is a pythong file that we can import
# you can find a huge list of python module by search "python module index"
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
     Question(question_prompt[0], "a"),
     Question(question_prompt[1], "b"),
     Question(question_prompt[2], "c")
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
class StudentNew:
    # initialize function to initialize the object attributes
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return true
        else:
            return false


student1 = StudentNew("Jim", "Math", 3.6) 
student2 = StudentNew("Pam", "Art", 2.5) 
print(student1.on_honor_roll())

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

# ChineseChef derives from Chef
class ChineseChef(Chef):
    # override the make_special_dish in Chef
    def make_special_dish(self):
        print("chef makes orange chicken")

    def make_fried_rice(self):
        print("chef makes fried rice")

myChineseChef = ChineseChef()
myChineseChef.make_chicken()
myChineseChef.make_fried_rice()


