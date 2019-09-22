# python basics

# this is a single line comment

"""This is a multiple
comment line example
"""

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

# num1 = int(raw_input('Please enter a number:'))
# num1 = int(raw_input('Please enter an another number:'))
# add(num1, num2)
# add(num1)
# add()


# PyCharm, community edition
print("Hello World")

name = "Tom"   # string 
age = 50       # integer   
is_male = True # boolean
print("the character name is " + name + ".")
print("the character age is ",age,".")

# string
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

# number
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
from math import *
print(floor(3.7))  # return 3
print(ceil(3.1))   # return 4
print(sqrt(36))    # return 6.0

# get the user input
user_name = input("this is a prompt, enter your name: ")
print("Hello " + user_name)

# by default, input returns a string
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
# int() only takes a "integer" string
result = int(num1) + float(num2)
print(result)

# list, use []
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

# list functions
lucky_number = [4, 8, 15, 16, 23, 42]
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

lucky_number.reverse()
print(lucky_number)

# friends is the copy of friend
friends2 = friends.copy()

# tuple, use ()
# tuple is immutable, can't be modified once created
coord = (4, 5)
print (coord[0])  # return 4
# coord[1] = 6    # python will error out

# functions
def cube(num):
    return num*num*num*

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
num1 = float(input("Enter first numer: "))
op = input("Enter operator: ")
num2 = float(input("Enter second numer: "))

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

for index in range(len(friends))
    print(friends[index])

# exponent function
print (2**3)   # 2^3

# two dimentinal list
# each element in the list is a list
number_grid = [
    [1, 2, 3]
    [4, 5, 6]
    [7, 8, 9]
    [0]
]

print (number_grid[1][1])   # return 5

# nested for loop to interate through two dimentional list
for row in number_grid:
    for col in row:
        print (col)

# exercise: translator
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

print (translate(input("Enter a phrase: ")))












