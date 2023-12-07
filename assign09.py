# Write a function in python to display the elements of list thrice if it is a
# number and display the element terminated with ‘#’ if it is not a number.
# Suppose the following input is supplied to the program:
# [‘23’,‘MAN’,‘GIRIRAJ’, ‘24’,‘ZARA’]
# The output should be
# 232323
# MAN#
# GIRIRAJ#
# 242424
# ZARA#

def is_num(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def special_print(ls):
    for el in ls:
        if is_num(el):
            print(f'{el}' * 3)
        else:
            print(f'{el}#')

inp = input('Enter a list of elements separated with space: ')
special_print(inp.split(' '))
