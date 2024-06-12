# relational operator:
#Ex: AND operator
a=10
b=23
x=78
y=8

result=(a>b) # false
result2=(x<y) # false
result3=result and result2
print(result3) # false

result=(a<b) # true
result2=(x>y) # true
result3=result and result2
print(result3) # true

result=(a>b) # false
result2=(x>y) # true
result3=result and result2
print(result3) # false

result=(a<b) # true
result2=(x<y) # false
result3=result and result2
print(result3) # false

#note:
#AND gate:
# if any one is false than answer will be false
# if both true means than output will be true
#
# false true = false
# true false =false
# true true true
# false false =false

#note: true =1, false=0

#============================================================================================================

