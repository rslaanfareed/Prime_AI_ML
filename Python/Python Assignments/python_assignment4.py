#Question 1: classes and objects
'''
class BankAccount:
    def __init__(self,acc_num,owner_name,balance):
        print("Account Created\n")
        self.acc_num=acc_num
        self.owner_name=owner_name
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print(f"RS.{amount} deposited\n")

    def withdraw(self,amount):
        self.balance-=amount
        print(f"RS.{amount} withdrawn\n")

    def check_balance(self):
        print(f"Balance= {self.balance}\n")

ac1=BankAccount(101,"ali",1000)

print("Checking balance")
ac1.check_balance()

print("Depositing money")
ac1.deposit(2000)

print("Checking balance")
ac1.check_balance()

print("Withdrawing money")
ac1.withdraw(500)

print("Checking balance")
ac1.check_balance()

'''


#Question 2
'''
class Book:
    def __init__(self,title,author,rev_list):
        print("\nNew book")
        self.title=title
        self.author=author
        self.rev_list=rev_list

    def add_review(self):
        rev=input("Enter review: ")
        self.rev_list.append(rev)
        print("Review added")

    def count_reviews(self):
        print(f"Total reviews: {len(self.rev_list)}")
    
    def display_reviews(self):
        print("\nDisplaying all reviews:")
        i=1
        for r in self.rev_list:
            print(f"Review:{i}={r}")
            i+=1

b1=Book("Fire and Blood","George Martin",[])
print(f"Book name:{b1.title} Author:{b1.author}")
b1.count_reviews()
b1.add_review()
b1.count_reviews()
b1.add_review()
b1.count_reviews()
b1.display_reviews()
print(type(b1.rev_list))
'''

#Question 3: Encapsulation
'''
class Student:
    def __init__(self,name,roll,marks):
        while name.strip()=="":
            print("name cannot be empty")
            name=input("Enter name again: ")
            
        while (roll<1 or roll>100):
            print("Roll no must be 1-100")
            roll=int(input("Enter roll no again: "))
        
        while (marks<0):
            print("Marks cannot be nagative")
            marks=int(input("Enter marks again: "))
            
        
        self.__name=name
        self.__roll=roll
        self.__marks=marks
        
    
    def get_name(self):
        return self.__name
    def get_marks(self):
        return self.__marks
    def get_roll(self):
        return self.__roll
        
    def set_roll(self,roll):
        while (roll<1 or roll>100):
            print("Roll no must be 1-100")
            roll=int(input("Enter roll no again: "))
        
        self.__roll=roll
        print("Roll no entered")

    def set_marks(self,marks):
        while (marks<0):
            print("Marks cannot be nagative")
            marks=int(input("Enter marks again: "))
        
        self.__marks=marks
        print("Marks entered")
    def set_name(self,name):
        while name.strip()=="":
            print("name cannot be empty")
            name=input("Enter name again: ")
    
        self.__name=name
        print("Name entered")
        
try:
    s1=Student("",0,-9)

    print(s1.get_name())
    print(s1.get_roll())
    print(s1.get_marks())

    s1.set_name("")
    s1.set_roll(00)
    s1.set_marks(-8)

    print(s1.get_name())
    print(s1.get_roll())
    print(s1.get_marks())
except:
    print("error")
'''


#Question 4: function overriding
'''
import math
class Shape:
    def area(self):
        print("shape")
        

class Circle(Shape):
    def __init__(self,radius):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        else:
            self.radius=radius
    def area(self):
        return math.pi*self.radius**2

class Rectangle(Shape):
    def __init__(self,l,w):
        if l>0 and w>0:
            self.l=l
            self.w=w
        else:
            raise ValueError("length and width must be a positive number")
    def area(self):
        return self.l*self.w

class Triangle(Shape):
    def __init__(self,a,b):
        if a>0 and b>0:
            self.a=a
            self.b=b
        else:
            raise ValueError("Triangle a and b must be positive numbers")
    def area(self):
        return (self.a*self.b)/2
try:
    shapes = [
        Circle(0),
        Rectangle(3,4),
        Triangle(3,4)
    ]

    for shape in shapes:
        print(f"{shape.area():.2f}")
except ValueError as e:
    print(e)

'''

#Question 5: Inheritance
'''
class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display(self):
        print(self.brand)
        print(self.model)

class Car(Vehicle):
    def __init__(self,brand,model,seats):
        super().__init__(brand,model)
        self.seats=seats
    def display(self):
        super().display()
        print(self.seats)

class Bike(Vehicle):
    def __init__(self,brand,model,engine_cc):
        super().__init__(brand,model)
        self.engine_cc=engine_cc
    def display(self):
        super().display()
        print(self.engine_cc)

v=Vehicle("toyota",2022)
v.display()

c=Car("Honda",2020,4)
c.display()

b=Bike("Suzuki",2024,1300)
b.display()
'''

