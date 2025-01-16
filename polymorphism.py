#calling methods of same name usinng function:

# class A:
#     def x(self):
#         return "Hello"
    
# class B:
#     def x(self):
#         return "yess"
    
# def z(q):
#     return q.x()

# r=A()
# t=B()

# print(z(r))
# print(z(t))

#using inheritence:

# class Maths:
#     def area (self):
#         pass
    # def perimeter(self):
    #     pass 


# class Rectangle(Maths):
#     def __init__(self,l,b):
#         self.l=l
#         self.b=b
#     def area(self):
#         return self.l * self.b
    # def perimeter(self):
    #     return  2 * (self.l + self.b)
    

# class Square(Maths):
#     def __init__(self,a):
#         self.a=a
#     def area(self):
#         return self.a * self.a 
    # def perimeter(self):
    #     return 4 * (self.a)



# class Circle(Maths):
#     def __init__(self,r):
#         self.r=r
#     def area(self):
#         return 3.14 * self.r * self.r

        



# x=[Rectangle(5,6),Square(4),Circle(6)]
# for result in x:
#     print(result.area())

# for result in x:
#     print(result.perimeter())



##########################################################################
                                                                                            
# from abc import ABC,abstractmethod

# class NSTI(ABC):
#     @abstractmethod
#     def xyz(self):
#         pass 

# class AI(NSTI):
#     def xyz(self):
#         return " Artificial Intelligence"

# class CHNM(NSTI):
#     def xyz(self):
#         return "Computer Hardware , Networking and maintanance"

# x=[AI(),CHNM()]

# for result in x:
#     print(result.xyz())


##############################################################################

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
    
#     def calculate_area(self):
#         pass 

# class Rectangle(Shape):
#     def __init__(self,l,b):
#         self.l=l
#         self.b=b

#     def calculate_area(self):
#         return self.l * self.b
    
# class Triangle(Shape):
#     def __init__(self,b,h):
#         self.b=b
#         self.h=h

#     def calculate_area(self):
#         return 0.5 * self.b * self.h
    
# class Circle(Shape):
#     def __init__(self,r):
#         self.r=r

#     def calculate_area(self):
#         return 3.14 *self.r * self.r
    

# x=[Rectangle(6,4),Triangle(9,6),Circle(12)]

# for result in x:
#     print(result.calculate_area())
        
        
####################################################################

# from abc import ABC,abstractmethod

# class GameofThrones(ABC):
    
#     @abstractmethod
#     def Kingdoms(self):
#         pass

# class
    
#Abstraction:

from abc import ABC, abstractmethod

class Car(ABC):
    
    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def stop_engine(self):
        pass
    
    @abstractmethod
    def drive(self):
        pass



class SportsCar(Car):
    
    def __init__(self, model):
        self.model = model
        self.engine_started = False
    


    
    def start_engine(self):
        self.engine_started = True
        print(f"Starting the engine of {self.model} sports car.")
    
    def stop_engine(self):
        self.engine_started = False
        print(f"Stopping the engine of {self.model} sports car.")
    
    def drive(self):
        if self.engine_started:
            print(f"{self.model} sports car is now driving.")
        else:
            print("Start the engine first!")



# Create a SportsCar object
my_car = SportsCar("toyota")

# Start the engine
my_car.start_engine()

# Drive the car
my_car.drive()

# Stop the engine
my_car.stop_engine()

     