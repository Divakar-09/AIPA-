# x = input("Type a number: ")
# print(x)




# import keyword
# koushik99=keyword.kwlist
# print (koushik99)




# x="""The sun dipped below the horizon, painting the sky in shades of orange and pink.
# The cool breeze rustled the leaves of the trees, and the sound of distant waves crashing on the shore brought a sense of calm.
# It was a peaceful evening, the kind that made you forget about the rush of everyday life and simply enjoy the present moment"""
# print(x)




# x=9
# y=2
# z=x/y 
# # z=x//y
# print(z)




# x="Divakar"
# y=" AI"
# z=12
# print(x)
# print(type(y))
# print(type(z))
# print(type(x))
# print(x[0:4])
 



# print(2>3)
# print(2==3)
# print(2==2)




# x=["koushik","sadvika","uma","srivalli","sampath"]
# x.append("ramesh")
# x.insert(3,"kothi")
# print(x)
# del x[0:3]
# print(x)
# y=["tain","bike","car","truck","aeroplane"]
# x.extend(y)
# print(x)
# del y[0:3]
# print(y)
# x.clear()
# y.clear()
# print(x)
# print(y)
 

# x=("daya","divakar",5,7,"deepaak","danush")
# y=list(x)
# print(type(x))

# y[2]="shailesh"
# x=tuple(y)
# print(x)

# y=("kevin",)
# x +=y
# print(y)

# x=("apple","mango","grape")
# y=("orange","banana")
# z=("hii","bye")
# a=x+x+z
# print(a)

# x += y
# print(x)



# my_var="edaina"
# print(my_var)


# my_Var="edaina"
# print(my_Var)



# x=1
# y=2
# x=y
# y=7
# print(x,y)

# x=1
# y=2
# x=y
# y=7
# print(x,y)

# a,b,c=1,2,3
# print(a,b,c)


# Global variable
# x = 10

# def modify_global():
#     global x
#     x = 20
#     print("Modified global variable x inside the function:", x)

# modify_global() 
#  # Output: Modified global variable x inside the function: 20
# print("Global variable x outside the function:", x) 
#  # Output: Global variable x outside the function: 20



# for i in range(1,9):
#     print(i)

# fruits=["apple","banana","grape"]

# for fruit in fruits:
#     print(fruit)


# varieties=["chicken curry","muttoncurry","fish curry"]

# for i in varieties:
#     print(i)

# word = "hello"
# for char in word:
#     print(char)


# cars=["benz","audi","jaguar","lambo","bugatti","santro"]

# for i in cars:
#     print(i)

# start=1
# end=21

# for i in range(start,end+1):
#     if i % 2 !=0:
#         print(i)


# for i in range(1,21):
#     if i % 2==0:
#         print(i)


# for i in "apple":
#     print(i)

# 

# class flipkart:

#     def __init__(self,name,price):
#         self.name=name
#         self.price=price


#     def adding_item(self,name,price):
#         self.name = name
#         self.price = price
#         print(f'item added {name} price: {price} ')

#     def display_name(self,name,price):
#         self.name=name
#         self.price=price
#         print(f' item : {name} price : {price}')

#     # def removing_item(self,name,price):
#     #     self.name
#     #     self.price

# x=flipkart()

# x.adding_item()
# x.display_name()

# class ShoppingCart:
#     def __init__(self):
#         self.cart = []
    
#     def add_item(self, item, price):
#         """Adds an item and its price to the cart."""
#         self.cart.append({'item': item, 'price': price})
#         print(f"Added {item} to the cart for ${price:.2f}.")
    
#     def remove_item(self, item):
#         """Removes an item from the cart by name."""
#         for product in self.cart:
#             if product['item'].lower() == item.lower():
#                 self.cart.remove(product)
#                 print(f" {item} from the cart.")
#                 return
#         print(f"Item '{item}' not found in the cart.")
    
#     def display_cart(self):
#         """Displays the contents of the cart."""
#         if not self.cart:
#             print("Your cart is empty.")
#             return
        
#         print("Items in your cart:")
#         for idx, product in enumerate(self.cart, 1):
#             print(f"{idx}. {product['item']} - ${product['price']:.2f}")
    
#     def calculate_total(self):
#         """Calculates the total cost of the items in the cart."""
#         total = sum(item['price'] for item in self.cart)
#         print(f"Total cost: ${total:.2f}")

#     def context_menu(self):
#         """Displays the shopping cart context menu."""
#         while True:
#             print("\nShopping Cart Menu:")
#             print("1. Add item to cart")
#             print("2. Remove item from cart")
#             print("3. Display cart")
#             print("4. Calculate total cost")
#             print("5. Exit")
#             choice = input("Choose an option (1-5): ")
            
