#formatt

# try:
#     result=10/0
# except ZeroDivisionError:
#     print("number can't be divided by zero ")

# result=10/0
# print(result)

##################################################

# try:
#     varun=10/
# except ZeroDivisionError:
#     print("you cant divide a number by zero")
# else:
#     print("the result is :", varun)
# finally:
#     print("it will print regardless of whether the issue is raised or not")

####################################################

# def check_age(age):
#     if age<18:
#         raise ValueError("age must be 18")
#         return "you are allowed to vote"

# try:
#     check_age(20)
# except ValueError as ve:
#     print(ve) 
# else:
#     print("you are eligible")

#################################################

# try:
#     num=int(input("enter a number"))
#     result=10/num
# except ValueError:
#     print("Invalid Input")
# except ZeroDivisionError:
#     print("you can't divide by zero")
# else:
#     print(result)
# finally:
#     print("you are done")

################################################


# class GasKhatamError(Exception):
#     pass
# class TeaPowderError(Exception):
#     pass
# class UnexpectedGuestError(Exception):
#     pass

# def prepare_te():
#     try:
#         gas=get_gas()
#         powder=get_powder()
#         serve_tea(powder)
#     except GasKhatamError:
#         print("oops,aipoindhi.")
#     except TeaPowderError:
#         print("aipaaye")
#     except UnexpectedGuestError:
#         print("we have more Guest")
#     finally:
#         print("tea is prepared ,how is it ")


# def get_gas():
#     user_input=input("enter 'yes' if the gas is finished, otherwise 'no':").strip().lower()
#     if user_input=='no':
#         raise GasKhatamError("oops,aipoindhi.")
#     return "gas"

# def get_powder(gas):
#     user_input=input("Enter 'khatm' if the tee powder is finished otherwise 'noi': ").strip().lower()
#     if user_input=='khatm':
#         raise TeaPowderError("tea powder nhi hai .")
#     return "powder"

# def serve_tea(powder):
#     user_input=input("enter 'extra; if there are unexpected guest ,otherwise 'okay':").strip().lower() 


#     if user_input=='extra':
#         raise UnexpectedGuestError("we have more guest that expected ")
#         print("chai is ready ")



\
