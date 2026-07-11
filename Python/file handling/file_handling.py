# #File object f ____ opening file in read mode
# f = open("data.txt","r")   

# #read line
# line1=f.readline()
# print(line1)

# #reading file and storing the content in data
# data=f.read()

# print(data)
# print(type(data))

# #close the file
# f.close()


# #open file in write mode
# f=open("data.txt","w")
# #overwrite data
# f.write("this content will overwrite the whole file")

# #close the file
# f.close()

# #open file in append mode
# f=open("data.txt","a")
# f.write("\nThis is new text which will be appended")

# #x mode -- create and open file
# f=open("sample.txt","x")
# f.write("this is sample text for file mode x")


# #r+ mode --- add the text at the start overwriting the text which already existed on that place.
# f=open("sample.txt","r+")
## will print after 1234567 bcz pointer is after 1234567 
# f.write("1234567")
# print(f.read())


# #a+ mode --- append the text at the end
# f=open("sample.txt","a+")
# f.write("appended text")
# #will print nothing bcz pointer is at the end of the file
# print(f.read())


# #w+ mode overwrite the file and pointer goes at the end of the file... nothing prints
# f=open("sample.txt","w+")
# f.write("new text")
# print(f.read())



# #With keyword --- opens the file and after operations, closes the file
# with open("sample.txt", "r") as f:
#     print(f.read())


# #Removing/deleting the files
# #import os and use os.remove

# import os
# os.remove("data.txt")



# #Activity --- find a word in file and also print its line no
# word="python"
# data=True
# line=1
# with open("sample.txt","r") as f:
#     while data:
#         data=f.readline()
#         if word in data:
#             print(f"{word} found in line {line}")
#             break
        
#         print(data)
#         line+=1

with open("sample.txt","r+") as f:
    print(f.read())
    f.write("this is added text after reading")