#Question 6: Abstraction

'''
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @abstractmethod
    def calculate_salary(self):
        pass

class Intern(Employee):
    def __init__(self,name,salary):
        super().__init__(name,salary)
    def calculate_salary(self):
        return self.salary*1.1

class FullTimeEmployee(Employee):
    def __init__(self,name,salary,bonus):
        super().__init__(name,salary)
        self.bonus=bonus
    def calculate_salary(self):
        return self.salary*1.2+self.bonus

class ContractEmployee(Employee):
    def __init__(self,name,salary,contract_months):
        super().__init__(name,salary)
        self.contract_months=contract_months
    def calculate_salary(self):
        return self.salary*self.contract_months

i=Intern("ali",30000)
print(f"{i.calculate_salary():.2f}")

f=FullTimeEmployee("Ahmad",60000,10000)
print(f"{f.calculate_salary():.2f}")

c=ContractEmployee("Nouman",50000,6)
print(f"{c.calculate_salary():.2f}")
'''

#Question 7: Constructor Overloading (with Default Parameters) 
'''
class Person:
    def __init__(self,name=None,age=None,address=None):
        self.name=name
        self.age=age
        self.address=address

    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}\nAddress: {self.address}")

p1=Person()
p1.display()

p2=Person("Ali")
p2.display()

p3=Person("Ahmad",19)
p3.display()

p4=Person("nouman",23,"ABC")
p4.display()
'''


#Question 8: Instance and class Attributes
'''
class Player:
    player_count=0
    def __init__(self,name,level):
        self.name=name
        self.level=level
        Player.player_count+=1

p=Player("ali",1)
p2=Player("Ahmad",2)
print(Player.player_count)
'''


#Question 9: Multiple Inheritance
'''
class Herbivore:
    def __init__(self,eat_grass):
        self.eat_grass=eat_grass

    def eat(self):
        print("Eating grass")

    def display(self):
        print(f"eats grass: {self.eat_grass}")
    
class Carnivore:
    def __init__(self,eat_meat):
        self.eat_meat=eat_meat

    def eat(self):
        print("Eating meat")

    def display(self):
        print(f"eats meat: {self.eat_meat}")

class Bear(Herbivore,Carnivore):
    def __init__(self,eat_grass,eat_meat):
        Herbivore.__init__(self,eat_grass)
        Carnivore.__init__(self,eat_meat)

    def display(self):
        Herbivore.display(self)
        Carnivore.display(self)

    def eat(self):
        Herbivore.eat(self)
        Carnivore.eat(self)

print("\nHerbivore")
h=Herbivore(True)
h.display()
h.eat()

print("\nCarnivore")
c=Carnivore(True)
c.display()
c.eat()

print("\nBear")
b=Bear(True,True)
b.display()
b.eat()
'''


#Question 10: oop chat system
class Message:
    message_counter=0

    def __init__(self,sender,content):
        self.sender=sender
        self.content=content
        Message.message_counter+=1
        self.id=Message.message_counter
    
    def __str__(self):
        return f"({self.id}){self.sender.username}:{self.content}"

class User:
    def __init__(self,username):
        self.username=username
        self.chatroom=None

    def join_chatroom(self,chatroom):
        if self.chatroom:
            print(f"{self.username} already in chatroom")
        else:
            chatroom.add_user(self)
            self.chatroom=chatroom
            print(f"{self.username} joined {chatroom.name}")
        
    def leave_chatroom(self):
        if not self.chatroom:
            print(f"{self.username} is not in any chatroom.")
        
        else:
            self.chatroom.remove_user(self)
            print(f"{self.username} left {self.chatroom.name}") 
            self.chatroom=None

    def send_message(self,content):
        if not self.chatroom:
            print(f"{self.username} cannot send a message: Not in the chatroom")

        else:
            self.chatroom.broadcast(self,content)
class Chatroom:
    def __init__(self,name):
        self.name=name
        self.users=[]
        self.messages=[]

    def add_user(self,user):
        self.users.append(user)

    def remove_user(self,user):
        self.users.remove(user)

    def broadcast(self,sender,content):
        message=Message(sender,content)
        self.messages.append(message)
        print(message)

    def show_chat_history(self):
        print(f"Chat history of: {self.name}")
        for msg in self.messages:
            print(msg)
            print()

room=Chatroom("Chat Room")
u1=User("Ali")
u2=User("Nouman")
u3=User("ahmad")

u1.join_chatroom(room)
u2.join_chatroom(room)

u1.send_message("hello everyone")
u2.send_message("hello whats up")

u3.join_chatroom(room)
u3.send_message("hellllo")

room.show_chat_history()

u1.leave_chatroom()
u2.leave_chatroom()
u3.leave_chatroom()

    

