# Write a python program for operations on set

colors = {'red', 'blue', 'orange', 'peach'}
fruits = {'apple', 'banana', 'orange', 'peach'}

print('Union: ' + str(colors.union(fruits)))

print('Intersection: ' + str(colors.intersection(fruits)))

print('Difference: ' + str(colors.difference(fruits)))

print('Symmetric difference: ' + str(colors.symmetric_difference(fruits)))

colors.add('purple')
fruits.add('grape')

print('Colors after addition: ' + str(colors))
print('Fruits after addition: ' + str(fruits))

colors.remove('red')
fruits.remove('apple')

print('Colors after removal: ' + str(colors))
print('Fruits after removal: ' + str(fruits))
