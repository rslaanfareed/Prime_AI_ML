try:
    a=int(input("Enter number:"))
    ans=10/a
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:
    print("Enter integers only")
else:
    print("Ans:",ans)
finally:
    print("End of program")