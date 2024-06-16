# # Task #2
# #
# # Develop a Python script that calculates the square and cube of a given number. num = 2 sq - 4, c = 8
# # Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.
#
# # ======================================================================================================================
#
# # Develop a Python script that calculates the square and cube of a given number. num = 2 sq - 4, c = 8
# # answer:
square=2
cube=8
print(" print square of number",2**2)
print(" print cube of number",8**3)
#
# #=========================================================================================================
#
# #Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.
# # Answer:
# # Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
#
# # Comparing the numbers
if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num1} is less than {num2}")
else:
    print(f"{num1} is equal to {num2}")