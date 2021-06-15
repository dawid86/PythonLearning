# remember that names of the variables comes first, like hrs or rate

hrs = input("Enter Hours: ")
rate = input("Rate per hour: ")
h = float(hrs)
r = float(rate)

if h < 40.0 :
    print(h*r)
else :
    print(40*r+((h-40)*(r*1.5)))
