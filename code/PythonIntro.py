"""
Created on Sun Mar 12 15:39:22 2017

@author: Vincent Gregoire

Prepared by [Vincent Grégoire](http://www.vincentgregoire.com), 
Department of Finance, The University of Melbourne. 

This is a sample code to illustrate some basic features of the Python language.
This notebook was created as supplemental material to a Python for 
financial research workshop for finance honours and PhD students at 
the University of Melbourne in March of 2018.

Last update: March 9, 2018.

**Contact**: <vincent.gregoire@unimelb.edu.au>

Latest version: <http://www.vincentgregoire.com/python-bootcamp/>
"""


# This is a comment!

"""
This is a longer comment
that can span multiple
lines.
Actually this is a string which is not
assigned to anything, so it is code,
but it does nothing.
"""


# %% This is a neat comment trick that split blocks of code in Spyder
# To execute the code in the block, just type shift-enter.


# It is usual to always begin by saying Hello World!
# I prefer to use parenthesis, but they are not required for `print`.
print('Hello World!')

# Python is case sensitive, so the statement below is different from
# the one above, and would not work as PRINT() is not defined.
# PRINT('HELLO WORLD!')

# %% Number and operators

print(2 + 2)

print(4 - 1)

print(5 * 2)

print(5.5 * 2)

print(10 / 2)

print(11 / 2)

print(2 ** 8)

print(round(22.34))

