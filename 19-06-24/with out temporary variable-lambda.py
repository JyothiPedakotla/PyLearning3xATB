#with out temporary variable with lambda

my_list=[2,4,8]
output=lambda num:num**2
double_list=list(map(output,my_list))
print(double_list)

#output
#[4,16,64]