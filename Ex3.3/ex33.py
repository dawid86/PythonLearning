score = input("Enter score")
try :
    sc = float(score)
except :
    print("enter a number from 0 to 1")
    quit()

if sc < 0.6 :
    print("F")
elif sc < 0.7 :
    print("D")
elif sc < 0.8 :
    print("C")
elif sc < 0.9 :
    print("B")
elif sc < 1 :
    print("A")
else :
    print("invalid score number, please enter a value between 0 and 1")
