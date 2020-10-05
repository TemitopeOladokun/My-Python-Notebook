# If- Statement 
is_hot = True

if is_hot:
    print("Drink lot of water")
print("Enjoy your day!\n \n")


is_hot = False

if is_hot:
    print("Drink lot of water")
print("Enjoy your day! \n")


is_hot = True
is_cold = True

if is_hot:
    print("Drink lot of Water")
elif is_cold:
    print("Wear warm clothing")
else:
    print("It is a lovely day.\n")


is_hot = False
is_cold = True

if is_hot:
    print("Drink lot of Water")
elif is_cold:
    print("Wear warm clothing")
else:
    print("It is a lovely day.\n")


is_hot = False
is_cold = False

if is_hot:
    print("Drink lot of Water")
elif is_cold:
    print("Wear warm clothing")
else:
    print("It is a lovely day.\n")


# Classwork

price = 10000000
good_credit = True

if good_credit:
    down_payment = price * 0.1
else:
    down_payment = price * 0.2
print("The down payment is: $%s" %(down_payment))





