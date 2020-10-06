'''
weight = input("Enter your weight ?")
Weight = int(weight)
print("\n")
print("Enter 'l' for pound and 'k' for Kilogram")

unit = input("Enter your unit ?")

if  unit == "l" :
    val = Weight * 0.45
    print("You are {%s} kilograms" % (val))
elif unit == "k":
    val2 = Weight / 0.45
    print("You are {%s} pounds" % (val2))
else:
    print("Try again")


print("\n")
'''
#Another Solution
weight2 = int(input("Weight: "))
unit2 = input("Enter (L) for Pounds or (K) for Kilogram: ")
print(unit2)
if unit2 == "L":
    converter = weight2 * 0.45 
    print("You are {%s} kilograms" % (converter))
elif unit2.upper == "K":
    converter = weight2 / 0.45
    print("You are {%s} pounds" % (converter))
else:
    print("Try again")


