#  #general way to create a list
# squares=[]
# for i in range(10):
#     squares.append(i*i)
# print(squares)

# #using list comprehension
# #squares
# sq=[i*i for i in range(10) ]
# print(sq)

# #squares of even numbers
# even=[i*i for i in range(20) if i%2==0 ]
# print(even)


# #replacing neg numbers with 0
# numbers=[-2,0,9,-4,5,-6,0,6,-9]
# print( numbers)

# numbers=[0 if val<0 else val for val in numbers]
# print(numbers)


# words=["hello","python"]
# print(words)
# words=[val.upper() for val in words]
# print(words)