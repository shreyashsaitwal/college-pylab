# Write a python program to read string from user and create a dictionary having
# key as word length and value is count of words of that length.
# 1. For example, if user enters ‘I scream you scream we all scream for ice cream’
# 2. Word Word length
# 1. I 1
# 2. scream 6
# 3. you 3
# 4. scream 6
# 5. we 2
# 6. all 3
# 7. scream 6
# 8. for 3
# 9. ice 3
# 10. cream 5
# 11. The content of dictionary should be {1:1, 6:3, 3:4, 2:1, 5:1}

inp = input('Enter a string: ')

def normal_way():
    dict = {}
    for word in inp.split(' '):
        dict[len(word)] = dict.get(len(word), 0) + 1
    return dict

def hard_way():
    dict = {}
    count = 0
    for i in range(len(inp)):
        if i >= len(inp) - 1:
            count += 1
            dict[count] = dict.get(count, 0) + 1
            break
        elif inp[i] == ' ':
            dict[count] = dict.get(count, 0) + 1
            count = 0
        else:
            count += 1
    return dict

print(normal_way())
print(hard_way())
