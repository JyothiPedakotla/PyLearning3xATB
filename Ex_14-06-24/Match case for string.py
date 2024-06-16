#match case with string


number=(input("enter the name\n"))
match number:
    case "chrome":
        print("you have entered chrome")
    case "edge":
         print("you have entered edge")
    case "fire fox":
         print("you have entered fire fox")
    case _:
         print("no idea")

# output:
#
# enter the name
# chrome
# you have entered chrome

