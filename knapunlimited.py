#tl

#nbddknpsckprblm

#   outlining
#       given a Set of N items with weight W(N), value V(N) and unlimited of each item, maximize the value within W(L)
#       where W(L) is the weight limit.

#   Key Things:
#       Remove items where W(N) > W(L)
#       Remove items where W(N) >= W(Others) where V(Others) > V(N)
#       ...


import sys
import random

def createrandomlist(minWt, capWt, capVal, totalItems):
    #using random integer generation, create a list of tupled values
    #that will have a weight between minWt, capWt
    #               a value between 1 and capVal
    #               and totalItems amount of items
    randomlist = {}
    for i in range(0,totalItems):
        wt = random.randint(minWt,capWt)
        val = random.randint(1,capVal)
        randomlist[i] = (wt, val)
    return randomlist

def createdict(newdict):
    realdict = {}
    itemnum = 1
    for item in newdict.values():
        realdict[itemnum] = item
        itemnum += 1
    return realdict

def printlist2(randomlist, numrows):
    print("Format is: [Item] : (Weight, Value)")
    x = len(randomlist)
    y = 0
    flag = False
    for i in randomlist:
        if(i == numrows):
            break
        while(i <= x):
            if(i not in randomlist):
                break
            print("[" + str(i) +  "]", randomlist[i], end='\t')
            i += numrows
            y += 1
        print()
        y = 0
        i -= y*numrows
        

def firstfilterlist(randomlist):
    #first filter
    #Objective: for each weight, keep only the highest value item
    print("Amount before:", len(randomlist))
    sortedlist = sorted(
    randomlist.values(),
    key=lambda t: (t[0], t[1])
    )

    newdict = {}
    for item in sortedlist:
        x = item[0]
        if(x not in newdict):
            newdict[x] = item
        elif item[1] > newdict[x][1]:
            newdict[x] = item
    print("Amount after:", len(newdict))
    realdict = {}
    itemnum = 1
    return createdict(newdict)

def secondfilterlist(randomlist):
    #second filter
    #Objective: with the highest value of each weight now...
    #           place each item in a dictionary by its value
    #           however, if there exists an item with a lower weight at
    #           the given value, we can replace the current one.
    #           (this can be done safely due to the "first filter"
    print("Amount before:", len(randomlist))
    sortedlist = sorted(
    randomlist.values(),
    key=lambda t: (t[0], t[1])
    )
    newdict = {}
    for item in sortedlist:
        x = item[1]
        if(x not in newdict):
            newdict[x] = item
        elif x < newdict[x][0]:
            newdict[x] = item
    print("Amount after:", len(newdict))
    return createdict(newdict)

def thirdfilterlist(randomlist):
    #third filter
    #Objective: taking the sequentially highest value item
    #                   (the order is first by value then by weight)
    #               we compare it to every other item and...
    #               IF 1 CONDITION IS MET:
    #                   If the Highest Value Item has a LOWER weight
    #                   we remove the compared item.
    #               This can be done because the order of the items
    #                   is already by first Value, second Weight
    #                   to guarantee no other higher Value items can exist
    #                   and be accidentally removed.
    #                   furthermore, even if items shared same Value,
    #                   with different weights, they would have been ordered.
    print("Amount before:", len(randomlist))
    sortedlist = sorted(randomlist.values(),
    key=lambda t: (t[1], t[0]), reverse=True
    )
    counter = -1
    #print("B4")
    #print(sortedlist)
    #print("SPACE\n")
    for filteritem in sortedlist:
        counter = sortedlist.index(filteritem)
        for checkthis in sortedlist[counter:]:
            if checkthis[0] > filteritem[0]:
                sortedlist.remove(checkthis)
                #print("removing", checkthis, "compared to", filteritem)

    newdict = {}
    for item in sortedlist:
        x = item[0]
        newdict[x] = item
    print("Amount after:", len(newdict))
    return createdict(newdict)

def fourthfilterlist(randomlist):
    #fourth filter
    #Objective: for all items, beginning with the lowest weight item
    #           compare to all other items.
    #           Conditions to be met:
    #               1) Can this item be placed more often (2x, 3x, 4x, ...)
    #                   1a) If so, does it have a higher given value?
    #               2) Repeat for all items.
    print("Amount before:", len(randomlist))
    sortedlist = sorted(randomlist.values(),
    key=lambda t: (t[0], t[1])
    )
    counter = -1
    #print("B4")
    #print(sortedlist)
    #print("SPACE\n")
    for filteritem in sortedlist:
        counter = sortedlist.index(filteritem)
        for checkthis in sortedlist[counter:]:
            multiple =  checkthis[0] // filteritem[0]
            #print(checkthis[0], "//", filteritem[0])
            #print(multiple)
            if multiple >= 2:
                if filteritem[1] * multiple > checkthis[1]:
                    sortedlist.remove(checkthis)
                    #print("removing", checkthis, "compared to", filteritem)
    #print(sortedlist)
    newdict = {}
    for item in sortedlist:
        x = item[0]
        newdict[x] = item
    print("Amount after:", len(newdict))
    return createdict(newdict)

def main(argv):
    numrows = 25
    minwt = 77
    maxwt = 2888
    maxval = 777
    numitems = 100000
    randomlist = createrandomlist(minwt, maxwt, maxval, numitems)

    #printlist2(randomlist)
    print("Filter One")
    newdict = firstfilterlist(randomlist)

    #print(sortedlist)
    #print("spacer")
    #printlist2(newdict, numrows)
    print("Filter Two")    
    newdict = secondfilterlist(newdict)
    #printlist2(newdict, numrows)
    print("Filter Three")
    newdict = thirdfilterlist(newdict)
    printlist2(newdict, numrows)
    print("Filter Four")
    newdict = fourthfilterlist(newdict)
    printlist2(newdict, numrows)
    return

if __name__ == "__main__":
    main(sys.argv)

