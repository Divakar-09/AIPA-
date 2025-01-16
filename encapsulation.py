# class AI:
#     def __init__(self):
#         self.name="Divakar"
        # self._name="Divakar"
        # self.__name="Divakar"

    # def disp(self):
    #     print(self.name)

# x=AI()
# x.disp()
# print(x.name)

####################################################

# class NSTI:
#     def __init__(self):
#         self._trade="AI"

# class CTS(NSTI):
#     def disp(self):
#         print(self._trade)

# x=CTS()
# x.disp()

###################################################

# class NSTI:
#     def __init__(self):
#         self.__aadhar="xxxxxxxxxxxx"

#     def disp(self):
#         print(self.__aadhar)

# class CTS(NSTI):
#     def disp(self):
#         print(self.__aadhar)
    
# x=CTS()
# print(x.__aadhar)

#################################################

# class Person:
#     def __init__(self, name):
#         self.name = name  

#     def disp(self):  
#         print(f"Hello, {self.name}")

# person = Person("Divakar")


# print(person.name)  

# person.disp()  

#############################################\

# class Hospital:
#     def __init__(self):
#         self.__patients=[]

#     def add(self,patient):
#         self.__patients.append(patient)
#         print(f'patient {patient} added ')

#     def remove(self,patient):
#         if patient in self.__patients:
#             self.__patients.remove(patient)
#             print(f'patient {patient} removed from list. ')

#         else:
#             print(f'{patient} not found. ')
    
#     def disp(self):
#         for patient in self.__patients:
#             print(patient)

# x=Hospital()

# x.add("Divakar ")
# x.add("varun ")
# x.add("venkatesh ")
# x.remove("venkatesh ")
# x.disp()

###############################################

# class NSTI:

#     def __init__(self):
#         self.__students=input([])
#         print(self.__students)

#     def add(self,student):
#         self.__students.append(student)
#         print(f'NSTI student {student} added ')

#     def remove(self,student):
#         if student in self.__students:
#             self.__students.remove(student)
#             print(f'NSTI student {student} removed from list. ')

#         else:
#             print(f'{student} not found. ')

#     def disp(self):
#         for student in self.__students:
#             print(student)

#     def main():
        
#         choise1 == "1":
#         choose2 == "2":
#         choose3 == "3":
        
# x=NSTI()

# x.add("DIvakar")
# x.add("Varun")
# x.add("Venkatesh")

# x.remove("Varun")
# x.disp()

##############################################

# class Ai: 

#     def __init__(self):
#         self.name=None
#         self.__grade=None

#     def details(self):
#         self.name=input("Enter name: ")
#         while True:
#             grade=int(input("enter grade :"))
#             if 0<=grade<=100:
#                 self.__grade=grade
#                 break
#             else:
#                 print("Enter grade (0--100): ")

#     def disp(self):
#         print("Studnets details :")
#         print(f'Name:{self.name}')
#         print(f'Grade :{self.__grade}')

# x=Ai()

# x.details()


# x.disp()


# class Demo:
#     def method():
#         print("hello")

# object=Demo()
# object.method()