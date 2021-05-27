#oop
# create class
# class definition by name class
#  name/type NameOfClass (object) -> class parent

class Math:
    PI = 3.14
    def __init__(self, size):
        self.size = size

    def calc_size(self, y):
        return self.size * self.PI * y
obj = Math(300)
obj.calc_size(5)
obj2 = Math(3000)

# class Car:
#     # class Variable
#     BRAND = 'BMW'
#     def __init__(self, engine, name):
#         self.engine = engine
#         self.name = name
#         # print('self', self)
#         # print('INIT CALLED')
#
#     def get_enginge(self):
#         print(self.engine)
#
#     def greeting_car(self, number):
#         print(self.name +" "+ str(number))
#
# obj = Car(3000, 'LOLO')
# # obj.get_enginge()
# obj.greeting_car(400)
# obj2 = Car(1500, 'TOTO')
# obj2.get_enginge()
# class Test:
#     def __init__(self):
#         print(self)
#         print('constructor called')
# class Test2:
#     pass
# obj = Test2()
#
# test1 = Test()
# test2 = Test()
# print(test1)
# print(test2)
#test1 -> 0x7fdde8e5b9a0 (property of test1)
# test2 -> 0x7f958c9fd790 (property of test2)
# define attributes here

# start with class and name of class convention name start with Captial
# class Employee:
#    pass
#   #  def __init__(self):
#       #  pass
#       #  print('constructor called')


# #create instance object
# obj = Employee()
# print(obj)









# # example for class containe variable, constructor and method

# class Employee:
#    'Common base class for all employees'
#    empCount = 0
#    def __init__(self, name, salary):
#       self.name = name
#       self.salary = salary
#       # access class variable
#       Employee.empCount += 1
#
#    def displayCount(self):
#        print("Total Employee %d" % Employee.empCount)
#
# #    def displayEmployee(self):
# #       print("Name : ", self.name,  ", Salary: ", self.salary)
#
# obj = Employee('ahmed', 1000)
# obj.displayCount()

# obj2 = Employee('hamada', 5)
# obj2.displayCount()
# print('--------------------------')

# print('obj=', obj.displayEmployee())

# print('obj2=', obj2.displayEmployee())

#Accessing Attributes

#obj.displayCount

# add access attr , create oobj, create class , create variable ckass

