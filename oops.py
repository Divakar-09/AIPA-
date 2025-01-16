# class AI:
#     institute="NSTI"

#     def __init__(self,name,age,address):
#         self.name= name
#         self.age= age
#         self.address=address

# students=AI("Divakar",19,"HYD")

# print(f'{students.name},{students.age},{students.address}')

##############################################################################

# class NSTI:
#     trades="NSTI"

#     def __init__(self,trade,students,pc):
#         self.trade=trade
#         self.students=students
#         self.pc=pc

# trade1=NSTI("AI",21,16)
# trade2=NSTI("CSA",40,40)
# trade3=NSTI("CHNM",30,27)

# print(trade1.trades)
# print(f"1. {trade1.trade},{trade1.students},{trade1.pc}")
# print(f"2. {trade2.trade},{trade2.students},{trade2.pc}")
# print(f"3. {trade3.trade},{trade3.students},{trade3.pc}")

##############################################################################

# class states:

#     a="hyderabad"
#     b="mumbai"

#     def xyz(self):
#         print("Hello : ",self.a)
#         print("Hii : ",self.b)

#     def abc(self):
#         print("All the states.")

#     def add(self,c,d):
#         return(c+d)

# x=states()

# print(f"{x.a},{x.b}")
# print(x.add(10,20))
# x.xyz()
# x.abc()

##############################################################################


# class wallet:
     
#     def __init__(self,name,balance=0):
#         self.name=name
#         self.balance=balance

#     def add_money(self,money):
#         if money>0:
#             self.balance +=money
#             print(f'money added : {money} new balance : {self.balance }')
#         else:
#             print("Enter a valid amount.")
    
#     def spend(self,money):
#         if money > self.balance:
#             print("Insufficient balance.")
#         else:
#             original_balance=self.balance
#             self.balance -= money
#             print(f'Spent Amount :  {money} from {original_balance} remaining balance : {self.balance} ')

#     def check(self):
#         print(f'{self.name} balance is: {self.balance}')

# x=wallet("Divakar",20)
# y=wallet("Varun",50)

# x.add_money(100)
# y.add_money(100)

# x.spend(60)
# y.spend(60)

# x.check()
# y.check()

#################################################################################################################

# class flipkart:
#     def __init__(self,name,phone):
#         self.name=name
#         self.__item=[]
#         self.phone=phone

#     def add_item(self,i_name,price):
#         self.__item.append({'name':i_name,'price':price})
#         print(f'Added {i_name} to list with price {price}')

#     def remove(self,i_name):
#         for item in self.item:
#             if item['name']==i_name:
#                 self.item.remove(item)
#                 print(f'Removed{i_name}')
#                 return
#         print(f'{i_name}not found')

#     def display(self):
#         if self.item:
#             print(f'cart for {self.name}')
#             for item in self.item:
#                 print(f'{item['name']} : {item['price']}')
#             else:
#                 print("Cart is Empty.")

# x=flipkart("Divakar")
# y=flipkart("Varun")

# x.add_item("mobile",85000)
# y.add_item("laptop",32000)

# x.display()
# y.display()


############################################################################

# class icc:

#     a="India"
#     b="Pakistan"
#     z="icc champions trophy final"

#     def xyz(self):
#         print(self.z)
#         print("team 1 : ",self.a)
#         print("team 2 : ",self.b)


# team1=icc()

# x=icc()
# x.xyz()


##################################################################

class Tournament:

    def __init__(self):
        self.teams={
            "team india":["Rohit Sharma","Virat Kohli","shreyas iyer","shubman gill","surya kumar yadav","ishan kishan","ravindra  jadeja","jasprit bumrah","mohammad shami","mohammad sirja","kuldeep yadav"],
            "team pakistan":["Babar Azam" , "Mohammad Rizwan", "Usman Khan", "Fakhar Zaman", "Imad Wasim", "Iftikhar Ahmed", "Shadab Khan", "Shaheen Afridi", "Naseem Shah", "Mohammad Amir", "Haris Rauf"]
            }        
        
    def players(self,team_name):
        if team_name in self.teams:
            print("\n players of {team_name}:")
            for index, player in enumerate(self.teams[team_name],start=1):
                print(f'{index}.{player}')
        else:
            print("No Data Available")

Teams=Tournament()

team_name=input("enter the team name: ")
Teams.players

