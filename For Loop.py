'''

for item in ("Python"):
    print(item)

for item2 in ["Temi", "Samuel", "Ivoline"]:
    print(item2)

for item3 in [1, 2, 3, 4, 5]:
    print(item3)

for item4 in range(5, 30):
    print(item4)

for item4 in range(5, 30, 5):
    print(item4)
'''

#Exercise
# Calculate the total amount of the shopping cart.
prices = [10, 20, 30, 40, 50]
Total = 0
for total in prices:
    Total += total
    print("The total cost is %s" % (Total))
print("The final cost is %s" % (Total))