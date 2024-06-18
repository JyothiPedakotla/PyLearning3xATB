# functions with *args

#*args means list

def demo(*args):
    for  i in args:
      print(i,end=" - ")

demo("jyothi","hema","megha")

# outpou:
# yothi - hema - megha -