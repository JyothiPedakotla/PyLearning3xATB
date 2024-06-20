# function scope-local variable

def my_function():
    a=10
    print(a)
    print("Hello")

# print(a) # it will throw an error like we need to print the insid ethe function only not out of the function

my_function()

# output
# 10
# Hello
