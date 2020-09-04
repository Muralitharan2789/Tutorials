# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 19:41:05 2020
"""

#Higher Order Functions

'''
A Higher Order function is a function, which is capable of doing any one of the following things:
It can be functioned as a data and be assigned to a variable.
It can accept any other function as an argument.
It can return a function as its result
'''

    #Function as a Data
def greet():
    return 'Hello Everyone!'
print(greet())
wish = greet        # 'greet' function assigned to variable 'wish'
print(type(wish))   
print(wish())    

    #Function as an Argument
def add(x, y):
    return x + y
def sub(x, y):
   return x - y
def prod(x, y):
    return x * y
def do(func, x, y):
   return func(x, y)

print(do(add, 12, 4))  # 'add' as arg
print(do(sub, 12, 4))  # 'sub' as arg
print(do(prod, 12, 4))  # 'prod' as arg

    #Returning a Function
    
def outer():
    def inner():
        s = 'Hello world!'
        return s            
    return inner()    
print(outer())

#You can observe from the output that the return value of 'outer' function is the return value of 'inner' function i.e 'Hello world!'.
    
def outer():
    def inner():
        s = 'Hello world!'
        return s            
    return inner   # Removed '()' to return 'inner' function itself

print(outer()) #returns 'inner' function
#Parenthesis after the inner function are removed so that the outer function returns inner function.
func = outer() 
print(type(func))
print(func()) # calling 'inner' function


#Closures
'''
In simplest terms, a Closure is a function returned by a higher order function, 
whose return value depends on the data associated with the higher order function.
'''
def multiple_of(x):
    def multiple(y):
        return x*y
    return multiple

c1 = multiple_of(5)  # 'c1' is a closure
c2 = multiple_of(6)  # 'c2' is a closure
print(c1(4))
print(c2(4))


#Decorators
'''
A decorator function is a higher order function that takes a function as an argument and returns the inner function.
A decorator is capable of adding extra functionality to an existing function, without altering it.
'''

def outer(func):
    def inner():
        print("Accessing :", 
                func.__name__)
        return func()
    return inner
@outer
def greet():
    return 'Hello!'
greet()

    #greet = outer(greet) expression is same as @outer.
    
#Descriptors
    
class EmpNameDescriptor:
    def __get__(self, obj, owner):
        return self.__empname
    def __set__(self, obj, value):
        if not isinstance(value, str):
            raise TypeError("'empname' must be a string.")
        self.__empname = value
        

class EmpIdDescriptor:
    def __get__(self, obj, owner):
        return self.__empid
    def __set__(self, obj, value):
        if hasattr(obj, 'empid'):
            raise ValueError("'empid' is read only attribute")
        if not isinstance(value, int):
            raise TypeError("'empid' must be an integer.")
        self.__empid = value
        
class Employee:
    empid = EmpIdDescriptor()           
    empname = EmpNameDescriptor()       
    def __init__(self, emp_id, emp_name):
        self.empid = emp_id
        self.empname = emp_name

e1 = Employee(123456, 'John')
print(e1.empid, '-', e1.empname)  

e1.empname = 'Williams'

print(e1.empid, '-', e1.empname)

e1.empid = 76347322  

'''
However when executing the expression e1.empid = 76347322, the __set__ method defined in 
EmpIdDescriptor is executed and raises "ValueError: 'empid' is read only attribute".
'''


#Introduction to Class and Static Methods

    #Class Methods - Example
class Circle(object):
    no_of_circles = 0
    def __init__(self, radius):
        self.__radius = radius
        Circle.no_of_circles += 1
    def getCirclesCount(self):
        return Circle.no_of_circles
    
c1 = Circle(3.5)
c2 = Circle(5.2)
c3 = Circle(4.8)

print(c1.getCirclesCount())     # -> 3
print(c2.getCirclesCount())     # -> 3
print(Circle.getCirclesCount(c3)) # -> 3
print(Circle.getCirclesCount()) # -> TypeError


    # Static Method
class Circle(object):
    def __init__(self, radius):
        self.__radius = radius
    @staticmethod
    def square(x):
        return x**2
    def area(self):
        return 3.14*self.square(self.__radius)
    
c1 = Circle(3.9)
print(c1.area())  
print(square(10)) # -> NameError

# Problems: Class and static Methods
class Circle(object):
    no_of_circles = 0
    def __init__(self, radius):
        self.__radius = radius
        Circle.no_of_circles += 1
    @classmethod
    def getCirclesCount(self):
        return Circle.no_of_circles
    def area(self):
        return round(3.14*(self.__radius)*(self.__radius),2)
    

class Circle(object):
    no_of_circles = 0
    def __init__(self, radius):
        self.__radius = radius
        Circle.no_of_circles+=1
    @classmethod
    def getCirclesCount(self):
        return Circle.no_of_circles
    @staticmethod
    def getPi():
        return 3.14
    def area(self):
        return self.getPi()*(self.__radius)*(self.__radius)

#Abstract Classes
        
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    
class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius
    @staticmethod
    def square(x):
        return x**2
    def area(self):
        return 3.14*self.square(self.__radius)
    def perimeter(self):
        return 2*3.14*self.__radius
c1 = Circle(3.9)



# Quiz
class Animal(ABC):
    @abstractmethod
    def say(self):
        pass
    
class Dog(Animal):
    
    @staticmethod
    def say():
        return 'I speak Booooo'
    
#Context Manager
from contextlib import contextmanager

@contextmanager
def context():
    print('Entering Context')
    yield 
    print("Exiting Context")

with context():
    print('In Context')
    
from contextlib import contextmanager

@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag('h1') :
    print('Hello')
    
# Quiz
    
# Define 'writeTo' function below, such that 
# it writes input_text string to filename.
def writeTo(filename, input_text):
    with open(filename,'w+') as fp:
        content=fp.write(input_text)
    return content
    
# Define the function 'archive' below, such that
# it archives 'filename' into the 'zipfile'
from zipfile import ZipFile
def archive(zfile, filename):
    with ZipFile(zfile, 'w') as myzip:
        myzip.write(filename)

import subprocess
def run_process(cmd_args):
    with subprocess.Popen(cmd_args, stdout=subprocess.PIPE) as p:    
        output = p.stdout.read() 
        return output
    
    
#Coroutine
        
'''
A Coroutine is generator which is capable of constantly receiving input data, process input data and may or
may not return any output.
'''

def TokenIssuer():
    tokenId = 0
    while True:
        name = yield
        tokenId += 1
        print('Token number of', name, ':', tokenId)
t = TokenIssuer()
next(t)
t.send('George')
t.send('Rosy')
t.send('Smith')

def TokenIssuer(tokenId=0):
    try:
       while True:
            name = yield
            tokenId += 1
            print('Token number of', name, ':', tokenId)
    except GeneratorExit:
        print('Last issued Token is :', tokenId)
t = TokenIssuer(100)
next(t)
t.send('George')
t.send('Rosy')
t.send('Smith')
t.close()

    #If the developer forgets use next function call below decorator can be used
def coroutine_decorator(func):
    def wrapper(*args, **kwdargs):
        c = func(*args, **kwdargs)
        next(c)
        return c
    return wrapper

@coroutine_decorator
def TokenIssuer(tokenId=0):
    try:
        while True:
            name = yield
            tokenId += 1
            print('Token number of', name, ':', tokenId)
    except GeneratorExit:
        print('Last issued Token is :', tokenId)
t = TokenIssuer(100)
t.send('George')
t.send('Rosy')
t.send('Smith')
t.close()


def coroutine_decorator(coroutine_func):
    def wrapper(*args, **kwdargs):
        c = coroutine_func(*args, **kwdargs)
        next(c)
        return c
    return wrapper
    
# Define the coroutine function 'linear_equation' below
@coroutine_decorator
def linear_equation(a, b):
    while True:
        x = yield
        e = a*(x**2)+b
        print('Expression, '+str(a)+'*x^2 + '+str(b)+', with x being '+str(x)+' equals '+str(e))
    
# Define the coroutine function 'numberParser' below
@coroutine_decorator
def numberParser():
    x=yield
    equation1 = linear_equation(3, 4)
    equation2 = linear_equation(2, -1)
    # code to send the input number to both the linear equations
    equation1.send(x)
    equation2.send(x)

def main(x):
    n = numberParser()
    try:
        n.send(x)
    except StopIteration as e:
        pass