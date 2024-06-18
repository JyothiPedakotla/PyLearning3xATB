# Fibonaci series
# ✅ #4. Fibonaci series
# # 0,0+1, 0+1+1,
# # n = 7
# # 0, 1, 2, 3, 5, 8, 13

# Start with 0 and 1.
# The next number is found by adding 0 + 1, which gives us 1.
# Then, to get the next number, add the last two numbers: 1 + 1 = 2.
# Continue this pattern: 1 + 2 = 3, 2 + 3 = 5, and so on.

# 0,1
# 0+1=1
# 1+1=2
# 1+2=3
# 2+3=5
# 3+5=8
#5+8=13

Fibonaci=int(input("Enter the range of Fibonaaci Series \n"))

a=0
b=1

for i in range(Fibonaci):
    print(a, end=" ")
    c=a+b
    a=b
    b=c
