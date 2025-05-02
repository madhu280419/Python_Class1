#Bank account balance protection

# class bankaccount:
#     def __init__(self,owner,balance):
#         self.__owner = owner
#         self.__balance = balance
        
#     def get_owner(self):
#         return self.__owner
    
#     def set_owner(self,name):
#         self.__name = name
        
#     def get_balance(self):
#         return self.__balance
    
#     def set_balance(self,new_balance):
#         if new_balance >= 0:
#             self.__balance = new_balance
#         else:
#             print("Invalid balance")
            
# ac = bankaccount("Madhu", 1000)
# print(ac.get_owner())
# #print(ac.get_balance())
# ac.set_balance(1500)
# print(ac.get_balance())

    
    
# Age Validation

# class Person:
#     def _init_(self, name, age):
#         self.__name = name
#         self.__age = age

#     def get_name(self):
#         return self.__name

#     def set_name(self, name):
#         self.__name = name

#     def get_age(self):
#         return self.__age

#     def set_age(self, age):
#         if age >= 0:
#             self.__age = age
#         else:
#             self.__age = "Invalid age"

#     def display(self):
#         print(f"Name: {self._name}, Age: {self._age}")

# p = Person("jaunt", 31)
# p.display()

# p.set_age(26)
# p.set_name("madhu")  
# p.display(set)  



# class BankAccount:
#     def _init_(self, acc_no, holder, balance=0):
#         self.__accountNumber = acc_no
#         self.__accountHolder = holder
#         self.__balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount

#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             self.__balance = "Insufficient funds"

#     def get_balance(self):
#         return self.__balance
#     def display(self):
#         print("Account number: ",self._accountNumber,"account holder name:",self._accountHolder)
    

# ac = BankAccount("12345", "madhu", 1000)
# ac.display()
# print("balance:",ac.get_balance())

# ac.deposit(500)
# ac.withdraw(200)
# print("Balance:", ac.get_balance())


    
class Student:
    def __init__(self, roll, name, marks):
        self.rollNumber = roll
        self.name = name
        self.__marks = marks
        print("Student roll:", self.rollNumber, "Student name:", self.name)

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        if value >= 0:
            self.__marks = value
        else:
            print("Error: Marks can't be negative.")


student = Student(420, "mad", 75)
print("Student's marks:", student.marks)

#student.marks = -5 
student.marks = 95   
print("Updated marks:", student.marks)

            
        

        
    