#library books

# import os 

# def menu():
#     print("NSTI Book Store ")
#     print("1. Add a book:")
#     print("2. view books: ")
#     print("3. search for the book :")
#     print("4. Exit")

#add a new book 

# def add_new_book(filename):
#     try:
#         with open(filename,"a") as file:
#             title=input("Enter the book title: ")
#             author=input("Enter the Author: ")
#             price=input("Enter the price: ")
#             book=f'{title},{author},{price}\n'
#             file.write(book)
#             print("Book added successfully.")
#     except Exception as e:
#         print(f'An error Occurred: {e}')


# def view_inventory(filename):
#     try:
#         if os.path.exists(filename):
#             with open(filename, "r") as file:
#                 books = file.readlines()
#                 if books:
#                     print("Inventory:")
#                     for book in books:
#                         try:
#                             title, author, price = book.strip().split(',')
#                             print(f'Title: {title}, Author: {author}, Price: {price}')
#                         except ValueError:
#                             print(f"Skipping malformed line: {book.strip()}") 
#                 else:
#                     print("No record found...")
#         else:
#             print("Inventory not found.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# def search_book(filename):
#     try:
#         if os.path.exists(filename):
#             search=input("Enter the Book name:")
#             with open(filename,"r")as file:
#                 book=file.readlines()
#                 found=False
#                 for book in book:
#                     try:
#                         title,author,price=book.strip().split(",")
#                         if title==search:
#                             print("book found below:")
#                             print(f'Title-{title}')
#                             print(f"Author-{author}")
#                             print(f"Price-{price}")                     
#                             found=True
#                             break
#                         if not found:
#                             print("Book not found")
#                     except Exception as e:
#                         print(e)
#         else:
#             print("Inventry file does not exist.")
#     except Exception as e:
#         print(f'an error occurered,{e}')


# def del_book(filename):
#     try:
#         if os.path.exists(filename):
#             title1=input("Enter the title of book:")
#             with open (filename,"r")as file:
#                 books=file.readlines()
#                 found=False
#                 with open(filename,"w")as file:
#                     for book in books:
#                         title,author,price=book.strip().split(',')
#                         if title==title1:
#                             print(f"Deleted -{title},{price}")
#                             found=True
#                         else:
#                             file.write(book)
#                         if not found:
#                             print("Book not found.")
#                         else:
#                             print("inventory file does not exist.")
#     except Exception as e:
#         print(f"An error occurred {e}")     
    

# def main():
#     filename="books.txt"
#     while True:
#         menu()
#         choice=input("Enter your choice : ")
#         if choice =="1":
#             add_new_book(filename)
#         elif choice=="2":
#             view_inventory(filename)
#         elif choice=="3":
#             search_book(filename)
#         elif choice=="4":
#             del_book(filename)

#             print("Exiting the code:")
#             break
#         else:
#             print("Invalid choice.")


# if __name__=="__main__":
#     main()



# y=[200,300,400,500]
# x=[2,3,4,5]
# print(3*x )


