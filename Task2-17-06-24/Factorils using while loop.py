# factorial using while loop

fact=1
number=int(input("Enter the number \n"))

while(number>0):
    fact=fact*number
    number=number-1
print("factorial of num",fact)


# output
# Enter the number
# 3
# factorial of num 6