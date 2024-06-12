# OR operator
a=10
b=23
x=78
y=8

result=(a>b) # false
result2=(x<y) # false
result3=result or result2
print(result3) # false

result=(a<b) # true
result2=(x>y) # true
result3=result or result2
print(result3) # true

result=(a>b) # false
result2=(x>y) # true
result3=result or result2
print(result3) # true

result=(a<b) # true
result2=(x<y) # false
result3=result or result2
print(result3) # true

#note
# OR gate
# false true= true
# true false=true
# true true=true
# false false= false

#AND gate oppsite is oR gate
#in AND gate if it is any of the number is false than it wil be false
#in OR gate if it is any of the number is ture than it wil be ture
