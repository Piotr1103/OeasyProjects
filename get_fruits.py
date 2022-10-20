import get_apples
import get_bananas

a = get_apples.a
b = get_bananas.b

try:
    a = int(a)
    b = int(b)
except:
    print("Wrong inputs!")
else:
    print("You've got ", a+b, "fruits in all")
