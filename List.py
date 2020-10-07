'''
# Exercise - checking for the largest number
number = [10, 100, 20, 50, 30]
Max_number = number[0]
for item in number:
    if item > Max_number:
        Max_number = item
print(Max_number)

'''

names = ["Ali", "Hippopotamus", "Adeola", "Shola", "Muhammed", "Susan" ]
max2 = -1
for item in names:
    if len(item) > max2:
        max2 = len(item)
        result = item
print(result)