print(8 // 3)  # Integer division
print(8 % 3)  # Modulo (remainder of integer division)



# %% Variables

a = 2

b = 4

a * b

c = 'Hello'

c

# This doesn't work
# a + c

d = "World"

c + ' ' + d + '!'


# %% Operators

2 == 2

2 < 2

2 <= 2

True | False # OR

True & False # AND

True != False # XOR

not True # NOT

# %% None

# In Python there is a special value for null objects that is called None.
# Note that you first need to define a variable as None before you can
# access it.

a = None
b = 1

a is None

b is None

b is not None

# %% Strings

s = 'Hello World!'

len(s)

s[1]
s[0]
s[-1]
s[-2]

s[2:5]

s.upper()

s.lower()

'   Hello   '.strip()


'2'.zfill(3)
'20'.zfill(3)

s.replace('World', 'Moon')
s.replace('o', 'a')

s.find('d')
s[10]

# s + 2 # Error

s + str(2)

s * 2


s.split(' ')

s.startswith('Hell')

s.count('l')

print('Don\'t forget to escape the quotes.')

#%% Input

x = input('Type something: ')


#%% Input exercise

# Exercise: write a program that asks the user's name and responds with
# a personalised greating.

x = input('What is you name? ')

print('Good day to you, ' + x + '.')


# %% Sequences


# List

l = [2, 4, 'blabla', 4]
l[0]
l[2:4]

l[0] = 3

# Delete one element
del l[1]

l.append(3)

l.reverse()

l.pop()

l + l

l2 = [23, 2, 94, 39]
l2.sort()

l3 = ['oranges', 'apples', 'bananas']
l3.sort()

# Tuple (immutable list)

t1 = 2, 3
t2 = (2, 3)

34 not in t1

3 in t1


# Set (unordered list of unique elements)
{3, 4, 4, 5, 4}

# Dictionnary
d = {1: 2, 'a': 'Hello'}
d['a']

d['b'] = 'World!'


# Special note: copying lists (and most other objects)
# This does not create a new list, both l and l2 refer to the
# same list.

l_copy = l

l_copy.reverse()

l

# To create a new copy, you need to deepcopy
import copy

l_realcopy = copy.deepcopy(l)


# %% Identity

# For base types (numbers, strings), 'is' and == behave the same way.
2 is 2
2 == 2
'aa' is 'aa'
'aa' == 'aa'

# For other objects (including list), 'is' checks if the two operands refer
# to the same object, while == compares the content.

[1, 2, 3] is [1, 2, 3]
[1, 2, 3] == [1, 2, 3]


# %% Loops and branches (Flow control)

# Notice the indentation! This is how Python identifies
# blocks of codes. PEP8 recommends 4 spaces (as long as a tab,
# but actual spaces.) Spyder will do this automatically.

# Branches
if 1 > 2:
    print('Yes')
elif 2 > 2:
    print('No')
else:
    print('I don\'t know')

# Repeat for each element in the list. (note that 'l' need not be a list, it
# can be anything that is iterable, but for now you can think list!)
for x in l:
    print(x)
    
range(5)

for i in range(5):
    print(i)

for i, x in enumerate(l):
    print( str(i) + ', ' + str(x) )
    
# Interating on dictionnaries is iterating on keys.
for x in d:
    print(str(x) + ': ' + str(d[x]))
    

# Repeat something until a condition is met.
sum = 0

while sum < 10:
    sum = sum + 2
    print(sum)
    
# break and continue
# When iterating, you can stop the loop completely using break,
# or just skip the current iteration using continue.
for i in range(10):
    if i == 3:
        continue
    elif i == 6:
        break
    print(i)


# %% List comprehension

# We saw above how to assign a list statically. Another way is to assign
# actively from another list 

fillings = ['Apple', 'Cherry', 'Sugar', 'Meat']

pies = [x + ' pie' for x in fillings]

# Same idea with dictionnaries

swapped_cases = {x: x.swapcase() for x in fillings}

# Can have conditions
desserts = [x + ' pie' for x in fillings if x != 'Meat']

# Or multiple loops

desserts = [x + ' pie' + y for x in fillings if x != 'Meat' 
            for y in ('', ' with ice cream')]
# You can have as many loops as you want, but best practice is to limit to
# only 2 loops in list comprehensions.

# %% Loading packages

# Python is a pretty powerful language, but most of the benefits come from
# the buil-in functionality is somewhat limited. Most advanced features are
# available through packages, either as part of the Python Standard Library
# or from third-parties.

# To load a package and make it available, you have to import it.
import sys

# You can list the components using the dir() method (or in the console,
# typing os. and then tab to show avaialble options.)
dir(sys)

sys.path

# It's common to rename packages with the 'as' keyword to make access easier.
import pandas as pd

# If you want to import all the components of a pakcage, you can use *
from datetime import *

# But it's usually best to only import what you need
from datetime import datetime, timedelta

# You can also load only a subpackage if that's all you need.
import statsmodels.formula.api as sm


# %% Functions


def square(x):
    return x * x

square(2)

# Variables defined inside a function are only available
# inside that function


def computeBigSum(a, b, c, d):
        e = a + b
        f = c + d
        print(str(e))  # This works here
        return e, f
    
sum1, sum2 = computeBigSum(1, 2, 4, 5)

# But not here.
# print(str(e))
# You have to use a name defined in this scope.
print(str(sum1))


# You can make some arguments optional by assigning default values.
# Note that all required arguments need to be listed before the
# optional ones
def raise_power(n, power=2):
    return n**power

print(raise_power(4))
print(raise_power(4, 2))
print(raise_power(4, 3))

# %% Recursive function

# A function can call itself, we call this a recursive
# function. Just make sure you have a condition to stop
# the recursion (so that it doesn't run forever).

# A Fibonacci number is part of a sequence were every number is the
# sum of the previous two numbers in the sequence. The first two numbers
# of the sequence are defined to be 0 and 1.
# https://en.wikipedia.org/wiki/Fibonacci_number

def fibonacci_recursive(n):
    if n in [0, 1]:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

fibonacci_recursive(10)


# You can get the limit of recursion loops.
sys.getrecursionlimit()


# %% Iterative function

# However, recursion is not always the best solution. In this case, for
# large numbers (say 50+), even a modern computer will take some time.

# A better way is the iterative way

def fibonacci_iter(n):
    if n in [0, 1]:
        return n
    a = 0
    b = 1
    c = a + b
    for i in range(2, n):
        a = b
        b = c
        c = a + b
    return c

fibonacci_iter(10)

[fibonacci_iter(x) for x in range(10)]
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# %% Exceptions

# Sometimes things go wrong, and the code crashes. But it doesn't have to.
# You can catch exceptions, and decide what to do.


def inverse(n):
    return 1.0 / n

inverse(0)

def inverse_ex(n):
    out = None
    try:
        out = 1.0 / n
    except ZeroDivisionError as e:
        print(e)
        out = 0.0
    finally:
        return out
    

inverse_ex(0)    

# Anywhere in your code, you can raise your own exceptions
raise Exception('I just raised an exception!')


# %% Classes

# Python is an object-oriented programming
# language, which means that most of the datatypes are classes, and the
# actual instances of those datatypes are called objects.

# You can create your classes if you want to (probably won't need to at first)
class Rectangle:
    def __init__(self, length=1, width=1):
        self.length = length
        self.width = width
        
    def __repr__(self):
        return str(self.length) + 'x' + str(self.width) + ' rectangle'

    def getArea(self):
        return self.length * self.width

    def setLength(self, x):
        self.length = x

    def setWidth(self, x):
        self.width = x
    
    def getLength(self):
        return self.length
    
    def getWidth(self):
        return self.width
    
rect = Rectangle(3, 4)

print(rect)

rect.getArea()
