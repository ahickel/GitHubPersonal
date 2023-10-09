for num in range(100):
    num = num + 1
    def isMultiplethree(num):
        return num % 3 == 0
    def isMultiplefive(num):
        return num % 5 == 0
    if isMultiplethree(num) and isMultiplefive(num):
        print("FizzBuzz")
    elif isMultiplethree(num):
        print("Fizz")
    elif isMultiplefive(num):
        print("Buzz")
    else:
        print(num)
