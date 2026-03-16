# If you are wrapping the functions inside a class, then they are called as Methods.

class Calculator:
    num = 100

    def getData(self):
        print("I am now executing as method in class")

obj = Calculator()

obj.getData()
print(obj.num)

#constructor
class Calculator:
    num = 100
    #default constructor

    def __init__(self):
        print("I am called automatically when object is created")

    def getData(self):
        print("I am executing as method in class")

obj = Calculator()
obj.getData()
print(obj.num)

# There are two types of variable
# 1. Class variable
#A class variable is declared inside the class but outside any method.
#It is shared by all objects (instances) of that class.
#If one object changes it, it affects all objects.

class Student:
    school = "ABC School"   # class variable

s1 = Student()
s2 = Student()

print(s1.school)
print(s2.school)
#Here school is a class variable shared by both s1 and s2.
#Class variable → Same for all objects

#2. Instance Variable
#An instance variable is declared inside a method (usually __init__) using self.
#Each object has its own separate copy of the variable.

class Student:
    def __init__(self, name):
        self.name = name   # instance variable

s1 = Student("Rahul")
s2 = Student("Anita")

print(s1.name)
print(s2.name)

#Here name is an instance variable, and each object stores a different value.
#Instance variable → Different for each object

#| Type              | Defined Where                 | Shared or Separate       |
#| ----------------- | ----------------------------- | ------------------------ |
#| Class Variable    | Inside class, outside methods | Shared by all objects    |
#| Instance Variable | Inside methods using `self`   | Separate for each object |

#self keyword is mandatory for calling variable name into method
#instance and class variables have whole different purpose
#constructor name should be __init__
#new keyword is not required when you create object

#Program
class Calculator:
    num = 100  # class variable

    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executing as method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num

obj = Calculator(2, 3)
obj.getData()
print(obj.Summation())  # 2 + 3 + 100 = 105

obj1 = Calculator(4, 5)
obj1.getData()
print(obj1.Summation()) # 4 + 5 + 100 = 109

