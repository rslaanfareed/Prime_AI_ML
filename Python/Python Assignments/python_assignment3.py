#Q1. Palindrome
def palindrome(s):
    rev=s[::-1]
    if rev==s:
        print("Palindrome")
    else:
        print("Not palindrome")

while(True):
    s=input("Enter a string:")
    if s=="quit":
        break
    palindrome(s)


#Q2. avg of all nums of a list
list=[1,3,5,7,3]
sum=0
for val in list:
    sum+=val
avg=sum/len(list)
print(f"Average of all is: {avg}")


#Q3. 

user_input=input("Enter list 1 items with spaces:")
list1=user_input.split()
print(list1)

user_input=input("Enter list 2 items with spaces:")
list2=user_input.split()
print(list2)

list3=list1+list2
print(list3)
list3.sort()
print(list3)




#Q4. 
tup=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

even=[]
odd=[]

for val in tup:
    if val%2==0:
        even.append(val)
    else:
        odd.append(val)

even_tuple=tuple(even)
odd_tuple=tuple(odd)

print(f"Even Numbers: {even_tuple}")
print(f"Odd Numbers: {odd_tuple}")




#Q5.
d={
    "ali":78,
    "ahmad":45,
    "nouman":87
}
while(True):
    print("\na. Add student")
    print("b. Update marks")
    print("c. search for a student")
    print("d. display all students and marks")
    user_input=input("\nEnter your choice\n")

    match user_input:
        case 'a':
            name=input("Enter name of the student:").casefold()
            try:
                marks=int(input("Enter marks:"))
            except:
                print("Enter integers only")
                continue
            if name in d:

                d.update({
                    name:marks
                })
                print("Student already added. Marks Updated")
            else:
                d.update({
                    name:marks
                })
                print(f"Student Added. Name: {name} Marks: {marks} ")
        case 'b':
            name=input("Enter name to update marks:").casefold()
            if name in d:
                try:
                    marks=int(input("Enter marks to update:"))
                    
                except:
                    print("Enter integers only")
                    continue
                d.update({
                    name:marks
                })
                
            else:
                print("Name not in the dictionary. Add student from the main menu")

        case 'c':
            name=input("Enter student name to search:").casefold()
            if name in d:
                print("student found.")
                print(f"Name: {name}, Marks: {d.get(name)}")
            else:
                print("Student not found")
        case 'd':
            for key,value in d.items():
                print(f"Name :{key}   Marks:{value}")

        case _:
            print("Invalid choice")


#Q6.
words = ["apple", "banana", "kiwi", "cherry", "mango"]
dct={}
for val in words:
    dct.update({
        val:len(val)
    })

print(dct)



#Q7. 
s=input("Enter a string:")
count=s.count(" ")
print(f"Total spaces are {count}")



#Q8.
set1=set(input("Enter list 1 elements with spaces:").split())
set2=set(input("Entre list 2 elements with spaces:").split())
print(list(set1))
print(list(set2))
if len(set1.intersection(set2))>0:
    print("lists contain common elements")
    print(list(set1.intersection(set2)))
else:
    print("NO common elements")



#Q9.
list1=input("Enter list elements using spaces: ").split()
print(f"You entered {list1}")
seen=set()
duplicate=set()
for item in list1:
    if item in seen:
        duplicate.add(item)
    else:
        seen.add(item)
print("Duplicate items: ",duplicate)



#Q10.
s=input("Enter a string:")
seen=set()
unique=set()
for ch in s:
    if ch in unique:
        seen.add(ch)
        unique.remove(ch)
    else:
        unique.add(ch)
print(unique)
