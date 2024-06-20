# even and odd numbers by using lambda function

def find_even_odd(num):

    if num%2==0:
        print("even number")
    else:
        print("odd number")

#calling function
find_even_odd(4)

#output
#even number

#========================================
#same above code by using lambda expression
output=lambda num:"even" if num%2==0 else "odd"
print(output(5))

# output:
# odd

