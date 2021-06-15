largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    try:
        n = int(num)
    except:
        if num == "done":
            break
        else:
            print("Invalid input")
            continue
    #largest
    #largest = n
    #smallest
    #smallest = n

    #print(type(n))
      
    if largest is None:
        largest = n
    elif n > largest:
            largest = n
    if smallest is None:
        smallest = n
    elif n < smallest:
        smallest = n
            

print("Maximum is", largest)
print("Minimum is", smallest)
