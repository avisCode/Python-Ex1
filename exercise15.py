def listOfTouple(list):
    l1 = []
    for item in list:
        if isinstance(item, tuple):
            l1.extend(item)
    return l1


def TouplOfList(list):
    l1 = ()
    for item in list:
        if type(item) == type(list):
            l1 += tuple(item)
    return l1


def listOfString(list):
    l1 = []
    l2 = []
    for item in list:
        if isinstance(item, tuple) or type(item) == type(list):
            l1.extend(item)
    for item in list:
        if type(item) == type('') and item not in l1:
            l2.extend(item)
    return l2


def tupleOfInt(list):
    l1 = []
    l2 = ()
    for item in list:
        if isinstance(item, tuple) or type(item) == type(list):
            l1.extend(item)
    for item in list:
        if isinstance(item, (int, float)) and item not in l1:
            l2 = l2 + (item,)
    return l2


if __name__ == "__main__":
    L = [1, 2, 'a', (11, 2, 'b'), [22, 'c'], (33,), ['d'], 'e']
    print(listOfTouple(L))
    print(TouplOfList(L))
    print(listOfString(L))
    print(tupleOfInt(L))
