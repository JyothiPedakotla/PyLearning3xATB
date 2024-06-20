#without temporary variable


my_list=[10,20,30]

def demo(num):
    return num*2

double_list=list(map(demo,my_list))
print(double_list)

#output
# [20,40,60]

#map() map is function 1. it will take each item from list
                    #2.execute the function on it
                    #3.return same number of elements into list

