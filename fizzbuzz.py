# Write a program that prints the numbers from 1 to 100
# For multiples of ‘3’ print “Fizz” instead of the number
# For the multiples of ‘5’ print “Buzz”.
# Print "FizzBuzz" if it is divisible by 3 and 5.
check_three = 3
check_five = 5
for num in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]:
    def isMultiplethree(num,check_three):
        return num % check_three == 0
    def isMultiplefive(num,check_five):
        return num % check_five == 0
    if (isMultiplethree(num,check_three)==True) and (isMultiplefive(num,check_five)==False):
        print("Fizz")
    if (isMultiplefive(num,check_five)==True) and (isMultiplethree(num,check_three)==False):
        print("Buzz")
    if (isMultiplethree(num,check_three)==True) and (isMultiplefive(num,check_five)==True):
        print("FizzBuzz")
    if (isMultiplethree(num,check_three)==False) and (isMultiplefive(num,check_five)== False):
        print(num)
