b = input("How many bananas do you have?:")

try:
    b = int(b)
except:
    print("\033[41m[Error]\033[0m" + b + " Nan")
else:
    print("You have got " , b, " bananas!")
