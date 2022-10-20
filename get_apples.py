a = input("How many apples do you have?:")

try:
    a = int(a)
except:
    print("\033[41m[Error]\033[0m" + a + " Nan")
else:
    print("You have got " , a, " apples!")
