# class student:
#     subject="python"
#     year="3rd"
#     college="ABC"
# st1=student()
# st2=student()
# print(st1)
# print(st2)
# print(st1.subject)
# st1.subject="Java"
# print(st1.subject)

# class Student:
#     college="ABC"
#     PI=3.14
#     def __init__(self,name,college):
#         self.name=name
#         self.college=college
#         self.PI=3.13
#         print(self.name,self.college,self.PI,Student.PI)
    # def display(self,name):
    #     print(self.name)    
    
# s1=Student("Ali","python")
# s2=Student("Arslan","java")
# print(s1.name)
# print(s2.subject)
# s1=Student("ahmad","java")
# Student.college="acb"
# print(Student.college)
# s1.display("ali")
# print(Student.college)
# s1=Student("ali","bsc")


# #PRODUCT STORE PRACTICE PROBLEM
# class Product:
#     count=0
    
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#         Product.count+=1
#     def get_info(self):
#         print(f"Product name: {self.name}\nProduct Price: {self.price}")
    
#     @classmethod
#     def total_products(cls):
#         print(f"Total Products are {cls.count}")

#     @staticmethod
#     def calc_discount(price,discount):
#         discounted_price=price-price*discount/100
#         print(f"Discount: {discount}%")
#         print(f"Final price: {discounted_price}\n")

# p1=Product("Phone",40000)
# p2=Product("Laptop",80000)
# p3=Product("Pen",50)


# p1.get_info()
# p1.calc_discount(p1.price,10)

# p2.get_info()
# p2.calc_discount(p2.price,10)

# p3.get_info()
# p3.calc_discount(p3.price,10)

# Product.total_products()


# class student:

#     college="abc"
#     @classmethod
#     def change_college(cls,new_college):
#         print(f"old college: {cls.college}")
#         cls.college=new_college
#         print(f"new college: {cls.college}")

#     def __init__(self,name):
#         self.name=name
    
#     def display(self):
#         print(self.name)
#         print(self.college)

# s=student("ali")
# s2=student("ahmad")
# s.change_college("cool")
# print(s.college)
# print(student.college)




#METHOD CALL RULES-----------------------------------------------------------------

# #accessing instance method using object is ok
# s.display()

# #accessing instance method using class name is also ok
# student.display(s)

# #accessing class method using instance is ok
# s.change_college("ABC")

# #accessing class method using class name is also ok
# student.change_college("DEF")



#ATTRIBUTE ACCESS RULES-------------------------------------------------------------

# #we CAN access instance attributes using instance name
# print(s.name)

# #we CANNOT access instance attributes using class name
# print(student.name)

# #we CAN access class attributes using class name
# print(student.college)

# #we CAN also access class attribute of a specific instance using instance name
# print(s.college)


#ENCAPSULATION-------------------------

# class BankAccount:
#     def __init__(self,name,coin,balance):
#         #public attribute
#         self.name=name
#         #protected attribute              
#         self._coin=coin 
#         #private attribute
#         self.__balance=balance

#         #GETTER
#     def get_balance(self):               
#         return self.__balance

#         #SETTER
#     def set_balance(self,new_balance):   
#         self.__balance=new_balance

# #object b created
# b=BankAccount("ali",20,20_000)

# #public attribute printed
# print(b.name)

# #protected attribute printed(NOT RECOMMENDED)
# print(b._coin)

# #private attribute printed(NOT RECOMMENDED)
# print(b._BankAccount__balance)

# #access private att using getter
# print(b.get_balance())

# #change private att using setter
# b.set_balance(30_000)

# #access again to confirm change
# print(b.get_balance())



# # INHERITENCE--------------------------------

# class Employee:
#     start_time="9am"
#     end_time="5pm"
    
#     def change_end_time(self,new_end_time):
#         self.end_time=new_end_time


# class Admin(Employee):
#     def __init__(self,role):
#         self.role=role

# class accountant(Admin):                     #Multilevel Inheritence
#     def __init__(self,salary,role):
#         super().__init__(role)
#         self.salary=salary

# t=Teacher("ali","DBS")
# t.change_end_time("2pm")
# print(t.start_time,t.end_time,t.name,t.subject)

# a=Admin("Manager")
# print(a.role,a.start_time,a.end_time) 

# a1=accountant(200_000,"CA")
# print(a1.role,a1.salary,a1.start_time,a1.end_time)


# #Multiple inheritence------------
# class Teacher:
#     def __init__(self,salary):
#         self.salary=salary

# class student:
#     def __init__(self,gpa):
#         self.gpa=gpa

# class TA(Teacher,student):
#     def __init__(self,salary,gpa,name):
#         super().__init__(salary)
#         student.__init__(self,gpa)
#         self.name=name

# ta1=TA(50_000,3.5,"ali")
# print(ta1.name,ta1.salary,ta1.gpa)
# print(TA.mro())


#Multilevel inheritance example-----------------------------------------------
#Hospital management system

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def display_person(self):
        print(f"Name: {self.name}\nAge: {self.age}")

class Doctor(Person):
    def __init__(self,name,age,specialization):
        super().__init__(name,age)
        self.specialization=specialization
    def display_doctor(self):
        super().display_person()
        print(f"Specialization: {self.specialization}")


class Surgeon(Doctor):
    def __init__(self,name,age,specialization,surgeries_completed):
        super().__init__(name,age,specialization)
        self.surgeries_completed=surgeries_completed

    def display_surgeon(self):
        super().display_doctor()
        print(f"Surgeries completed:{self.surgeries_completed}")

p=Person("ali",25)
p.display_person()

d=Doctor("ahmad",34,"children")
d.display_doctor()

s=Surgeon("abc",45,"def",12)
s.display_surgeon()



#Multiple inheritence example


class Camera:
    def __init__(self,mp):
        self.mp=mp

    def take_pic(self):
        print(f"Picture taken using {self.mp}MP Camera")

class MusicPlayer():
    def __init__(self,songs):
        self.songs=songs
    def play_music(self):
        print(f"Playing {self.songs} songs")

class Smartphone(Camera,MusicPlayer):
    def __init__(self,mp,songs,brand):
        Camera.__init__(self,mp)
        MusicPlayer.__init__(self,songs)
        self.brand=brand

    def display_phone(self):
        print(f"Brand: {self.brand}")
        print(f"Camera: {self.mp}MP")
        print(f"Songs: {self.songs}")

sp=Smartphone("108",23,"Samsung")
sp.display_phone()
sp.take_pic()
sp.play_music()