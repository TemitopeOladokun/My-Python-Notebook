'''
numbers = [5, 1, 2, 7, 9]
numbers.insert(0, 15)
print(numbers)


numbers = [5, 1, 2, 7, 9, 5, 3]
numbers.remove(5)
print(numbers)

# Clear the content of a List.
numbers = [5, 1, 2, 7, 9]
numbers.clear()
print(numbers)


#To identify the index of a List
numbers = [5, 1, 2, 7, 9]
print(numbers.index(5))


#To print the index of number that is not in the List
numbers = [5, 1, 2, 7, 9]
print(numbers.index(50))


#To count the number of occurences
numbers = [5, 1, 2, 7, 9, 0, 1, 9, 9]
print(numbers.count(9))


# To sort the list in ascedning order
numbers = [5, 1, 2, 7, 9]
numbers.sort()
print(numbers)


# To sort the list in descending order
numbers = [5, 1, 2, 7, 9]
numbers.sort()
numbers.reverse()
print(numbers)

'''
# To make a copy of List
numbers = [5, 1, 2, 7, 9]
numbers2 = numbers.copy()
numbers.append(15)
print(numbers2)
print(numbers)

