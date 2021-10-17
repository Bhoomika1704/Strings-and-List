# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 22:24:31 2021

@author: Hp
"""


#Assignment 0
"""Find the value of x,y in given sequence"""
x=8;
y=9;
mylist =[10, 1, 8, 3, 6, 5, 4, 7, x, y]
print(mylist)
print("x value is:")
print(mylist[8])
print("y value is:")
print(mylist[9])

#Assignment 1.1
"""Use Operators"""
x=40;
y=10;
if x>y:
    print("x is greaterthan y");
else:
    print("x is lessthan y");
if x==y:
    print("x is equal to y");
else:
    print("x is not equal to y");

"""Create a Simple Calculator"""  
a = int(input("Enter value : "))
b = int(input("Enter value : "))
print(a+b)
print(a-b)
print(a*b)
print(b//a)

#Assignment 1.2
""" STRING Methods """
#capitalize()
txt = "python is FUN!"
x = txt.capitalize()
print (x) 
#casefold()
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x) 
#center()
txt = "mango"
x = txt.center(20, "1")
print(x) 
#count()
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24)
print(x)
#encode()
txt = "My name is Ståle"
x = txt.encode()
print(x) 
#endswith()
txt = "Hello, welcome to my world."
x = txt.endswith("my world.", 5, 11)
print(x) 
#expandtabs()
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)
#find()
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)
#format()
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))  
#index()
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x) 
#isalnum()
txt = "Company12"
x = txt.isalnum()
print(x) 
#isalpha()
txt = "CompanyX"
x = txt.isalpha()
print(x) 
#isascii()
txt = "Company123"
x = txt.isascii()
print(x) 
#isdecimal()
txt = "\u0033" #unicode for 3
x = txt.isdecimal()
print(x) 
#isdigit()
txt = "50800"
x = txt.isdigit()
print(x) 
#isidentifier()
txt = "Demo"
x = txt.isidentifier()
print(x) 
#islower()
txt = "hello world!"
x = txt.islower()
print(x) 
#isnumeric()
txt = "565543"
x = txt.isnumeric()
print(x) 
#isprintable()
txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x) 
#isspace()
txt = "   "
x = txt.isspace()
print(x) 
#istitle()
txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x) 
#isupper()
txt = "THIS IS NOW!"
x = txt.isupper()
print(x)
#join() 
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x) 
#ljust()
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.") 
#lower()
txt = "Hello my FRIENDS"
x = txt.lower()
print(x) 
#lstrip()
txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite") 
#maketrans()
txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))
#partition()
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x) 
#replace()
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x) 
#rfind
txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x) 
#rindex
txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x) 
#rjust()
txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit.") 
#rpartition()
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x) 
#rsplit()
txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x) 
#rstrip()
txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite") 
#split()
txt = "welcome to the jungle"
x = txt.split()
print(x) 
#splitlines()
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x) 
#startswith()
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x) 
#strip()
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite") 
#swapcase()
txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x) 
#title()
txt = "Welcome to my world"
x = txt.title()
print(x) 
#translate()
txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable)) 
#upper()
txt = "Hello my friends"
x = txt.upper()
print(x) 
#zfill
txt = "50"
x = txt.zfill(10)
print(x) 


"""list Methods"""
#append()
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
#clear()
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()
#copy()
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()
#count()
fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry")
#extend()
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
#index()
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry") 
#insert()
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange") 
#pop()
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1) 
#remove()
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana") 
#reverse()
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
#sort() 
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()


"""Simple Calculator using Functions"""

def add(num1, num2):
    return num1 + num2  
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2  
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
print(number_1, "+", number_2, "=", add(number_1, number_2))
print(number_1, "-", number_2, "=", subtract(number_1, number_2))
print(number_1, "*", number_2, "=", multiply(number_1, number_2))
print(number_1, "/", number_2, "=", divide(number_1, number_2))
