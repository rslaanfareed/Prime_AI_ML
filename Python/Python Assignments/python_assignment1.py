# Python Fundamentals Assignment 1

# Q1. Name and Age -------------------------


# Take name and age from the user
name = input("Enter your name: ")
age = input("Enter your age: ")

# Display the result
print("Hello", name + ",", "you are", age, "years old!")



# Q2. Basic Arithmetic ----------------------


# Take two numbers
num1 = float(input("\nEnter first number: "))
num2 = float(input("Enter second number: "))

# Perform calculations
print("Sum =", num1 + num2)
print("Difference =", num1 - num2)
print("Product =", num1 * num2)
print("Quotient =", num1 / num2)


# Q3. Average of Numbers ----------------------


# Take input
a = int(input("\nEnter first integer: "))
b = int(input("Enter second integer: "))
c = float(input("Enter a float number: "))

# Convert integers to float
a = float(a)
b = float(b)

# Find average
average = (a + b + c) / 3

# Print average
print("Average =", average)



# Q4. Type Conversion ---------------------------


# Take number as string
value = input("\nEnter a number: ")

# Convert into different types
int_value = int(value)
float_value = float(value)
string_value = str(value)

# Print values and their types
print(int_value, type(int_value))
print(float_value, type(float_value))
print(string_value, type(string_value))



# Q5. Operator Precedence --------------------------


# Evaluate the expression
x = 10 + 3 * 2 ** 2

# Print result
print("\nResult =", x)

# Explanation:
# 2 ** 2 = 4
# 3 * 4 = 12
# 10 + 12 = 22



# Q6. Swap Two Numbers --------------------------


# Take input
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))

# Swap using a temporary variable
temp = a
a = b
b = temp

# Display swapped values
print("After Swapping:")
print("First number =", a)
print("Second number =", b)



# Q7. Celsius to Fahrenheit --------------------------


# Take temperature as string
celsius = input("\nEnter temperature in Celsius: ")

# Convert to float
celsius = float(celsius)

# Convert to Fahrenheit
fahrenheit = (celsius * 9 / 5) + 32

# Print result
print("Temperature in Fahrenheit =", fahrenheit)



# Q8. Area of Circle ---------------------------


# Take radius
r = float(input("\nEnter radius: "))

# Calculate area
area = 3.14 * r * r

# Display area
print("Area =", area)



# Q9. Simple Interest ---------------------


# Take input
P = float(input("\nEnter Principal: "))
R = float(input("Enter Rate: "))
T = float(input("Enter Time: "))

# Calculate Simple Interest
SI = (P * R * T) / 100

# Print result
print("Simple Interest =", SI)



# Q10. Integer and Fractional Part --------------------


# Take decimal number
number = float(input("\nEnter a decimal number: "))

# Find integer part
integer_part = int(number)

# Find fractional part
fractional_part = number - integer_part

# Print results
print("Integer part =", integer_part)
print("Fractional part =", fractional_part)