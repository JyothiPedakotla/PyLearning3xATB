# how to find max number in between twu numbers

# taking the inputs from the users
a=int(input("Enter the num1 "))
b=int(input("Enter the num2 "))

if a>b:
    print("number is max number")
else:
    print("number is min number")

#=============By using max function also we can findout the max number in given two numbers======
#Ex:
# taking the inputs from the users
a=int(input("Enter the num1 "))
b=int(input("Enter the num2 "))
result=max(a,b)
print("max number in given two numbers is: ", result)