# write a code for to take the inputs from user and display the grades accordingly

#Ex:
#score >=90 and  score<=100 => A
#score >=80 and  score<=90 => B
#score >=70 and  score<=80 => C
#score >=60 and  score<=70 => D
#score >=0 and  score<=34 => F

#programe:
score=int(input("Enter the score\n"))

if score >=90 and score<=100:
    print("A grade")

elif score >=80 and score<=90:
    print("B grade")

elif score >=70 and score<=80:
    print("C grade")

elif score >=60 and score<=70:
    print("D grade")

elif score >=0 and score<=34:
    print("F grade")

else :
    print("invalied score")