largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num_float = float(num)
    except:
        print('Invalid input')
        continue
    if largest is None:
        largest = num_float
    elif num_float > largest:
        largest = num_float
    if smallest is None:
        smallest = num_float
    elif num_float < smallest:
        smallest = num_float

print("Maximum is", int(largest))
print("Minimum is", int(smallest))
