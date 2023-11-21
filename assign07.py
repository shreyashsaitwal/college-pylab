string = input('Enter a string: ')

def sol1():
    dict = {}
    for word in string.split(' '):
        dict[len(word)] = dict.get(len(word), 0) + 1
    return dict

def sol2():
    dict = {}
    count = 0
    for char in string:
        if char == ' ':
            dict[count] = dict.get(count, 0) + 1
            count = 0
        else:
            count += 1
    return dict

print(sol1())
print(sol2())
