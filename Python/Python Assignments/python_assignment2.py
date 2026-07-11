# #Q1 tax on salary
# def tax_on_salary(salary):
#     if salary<30000:
#         final_tax=salary*0.05
#         print(f"tax rate: 5%\nfinal tax: {final_tax}\nsalary after tax: {salary-final_tax}")

#     elif salary<=70000 and salary>=30000:
#         final_tax=salary*0.15
#         print(f"tax rate: 15%\nfinal tax: {final_tax}\nsalary after tax: {salary-final_tax}")

#     elif salary>70000:
#         final_tax=salary*0.25
#         print(f"tax rate: 25%\nfinal tax: {final_tax}\nsalary after tax: {salary-final_tax}")

# tax_on_salary(10000)



# # #Q2 print all even bewtween two numbers
# def even_numbers(a,b):

#     for i in range(a,b+1):
#         if i%2!=0:
#             continue
#         print(i)

# even_numbers(0,13)




# #Q3. print digits of a number
# def print_digits(n):

    #USING LOOP TO REVERSE

    # reverse=0
    # #reverse the number
    # while n>0:
    #     digit=n%10
    #     reverse=reverse*10+digit
    #     n=n//10

    
    #OR USE STRING REVERSE
#     reverse = str(num)[::-1]
#     reverse=int(reverse)


#     #print digits in correct order
#     while reverse > 0:
#         digit=reverse%10
#         print(digit)
#         reverse=reverse//10

# num=int(input("enter a number:"))
# print_digits(num)



# #Q4. count digits
# def count_digits(n):
#     count=0
#     while n>0:
#         count=count+1
#         n=n//10
#     return count
# num=int(input("Enter a number: "))
# print(count_digits(num))



# #Q5. sum of digits
# def sum_digits(n):
#     sum=0
#     while n>0:
#         sum=sum+(n%10)
#         n=n//10
#     print(sum)

# num=int(input("Ente a number:"))
# sum_digits(num)



# #Q6. divisibles of 3 and 5
# for i in range(1,101):
#     if i%3==0 and i%5==0:
#         print(i)



# #Q7. 
# while(True):
        
#                 num=(input("Enter a number:"))
#                 if num=='quit':
#                     print("Program exited")
#                     break
            
#                 num=int(num)
#                 if num==0:
#                     print("Zero")
#                 elif num<0:
#                     print("negative")
#                 else:
#                     print("positive")
        


# #Q8. calculator
# def calculator(a,b,op):
#     if op=='+':
#         return a+b
#     elif op=='-':
#         return a-b
#     elif op=='*':
#         return a*b
#     elif op=='/':
#         return a/b
#     else:
#         print("INVALID")

# try:
#     a=int(input("Enter a number:"))
#     b=int(input("Enter another number:"))
#     operation=input("Enter operation:")
#     print(calculator(a,b,operation))
# except:
#     print("Error")



# #Q9. check prime
# def check_prime(n):
#     if n<2:
#         print("Not prime")
#         return
#     for i in range(2,n//2+1):
#         if n%i==0:
#             print("not prime")
#             return
#     print("Prime")
# while True:
#     num=int(input("Enter a number: "))
#     check_prime(num)



#Q10. number guess
secret_num=10
while(True):
    user_input=int(input("Guess the number: "))
    if user_input<secret_num:
        print("Too low")
    elif user_input>secret_num:
        print("Too high")
    else:
        print("Correct")
        break

