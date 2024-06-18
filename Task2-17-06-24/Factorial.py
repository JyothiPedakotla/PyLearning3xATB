#
# ✅ Task - Fibonacci series and Factorial
#
# # 3. Factorial
# # n = 5
# # 5! -->5*4*3*2*1 -> 120
# # 3! -> 3*2*1 -> 6
# # 4! -> 4*3*2*1 -> 24

# Answer
# Factorials of any number means if i give number 3 and factorial of number 3 is 3*2*1=6


Factorial=1
number=int(input("Enter the number \n"))

for i in range(1,number+1):
    Factorial=Factorial*i
print("factorial of number is",Factorial)


#output
# Enter the number
# 3
# factorial of number is 6
