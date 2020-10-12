numbers = [1, 2, 2, 2, 4, 3, 5, 6, 4, 6, 8, 9, 7, 9, 2, 2]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
        uniques.sort()
        
print(uniques)    



