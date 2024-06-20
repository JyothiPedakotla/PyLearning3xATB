# important question
# lamda expression it is used to do the task in one line

def double_MySalary(salary):
    return salary*2

result=double_MySalary(100)
print(result)

# output
# 200

#============================================================================================

#by using lambda function we can reduse the above code into single line
result=lambda salary: salary*2
print(result(100))

#output
200




