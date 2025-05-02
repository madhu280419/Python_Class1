#1.Create a class Person with attributes name and age. Inherit a class Employee that adds salary. Write a method to display all attributes.
class person:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def display(self):
        print(f"Name:{self.name}")
        print(f"age:{self.age}")
        print(f"salary:{self.salary}")
details = person("Jaunty", 30, 8000)
details.display()

#2.Define a class Animal with a method speak(). Inherit it in class Dog and override the speak() method to print "Bark".
class Animal:
    def speak(self):
        print("animal sound")
class Dog(Animal):
    def speak(self):
        print("bark")
details = Dog()
details.speak()



#3.Make a class Vehicle with a method info() that prints "This is a vehicle". Create a class Car that inherits Vehicle and adds a method brand() which prints the car's brand.
class vehicle:
    def info(self):
        print("This is a vehicle")
class car(vehicle):
    def brand(self):
        print("brand: Toyota" )
my_car = car()
my_car.info()
my_car.brand()

#MULTIPLE INHERITENCE
#Create two classes Writer and Editor, each with a method role(). Inherit a class Author from both and override role() to describe an author’s combined role.

class writer:
    def role(self):
        print("I am a writer")
class editor:
    def role(self):
        print("I am a editor")
class author(writer,editor):
    def role(self):
        print("i am an author")
details = author()
details.role()

#Define a class MathTeacher with a method teach(), and another class BasketballCoach with train(). Make a SchoolStaff class that inherits both and uses both methods.

class mathteacher:
    def teach(self):
        print("i teach maths ")
class basketballcoach:
    def train(self):
        print("basket ball training")
class schoolstaff(mathteacher,basketballcoach):
    def role(self):
        print("schoolstaff")
staff = schoolstaff()
staff.teach()
staff.train()

#Create classes A and B with a method say() that prints different messages. Inherit class C(A, B) and call say(). What gets printed?
 
class A:
    def say(self):
        print("NOTHING")
class B:
    def say(self):
        print("SOMETHING")
class C(A,B):
     pass
alpha = C()
alpha.say()


#Write a program that demonstrates method resolution order (MRO) using multiple inheritance. Show how Python decides which method to call.

class X:
    def show(self):
        print("from X")
class Y(X):
    def show(self):
        print("from Y")
class Z(Y):
    def show(self):
        print("from Z")
class M(Z):
    pass
res = M()
res.show()
print(M.mro())


class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def information(self):
        print(f"name {self.name}")
        print(f"age{self.age}")
details = person("madhu",25)
details.information()
    
#Simulate a class Person and class Athlete. Make a subclass StudentAthlete that inherits from both, and demonstrate accessing attributes/methods from both base classes      
class person:
    def __init__(self,name):
        self.name = name
    def show_name(self):
        print(f"name: {self.name}")
class athlete:
    def __init__(self,sport):
        self.sport = sport
    def show_sport(self):
        print(f"sport:{self.sport}")
class studentathlete(person,athlete):
    def __init__(self,name,sport):
        person.__init__(self,name)
        athlete.__init__(self,sport)
s = studentathlete("Jaunty", "cricket")
s.show_name()
s.show_sport()

#Create a class Grandparent with a method history(). Inherit Parent from it and add legacy(). Inherit Child from Parent and add future(). Call all three methods from a Child object.

class grandparents:
    def history(self):
        print("Past")
class parent(grandparents):
    def legacy(self):
        print("family legacy")
class child(parent):
    def future(self):
        print("Future goals")
ch = child()
ch.history()
ch.legacy()
ch.future()

#Make a base class Device with a method specs(). Inherit Phone from Device, and Smartphone from Phone. Override specs() at each level and see which one gets called.

class device:
    def specs(self):
        print("generic specs")
class phone(device):
    def specs(self):
        print("calling and texting")
class smartphone(phone):
    def specs(self):
        print("apps,internet,camera")
s = smartphone()
s.specs()

#Design a multilevel class structure: Organism -> Animal -> Human, each with a method info(). Override the method at each level and call info() from a Human object.

class organism:
    def info(self):
        print("Living organism")
class animal(organism):
    def info(self):
        print("animal traits")
class human(animal):
    def info(self):
        print("human specific traits")
h = human()
h.info()

#Implement a multilevel inheritance where the base class University has details like name and location, College inherits it with department info, and Student inherits College with personal details. Print complete student info.

class university:
    
    def __init__(self,university_name,location):
        self.university_name = university_name
        self.location = location
        
class college(university):
    
    def __init__(self,university_name,location,department):
        super().__init__(university_name,location)
        self.department = department
        
class student(college):
    
    def __init__(self,university_name,location,department,student_name,roll_number):
        super().__init__(university_name,location,department)
        self.student_name = student_name
        self.roll_number = roll_number
        
    def display_information (self):
        print(f"university : {self.university_name}")
        print(f"location : {self.location}")
        print(f"department : {self.department}")
        print(f"student name : {self.student_name}")
        print(f"roll_number : {self.roll_number}")
        
s = student("YSU","YOUNGSTOWN","CSI","MADHU","Y00859770")
s.display_information()


# Write a multilevel inheritance example with a class A having a method greet(), B(A) adding introduce(), and C(B) adding describe(). Call all three methods from an object of class C.        

class A:
    def greet(self):
        print("i am from class A")
class B(A):
    def introduce(self):
        print("I am from class B")
class c(B):
    def describe(self):
        print("i am from class C")
obj = c()
obj.greet()
obj.introduce()
obj.describe()

print("hello world")