#             if choice == '1':
#                 item = input("Enter the name of the item: ")
#                 price = float(input("Enter the price of the item: $"))
#                 self.add_item(item, price)
#             elif choice == '2':
#                 item = input("Enter the name of the item to remove: ")
#                 self.remove_item(item)
#             elif choice == '3':
#                 self.display_cart()
#             elif choice == '4':
#                 self.calculate_total()
#             elif choice == '5':
#                 print("Exiting the cart system.")
#                 break
#             else:
#                 print("Invalid option, please choose between 1 and 5.")

# # Create a shopping cart instance and start the menu
# cart = ShoppingCart()
# cart.context_menu()

##########################################################################################################################################

# Class representing a single item in the cart
# class Item:
#     def __init__(self, name, description, price):
#         self.name = name
#         self.description = description
#         self.price = price
    
#     def __str__(self):
#         return f"{self.name} - {self.description} - ${self.price:.2f}"

# # Class representing the shopping cart
# class Cart:
#     def __init__(self):
#         self.items = []
    
#     def add_item(self, item):
#         """Adds an item to the cart."""
#         self.items.append(item)
#         print(f"Added '{item.name}' to the cart for ${item.price:.2f}.")
    
#     def remove_item(self, item_name):
#         """Removes an item from the cart by name."""
#         for item in self.items:
#             if item.name.lower() == item_name.lower():
#                 self.items.remove(item)
#                 print(f"Removed '{item_name}' from the cart.")
#                 return
#         print(f"Item '{item_name}' not found in the cart.")
    
#     def display_cart(self):
#         """Displays the contents of the cart."""
#         if not self.items:
#             print("Your cart is empty.")
#             return
#         print("Items in your cart:")
#         for idx, item in enumerate(self.items, 1):
#             print(f"{idx}. {item}")
    
#     def calculate_total(self):
#         """Calculates the total cost of the cart."""
#         total = sum(item.price for item in self.items)
#         print(f"Total cost of your cart: ${total:.2f}")

# # Class that acts as the interface for the user
# class ShoppingCartApp:
#     def __init__(self):
#         self.cart = Cart()
    
#     def show_menu(self):
#         """Displays the context menu for user interaction."""
#         while True:
#             print("\n--- Flipkart Cart Menu ---")
#             print("1. Add item to cart")
#             print("2. Remove item from cart")
#             print("3. Display cart")
#             print("4. Calculate total cost")
#             print("5. Exit")
            
#             choice = input("Choose an option (1-5): ")
            
#             if choice == '1':
#                 self.add_item_to_cart()
#             elif choice == '2':
#                 self.remove_item_from_cart()
#             elif choice == '3':
#                 self.cart.display_cart()
#             elif choice == '4':
#                 self.cart.calculate_total()
#             elif choice == '5':
#                 print("Exiting the cart system. Thank you for shopping with Flipkart!")
#                 break
#             else:
#                 print("Invalid option, please choose between 1 and 5.")
    
#     def add_item_to_cart(self):
#         """Handles adding a new item to the cart."""
#         item_name = input("Enter the name of the item: ")
#         item_description = input("Enter the description of the item: ")
#         try:
#             price = float(input("Enter the price of the item: $"))
#             item = Item(item_name, item_description, price)
#             self.cart.add_item(item)
#         except ValueError:
#             print("Invalid price. Please enter a valid number.")
    
#     def remove_item_from_cart(self):
#         """Handles removing an item from the cart."""
#         item_name = input("Enter the name of the item to remove: ")
#         self.cart.remove_item(item_name)

# # Run the application
# if __name__ == "__main__":
#     app = ShoppingCartApp()
#     app.show_menu()


###################################################################################


#  icc:


#     a="India"
#     b="Pakistan"

#     def xyz(self):
#         print("team 1 : ",self.a)
#         print("team 2 : ",self.b)

#     def add(self,c,d):
#         return(c+d)
    
# x=icc()

# print(x.add(10,20))
# x.xyz()

# class icc:

#     a="India"
#     b="Pakistan"

#     def xyz(self):
#         print("team 1 : ",self.a)
#         print("team  2 : ",self.b)

#     def add(self,c,d):
#         return(c+d)

# x=iccclass


#Regular expression 

import re

# xyz=r'^(?=.*[A-Z0-9])+\$%+@(?=.*[a-z])\.[a-z]{2,3}\$'

xyz=r'^[a-zA-Z0-9]+[.-_]*[a-zA-Z0-9]*@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$'


x=["bojugu2524@gmail.com","Divakar$%@gmail.com","Kevinmathew1217@gmail.com"]


if re.match(xyz,x):
    print(f"{x}" "Valid E-mail")
else:
    print(f"{x}" "Invalid E-mail")