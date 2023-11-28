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
