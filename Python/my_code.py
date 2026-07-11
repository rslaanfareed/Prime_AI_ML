# string="hello ".strip()
# vowel=0;
# consonant=0;
# for ch in string:
#     if (ch=='i' or ch=='a' or ch=='e' or ch=='o' or ch=='u'):
#         vowel+=1
#     else:
#         consonant+=1

# print("Vowels appear", vowel, "times in the string.")
# print("Consonants appear", consonant, "times in the string.")


# for i in range(5):
#     print(i)

# for i in range(2,6):
#     print(i)

# for i in range(2,10,2):
#     print(i)


# #sum of first 5 natural numbers-----------
# count=0
# for i in range(1,6):
#     count=count+i;
#     print(count)
# print("total",count)


# #match case
# color=(input("Enter color "))
# match color:
#     case 'yellow':
#         print("ready")
#     case 'green':
#         print("go")
#     case "red":
#         print("stop")
#     case _:
#         print("wrong color")


# #login system
# username = input("enter username: ")  
# password = input("enter password: ")  
# if (username == "admin" and password == "pass"):  
#     print("log in successful!")  
# else:  
#     if username != "admin":     
#     # NESTING  
#         print("wrong user name, try again.")  
#     else:  
#         print("wrong password, try again.") 


# num=int(input("Enter a number: "))
# if num%5==0:
#     print("The number is divisible by 5")
# else:
#     print("The number is not divisible by 5")



# #odds
# num=int(input("Enter a number: "))
# while num<50:
#     num+=1
#     if num%2==0:
#         continue
#     print(num)
    

# for i in range(1, 3):  
#     for j in range(1, 3):  
#         print(f"({i}, {j})")


# #table of a number
# num=int(input("Enter a number: "))
# i=1
# while i<=10:
#     print(num,"*",i,"=",num*i)
#     i+=1


# #function with default argument
# def sum(a,b=4):
#    return a+b
# print(sum(5))


# #lambda function
# sum=lambda a,b,c: a+b+c
# print(sum(1,2,3))


# #factorial of a number
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         fact = 1
#         for i in range (1, n+1):  
#             fact *= i 
#     return fact

# num=int(input("Enter a number: "))
# print("Factorial of", num, "is", factorial(num))


# #largest of three numbers
# def largest(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>c:
#         return b
#     else:
#         return c
# print("Largest number is", largest(10,20,30))


# #STRINGS-----------------------------------------
# word="hello python "
# print(word[0:19])
# print(word[::3])

# name="Arslan"
# age=19
# print("My name is {} and i am {} years old".format(name,age))


#LISTS----------------------------------------------
# marks=[67,54,76,98,76]
# print(marks)
# print(marks[-3:])

# marks[0]=69


# sliced=marks[0:5]
# print(sliced)

# sum=0
# for i in marks:
#     sum+=i
#     print(i)
# print(f"sum={sum}")
# print(f"average={sum/len(marks)}")

# #LISTS METHODS----------------------------------
# list=[7,2,3,4]
# list.append(5)
# print(list)

# print(list.count(3)) #return count of that value in list
# print(list.index(3)) #return index of the value 

# list.insert(5,2)
# print(list)

# list.sort(reverse=True)
# print(list)
# list.reverse()
# print(list)

# list=[1,4,5,7,8,9]
# x=9
# idx=0
# for val in list:
#     if val==x:
#         print(f"{x} found at {idx}")
#     idx+=1


#TUPLES-----------------------------------------
# tup=(2,3,4,1,6,5,1)
# for i in tup:
    # print(i)

# print(tup.index(3))
# print(tup.count(1))

# #DICTIONARIES-----------------------------------
# d={
#     "name":"arslan",
#     "cgpa": 3.5,
#     "age": 20
# }
# d_keys=d.keys()
# print(d_keys)
# d_values=d.values()
# print(d_values)
# d_items=d.items()
# print(d_items)
# print(d.get("name"))
# d.update({
#     "city":"DGK"
# })
# print(d)



#LIST COMPREHENSION---CREATING NEW LISTS FROM ITERABLES(RANGE,LIST,TUPLES,DICT,ARRAYS...)
# names=("arslan","nouman","haroon")
# list=[i*2 for i in range(5)]
# list =[i for i in names if 'o' in i]
# list=[i for i in range(1,1001) if i%2==0 and i%5==0 and i%3==0 and i%7==0]
# print(list)



#SETS---------------------------------

# num_set={1,2,2,3,4}
# print(num_set)
# print(len(num_set))
# num_list=[1,2,2,3,4]
# list_to_set=set(num_list)
# print(list_to_set)
# num_set.add(7)
# print(num_set)

# s1={1,2,3,4,5}
# s2={4,5,6,7}
# print(f"UNION: {s1.union(s2)}")
# print(f"INTERSECTION: {s1.intersection(s2)}")


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# #QUESTION -----a

# info = [
# ("Alice", "Math"),
# ("Bob", "Science"),
# ("Alice", "Science"),
# ("Charlie", "Math"),
# ("Bob", "Math"),
# ("Alice", "English"),
# ("Charlie", "English")]

# #solution 1
# unique_courses_set=set()
# for tup in info:
#     unique_courses_set.add(tup[1])
# #print
# print("Unique courses")
# print(unique_courses_set)

# #solution2
# courses=set()
# for name,course in info:
#     courses.add(course)
# print("Unique courses")

# print(courses)

# #QUESTION -----b
# print("\nStudents enrolled in English")
# for name,course in info:
#     if(course=="English"):
#         print(name)

# #QUESTION -----c
# dict={}
# for name,course in info:
#     if dict.get(name)==None:
#         dict.update({name:set()})
#         dict[name].add(course)
#     else:
#         dict[name].add(course)
# print(dict)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# fruits=["apple","banana"]
# print(dir(fruits))
# print(help(fruits))


# s={1,2,3}
# if 2 in s:
#     s.remove(2)
# print(s)

d={
    "name":"ali",
    "age":20
}

# d["name"]=
l = [2,5,6]
del(l)
print(len(l))