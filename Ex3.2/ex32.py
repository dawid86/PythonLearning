# remember that names of the variables comes first, like hrs or rate

hrs = input("Enter Hours: ")
rate = input("Rate per hour: ")
try:
    h = float(hrs)
except:
    print("Enter a number instead of text")
try:
    r = float(rate)
except:
    print("Enter a number instead of text")
try:
    if h < 40.0 :
        print(h*r)
    else :
        print(40*r+((h-40)*(r*1.5)))
except:
    print("please run program again and provide valid input")
