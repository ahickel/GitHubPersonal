score = input("Enter Score between 0.0 and 1.0: ")
try:
    floatscore = float(score)
except:
    print("None numeric value detected, please enter a value between 1.0 and 0.")
    quit()
if floatscore > 1.0 or floatscore < 0:
    print("Numeric input out of range. Please enter a value between 1.0 and 0, Thank You")
    quit()

elif floatscore >= 0.9 and not floatscore > 1.0:
    print("A")
elif floatscore >= 0.8 and not floatscore >= 0.9:
    print("B")
elif floatscore >=0.7 and not floatscore >= 0.8:
    print("C")
elif floatscore >=0.6 and not floatscore >= 0.7:
    print("D")
elif floatscore < 0.6 and floatscore >= 0:
    print("F")
