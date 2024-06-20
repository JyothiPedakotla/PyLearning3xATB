#outside the function-global variable

#declaring and initialation  variable in out of the function

global_var=35

def f1():
    print(global_var)
    print("hi")

f1()

# output:
# 35
# hi
