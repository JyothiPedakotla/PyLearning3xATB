#match case menas swich case in jva but in python its a match case

# match case is used for multiple conditions

#ex-match case

number=int(input("enter the number\n"))
match number:
    case 1:
        print("you have entered 1")
    case 2:
         print("you have entered 2")
    case 3:
         print("you have entered 3")
    case _:
         print("no idea")

#output:
# enter the number
# 3
# you have entered 3