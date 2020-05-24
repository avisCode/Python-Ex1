def FindTypes(list):
    temp = {}
    for item in list:
        s = str(type(item))[8:-2]
        if s in temp:
            temp[s] += 1
        else:
            temp[s] = 1
    return temp


if __name__ == "__main__":
    print(FindTypes([1, 2, 'a', (11, 2, 'b'), [22, 'c'], (33,), ['d'], 'e']))
