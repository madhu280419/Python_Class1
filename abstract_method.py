# from abc import ABC,abstractmethod
# class Animal(ABC):
#     @abstractmethod
#     def eat(self):
#         pass
#     @abstractmethod
#     def sound(self):
#         pass
# class Dog(Animal):
#     def eat(self):
#         print("dog is eating")
#     def sound(self):
#          print("BOW BOW")
# obj = Dog()
# print(obj.eat())

#Abstract method for vehicle 

# from abc import ABC,abstractmethod

# class vehicle(ABC):
    
#     @abstractmethod
#     def start_engine(self):
#         pass
    
# class car(vehicle):
    
#     def start_engine(self):
#         return "car engine started"
    
# x = car()
# print(x.start_engine())

# Abstract Method for Payment Systems.

from abc import ABC,abstractmethod

class payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
    
class creditcardpayment(payment):
    def pay(self,amount):
        return f"paid {payment} using AMEX card"
    
y = creditcardpayment()
print(y.pay(150))


#Employee class

from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
       pass
    
    def show_details(self):
        print("Employee details displayed.")

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return "Full-time salary calculated."

class Freelancer(Employee):
    def calculate_salary(self):
        return "Freelancer salary calculated."

emp1 = FullTimeEmployee()
print(emp1.calculate_salary())
emp1.show_details()

emp2 = Freelancer()
print(emp2.calculate_salary())
emp2.show_details()


#Device Class 
from abc import ABC,abstractmethod
class device(ABC):
    @abstractmethod
    def power_on(self):
        pass
    
    def power_off(self):
        print("Device is shutting down")
        
class laptop(device):
    def power_on(self):
        print("power on")
        
class smartphone(device):
    def power_on(self):
        print("phone power on")
        
l = laptop()
l.power_on()
l.power_off()

s = smartphone()
s.power_on()
s.power_off()


#withdraw money
from abc import ABC,abstractmethod

class account(ABC):
    @abstractmethod
    def withdraw(self,amount):
        pass
    
    def deposit(self,amount):
        print(f"deposited {amount}")
        
class savingsaccount(account):
    def withdraw(self,amount):
        print(f"withdrawn {amount} from savings account")
        

class currentaccount(account):
    def withdraw(self,amount):
        print(f"withdrawn {amount} from current account")
        
s = savingsaccount()
s.deposit(500)
s.withdraw(250)

c = currentaccount()
c.deposit(2046)
c.withdraw(1027)
        
        
        
    




