# outer and inner functions calling

def outer_fun():
  var1=45
  def inner_fun():
      print(var1)
  inner_fun()

outer_fun()

# output:
# 45
