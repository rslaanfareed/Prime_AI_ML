# #Question 1
'''
with open("names.txt","w+") as f:
    for i in range(5):
        name=input(f"Enter name {i+1}:")
        f.write(f"{name}\n")

data=True
with open("names.txt","r") as f:
    while data:
        data=f.readline()
        print(data)
        '''


# #Question 2
'''
with open("log.txt","a") as f:
    f.write("Program run successfully")

data=True
with open("log.txt","r") as f:
    while data:
        data=f.readline()
        print(data)
'''


#Question 3
'''
numbers=[5,10,15,20,25]
numbers=[num for num in numbers if num>15]
print(numbers)
'''


'''
# #Question 4: JSON
import json

cities={
    "islamabad":1000000,
    "lahore":14000000,
    "Karachi":20000000
}

with open("cities.json","w") as f:
    json.dump(cities,f)

with open("cities.json","r") as f:
    data=json.load(f)
    print(data)

with open("cities.json","w") as f:
    city=input("Enter city:")
    pop=int(input("Enter population:"))
    cities.update({city:pop})
    json.dump(cities,f)
    
with open("cities.json","r") as f:
    data=json.load(f)
    print(data)
'''


'''
Question 5: exception handling
try:
    with open("data.txt","r") as f:
        data=json.load(f)
        
except FileNotFoundError:
    print("File does not exist")
else:
    print(data)
finally:
    print("Program ended")
'''


