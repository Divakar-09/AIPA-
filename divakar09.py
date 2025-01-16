# python keywords and identifiers:
#1
# my_var="divakar"
# print(my_var)
# _myVar="divakar"
# print(_myVar)

# invalid
# 2var="divakar"
# print(2var)
# my-var="divakar"
# print(my-var)

#2 5 python keywords that cannot used as identifiers:
# del, append, extend, clear, insert
# example:
# import keyword
# print("the keyword list is:")
# print(keyword.kwlist)


# python print functions:
# 1 write a program to print  "welcome to python programming "
# x="welcome to python programming"
# print(x)
# 2 use the print () function to display
# x="divakar"
# y=12
# print(x)
# print(y)


# python variables:
# 1 assign the value 25 to a variable and print it 
# x=25
# print(x)

# 2 swap two variables without using a temporary variable 
# assign initial values 
# a=5
# b=10

# a, b = b, a 

# print("a =", a)
# print("b =", b)

# 3 assign three values to three variables in single line.
# a,b,c=1,2,3
# print(a,b,c)

# 4 create a globsl variable and access it inside a function
# def print_global_variable():
# print(global_var)

# global_var="hello kevin!"

# def modify_global_variable():
#  global_var

# modify_global_variable()
# print(global_var)

# python data type:
# 1 determine the data type of the following values 
# 10
# 10.5
# kevin
# True

# a=10
# b=10.5
# c="kevin"
# d=True
# print(type(a))
# print(type(b))
# print(type(c))  
# print(type(d))

# 2 check weather the variable x is of type str 

# x="hi kevin"
# if isinstance(x,str):
#     print("x is a string") 
 

# python Numbers:
# 1 write a program to add two integers 
# a=5
# b=10
# sum=a+b
# print(sum)

# 2 find the reminder when 25 is divided by 4
# reminder = 35 % 4
# print(reminder)

# 3 calculate the square of a number using an operator 



############################################################


# Strings

# 1.Convert the string "python programming" to uppercase.

# text = "python programming"
# print(text.upper())


# 2. Concatenate two strings: "Hello" and "Python".

# str1 = "Hello"
# str2 = "Python"
# result = str1 + " " + str2
# print(result)


# 3. Use an escape character to print: He said, "Python is fun!".

# print("He said, \"Python is fun!\"")




# Python Lists

# 1. Create a list with 5 elements and print the third element.

# my_list = [10, 20, 30, 40, 50]
# print(my_list[2])


# 2. Replace the second element in the list [1, 2, 3, 4, 5] with 10.

# my_list = [1, 2, 3, 4, 5]
# my_list[1] = 10
# print(my_list)


# 3. Add a new item to the end of the list [10, 20, 30].

# my_list = [10, 20, 30]
# my_list.append(40)
# print(my_list)


# 4. Remove the element 20 from the list [10, 20, 30].

# my_list = [10, 20, 30]
# my_list.remove(20)
# print(my_list)


# 5. Sort the list [5, 1, 8, 3] in ascending order.

# my_list = [5, 1, 8, 3]
# my_list.sort()
# print(my_list)



# Python Operators

# 1. Demonstrate the use of arithmetic operators in Python.

# a, b = 10, 5
# print("Addition:", a + b)
# print("Subtraction:", a - b)
# print("Multiplication:", a * b)
# print("Division:", a / b)
# print("Modulus:", a % b)


# 2. Write a program to compare two numbers and print the larger one.

# a, b = 10, 20
# print("Larger number:", a if a > b else b)


# 3. Combine logical operators to check if a number is greater than 10 and less than 20.

# num = 15  



# print(num > 10 and num < 20)



# Python Booleans

# 1. Write a program that returns True if a number is even, and False otherwise.

# def is_even(num):
#     return num % 2 == 0

# print(is_even(4))


# 2. Use the bool() function to check the truth value of an empty list.

# print(bool([]))  # Output: False


# Input and Output

# 1. Write a program that asks for the user's name and prints a greeting.

# name = input("Enter your name: ")
# print(f"Hello, {name}!")


# 2. Take two numbers as input from the user and display their sum.




