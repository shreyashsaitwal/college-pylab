# Write a Python program to sort a tuple by its float element.
# Sample data: [('item1', '13.10'), ('item2', '17.10'), ('item3', '25.3')]
# Expected Output: [('item3', '25.3'), ('item2', '17.10'), ('item1', '13.10')] 

inp = input("Enter data separated by space (format- key:value): ").split(" ")
data = list(map(lambda x: tuple(x.split(":")), inp))

def normal_way():
    return sorted(data, key=lambda x: float(x[1]), reverse=True)

def hard_way():
    global data
    _data = data
    for i in range(len(_data)):
        for j in range(len(_data)-i-1):
            if (float(_data[j][1]) < float(_data[j+1][1])):
                _data[j], _data[j+1] = _data[j+1], _data[j]
    return _data

print("Normal way: ", normal_way())
print("Hard way: ", hard_way())

