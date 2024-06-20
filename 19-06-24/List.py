#List nothing but a collection of items

#num=[1,2,4,78]

number=[10,11,23,34]

def list_ex():
    number.append(50)
    number[0]=100
    return number

p=list_ex()
print(p)

#output
# [10, 11, 23, 34, 50]
#[100, 11, 23, 34, 50]

