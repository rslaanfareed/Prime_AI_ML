import json


# #json.loads() and json.dumps() --- dealing with strings


# #json.loads()

# #json string
# json_str= '{"name":"Arslan","isStudent":true,"phone":null}'
# print(json_str)
# print(type(json_str))  #str

# #convert to python object
# py_obj=json.loads(json_str)
# print(py_obj)
# print(type(py_obj))  #python dictionary



# #json.dumps()
# py_obj={
#     "name":"ali",
#     "age":19,
#     "phone":None
# }
# #convert python object to json string
# json_str=json.dumps(py_obj)

# print(json_str)
# print(type(json_str))  #str



#json.load() and json.dump() --- dealing with files

#json.load() --- read

# with open("data.json","r") as f:
#     py_obj=json.load(f)
#     print(py_obj)
#     print(type(py_obj))  #dict

#json.dump()

# data={
#     "name":"Arslan",
#     "age":20,
#     "phone":None
# }

# with open("data.json","w") as f:
#     json.dump(data,f,indent=4,sort_keys=True)






# data={
#     "Name":"ABC",
#     "age":25,
#     "city":"XYZ"
# }

# with open("person.json","w+") as f:
#     json.dump(data,f,indent=4,sort_keys=True)

# with open("person.json","r") as f:
#     data=json.load(f)
#     print(data)





# #addin a new key value pair
# try:
#     cgpa=int(input("Enter cgpa (0-4):"))
#     if (cgpa<0 or cgpa>4):
#         raise ValueError
# except ValueError:
#     print("Enter valid value")
# else:
#     data.update({
#         "cgpa":cgpa
#     })
#     with open("person.json","w") as f:
#         json.dump(data,f,indent=4)
    
#     with open("person.json","r") as f:
#         person_data=json.load(f)
#     print(person_data)





#creating list in json file and reading it
d=[
    {
        "name":"Ali",
        "marks":80
    },
    {
        "name":"Ahmed",
        "marks":91
    }
]

# with open("data.json","w") as f:
#     json.dump(d,f)

# with open("data.json","r") as f:
#     std_data=json.load(f)
# for val in std_data:
#     print(f"Name:{val.get("name")}")
#     print(f"Marks:{val.get("marks")}")
#     print()

#adding new key value pair to the list
try:
    name=input("Enter name: ")
    marks=int(input("Enter marks:"))
    d.append({"name":name,"marks":marks})

    with open("data.json","w") as f:
        json.dump(d,f,indent=4)
except ValueError:
    print("Enter valid values")

else:
    with open("data.json","r") as f:
        std_data=json.load(f)
        print(std_data)
    


#search a student in json file

search="Arslan"
with open("data.json","r") as f:
    std_data=json.load(f)
    for val in std_data:
        if val.get("name")==search:
            print("Student found")
            
            print(val.get("name"),val.get("marks"))
        
