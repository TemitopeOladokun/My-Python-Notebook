'''

for x in range(5):
    for y in range(2):
        print(x, y)

# Exercise
# 1. Print Letter - F
numbers = [5, 2, 5, 2, 2]
for x in numbers:
    print("x" * x)

#Solution 2

numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ""
    for count in range(x_count):
        output += 'x'
    print(output)
'''

numbers = [2, 2, 2, 2, 5]
for x_count in numbers:
    output = ""
    for count in range(x_count):
        output += 'x'
    print(output)