import random


def randomize(dictionary):
    d = dictionary
    listvar = []
    for i in d:
        listvar.append(i)
    newlist = []
    for i in listvar:
        newlist.append(i)
    supernewlist = []
    for i in listvar:

        a = random.choice(newlist)
        newlist.remove(a)
        supernewlist.append(a)
        if i is True:
            break
    newdict = {}

    tick = 0
    for i in supernewlist:
        newdict[i] = d[supernewlist[tick]]
    return newdict


def sort(dictionary):
    d = dictionary
    dlist = list(d)
    dlist.sort()
    nd = {}
    for i in dlist:
        nd[i] = d[i]
    return nd
