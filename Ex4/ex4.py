def computepay(h, r):
    if h > 40 :
        x = ((h-40)*(1.5*r))+40*r
    else :
        x = h*r
    return x

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float (rate)
p = computepay(h, r)
print("Pay", p)
