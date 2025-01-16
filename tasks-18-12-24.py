# Task-1: Define a class student with attributes name and roll_number. create an object of this class and print its attributes 

# class Student:


#     def __init__(self, name, roll_number):
#         self.name = name
#         self.roll_number = roll_number

# student1 = Student("Divakar", 9)

# print("Name:", student1.name)
# print("Roll Number:", student1.roll_number)

###################################################################

# Task-2: Define a class rectangle with attributes length and width. add a method area to calculate the area of the rectangle. create an object and call the method.

# class Rectangle:

#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
    
#     def area(self):
#         return self.length * self.width


# rect = Rectangle(5, 3)

# print("The area of the rectangle is:", rect.area())

######################################################################

# Task-3: Define a class Circle with a method circumference to calculate the circumference and another method area to calculate the area. Use π = 3.14.

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
    
#     def circumference(self):
#         return 2 * 3.14 * self.radius
#         print(circle.circumference())

    
#     def area(self):
#         return 3.14 * (self.radius ** 2)
        
# circle = Circle(5)
# print(circle.circumference())
# print(circle.area())

# from turtle import circle




########################################################################

# Tsk-4: Define a class Employee with a class attribute company_name and instance attributes name and salary. Print both class and instance attributes.

# class Employee:
    
#     company_name = "Tech Solutions"
    
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

# emp1 = Employee("John Doe", 50000)

# print("Company Name (Class Attribute):", Employee.company_name)
# print("Employee Name (Instance Attribute):", emp1.name)
# print("Employee Salary (Instance Attribute):", emp1.salary)

#########################################################################

# TAsk-5: Create a base class Animal with a method sound. Create a derived class Dog that overrides the sound method. Call the method from an object of Dog.

class Animal:
    def sound(self):
        return "Some generic animal sound"

class Dog(Animal):
    def sound(self):
        return "Bow Bow"
    
class Cat(Animal):
    def sound(self):
        return "meow"

dog = Dog()
cat = Cat()

print(dog.sound()) 
print(cat.sound())

##########################################################################

# Task-6: Create a class Book with attributes title and author. Add a method is_same_author that compares the authors of two book objects.

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     def is_same_author(self, other_book):
#         return self.author == other_book.author

# book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
# book2 = Book("Tender is the Night", "F. Scott Fitzgerald")
# book3 = Book("1984", "George Orwell")

# print(book1.is_same_author(book2))  
# print(book1.is_same_author(book3))  

