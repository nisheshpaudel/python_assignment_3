def Linear_Search(mylist, item):
    x = 0
    result = False

    while x < len(mylist) and not result:
        if mylist[x] == item:
            result = True
        else:
            x = x + 1

    return result, x

print(Linear_Search([22, 16, 43, 27, 31, 41, 17, 21, 56], 31))