class Employee:
    'Common base class for all employees'
    #jjjj
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print ("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name,  ", Salary: ", self.salary)
#
# # "This would create first object of Employee class"

emp1 = Employee("ITI", 2000)
# # "This would create second object of Employee class"
# emp2 = Employee("Manni", 5000)
# emp1.displayEmployee()
# emp2.displayEmployee()
# print("Total Employee %d" % Employee.empCount)

# #self.age
# #age inside object
# print(emp1.age)
# try:
#     print(emp1.age)
# except:
#     emp1.age = 30  # Add an 'age' attribute.
# finally:
#     print(emp1.name)
#     print(emp1.age)

# emp1.age = 8  # Modify 'age' attribute.
# print(emp1.age)
# print(emp2.age)

# del emp1.age  # Delete 'age' attribute.
# # print(emp1.age)
# print("Total Employee %d" % Employee.empCount)



# #init
# class Person:
#    def __init__(self, age, name):
#       self.name = name
#       self.age = age


# p1 = Person('mo', 32)

# print(p1.name)
# print(p1.age)


# class Person:
#    def __init__(self, age, name):
#       self.name = name
#       self.age = age

#    def myFunc(self):
#       print('hello', self.name)
# p1 = Person('mo', 32)

# print(p1.name)
# print(p1.age)



#self references to current instance

# you can change name of self for anyother name


# class Person:
#    def __init__(self, age, name):
#       self.name = name
#       self.age = age
#
#    def myFunc(abc):
#       print('hello', abc.name)
# p1 = Person('mo', 32)
#
# # print(p1.name)
# # print(p1.age)
#
# p1.myFunc()

#  The getattr(obj, name[, default]) − to access the attribute of object.
#  The hasattr(obj,name) − to check if an attribute exists or not.
#  The setattr(obj,name,value) − to set an attribute. If attribute does not exist, then it would be created.
#  The delattr(obj, name) − to delete an attribute.
# emp1.age = 50
# bol = hasattr(emp1, 'age')    # Returns true if 'age' attribute exists
# print('check attr related obj ==== ', bol)
# # get_val = getattr(emp1, 'age')    # Returns value of 'age' attribute
# # print('value', get_val)
# setattr(emp1, 'age', 25) # Set attribute 'age' at 30000
# bol = hasattr(emp1, 'age')    # Returns true if 'age' attribute exists
# print('check attr related obj ==== ', bol)
# print('updated age', emp1.age)
#
# delattr(emp1, 'age')    # Delete attribute 'age'
#
# try:
#    print('updated age', emp1.age)
# except:
#    print('deleted age')



# print("Employee.__doc__:", Employee.__doc__) #__doc__ − Class documentation string or none, if undefined.
# print("Employee.__name__:", Employee.__name__) #__name__ − Class name.
# print("Employee.__dict__:", Employee.__dict__) #__dict__ − Dictionary containing the class's namespace.
#


# #Destroying Objects (Garbage Collection)
#
# a = 40      # Create object <40>
# b = a       # Increase ref. count  of <40>
# c = [b]     # Increase ref. count  of <40>
#
# del a       # Decrease ref. count  of <40>
# b = 100     # Decrease ref. count  of <40>
# c[0] = -1   # Decrease ref. count  of <40>

# '''
#  You normally will not notice when the garbage collector destroys an orphaned instance and reclaims
#  its space. But a class can implement the special method __del__(), called a destructor,
#  that is invoked when the instance is about to be destroyed.
#  This method might be used to clean up any non memory resources used by an instance.
# '''
# class Point:
#       pass
# #
# pt1 = Point()
# pt2 = pt1
# pt3 = pt1
# # #id to get id of object
# print(id(pt1), id(pt2), id(pt3)) # prints the ids of the obejcts
# del pt1
# del pt2
# del pt3


# class Animal: #=> parent class
#     drink = ''
#     eat = ''
#
# class Cat(Animal): # child
#     speaking = 'neaw'
#
# class Dog(Animal):
#     speaking = 'haw haw'
#
# cat = Cat()
# dog = Dog()
#Class Inheritance

# class Parent:        # define parent class
#    parentAttr = 100
#    # override
#    def __init__(self):
#       print("Calling parent constructor")
#
#    def parentMethod(self):
#       print('Calling parent method')
#
#    def setAttr(self, attr):
#       Parent.parentAttr = attr
#
#    def getAttr(self):
#       print("Parent attribute :", Parent.parentAttr)
#
# class Child(Parent): # define child class
#    def __init__(self):
#       print("Calling child constructor")
#
#    def childMethod(self):
#       print('Calling child method')
#
#
# c = Child()          # instance of child
# c.childMethod()      # child calls its method
# c.parentMethod()     # calls parent's method
# c.setAttr(200)       # again call parent's method
# c.getAttr()          # again call parent's method

'''
Similar way, you can drive a class from multiple parent classes as follows −
class A:        # define your class A
.....

class B:         # define your class B
.....

class C(A, B):   # subclass of A and B
.....
'''
# class A:
#     def called_A(self):
#         print('called_A')
# class B:
#     def called_b(self):
#         print('called_b')
# class c(A, B):
#         pass
# obj = c()
# obj.called_A()
# obj.called_b()

#Overriding Methods
#overriding parent's methods is because you may want special or different functionality in your subclass.

# class Parent:        # define parent class
#    def myMethod(self):
#       print('Calling parent method')
#
# class Child(Parent): # define child class
#    def myMethod(self):
#       print('Calling child method')
#
# class Child2(Parent):
#     pass
#
# c = Child()          # instance of child
# c.myMethod()
# x = Parent()
# x.myMethod()
#overloading

# class Vector:
#    '''
#    Suppose you have created a Vector class to represent two-dimensional vectors,
#     what happens when you use the plus operator to add them? Most likely Python will yell at you.
#
#    You could, however, define the __add__ method in your class
#    to perform vector addition and then the plus operator would behave as per expectation −
#    '''
#    def __init__(self, a, b):
#       print(a)
#       print(b)
#       self.a = a
#       self.b = b
#
#    def __str__(self):
#       return 'Vector (%d, %d)' % (self.a, self.b)
#
#    def __add__(self,other):
#       return Vector(self.a + other.a, self.b + other.b)
#
# v1 = Vector(2, 10)
# v2 = Vector(5, -2)
# print(v1 + v2)

#Data Hiding
#privte var __var
# class JustCounter:
#    __secretCount = 0
#
#    def count(self):
#       self.__secretCount += 1
#       print(self.__secretCount)
#
#
# counter = JustCounter()
# counter.count()
# counter.count()
#


# #init again and inhertence

class Person:
   def __init__(self, name, lname):
      self.name = name
      self.lname = lname

   def myFunc(abc):
      print('hello', abc.name)
# p1 = Person('mo','hama')

# print(p1.name)
#
# p1.myFunc()
#
# class Student(Person):
#    def __init__(self, fname, lname, year):
#       Person.__init__(self, fname, lname)
#       # add properties
#       self.graduationyear = year
#
#    #add method
#    def welcome(self):
#       print("welcome", self.name, self.lname, 'to the class of', self.graduationyear)
#
# x = Student('ahmed', 'elmahdy', 2020)
# x.welcome()

#some notes

# '''
# 123 is instance of int
# "hello" is instance of str
# '''
