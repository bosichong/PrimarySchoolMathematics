import random
def getNum(list, step):
    newList = []
    for i in range(0, step):
        newList.append(random.randint(list[i][0], list[i][1]))
    return newList
