import math
def split(word):
    return [int(char) for char in word]

input1 = int(input())
input2 = split(str(input()))
def indexEverything(input2):
    whereDict = dict()
    for index in range(len(input2)):
        try:
            whereDict[input2[index]].append(index)
        except:
            whereDict[input2[index]] = [index]
    return whereDict

def doesCodeExist(n, whereDict):
    ##n = int(n)
    ##print(n)
    ## n is a list of the three digits
    try:
        firstLoc = whereDict[int(n[0])][0]
    except:
        ##print("what")
        return False
    ##print(firstLoc)
    found2 = False
    counter2 = 0
    ##print("getting in here")
    while not found2:
        ##print("trying")
        try:
            ##print(whereDict[int(n[1])][counter2], firstLoc)
            ##print(whereDict[int(n[1])][counter2] > firstLoc)
            if (whereDict[int(n[1])][counter2] > firstLoc):
                secondLoc = whereDict[int(n[1])][counter2]
                ##print("beep")
                ##print(secondLoc)
                found2 = True
            ##print("jebtime")
            counter2 += 1

            #print(secondLoc)
        except:
            return False
    ##print(secondLoc)
    found3 = False
    counter3 = 0
    while not found3:
        try:
            if (whereDict[int(n[2])][counter3] > secondLoc):
                ##print(whereDict[int(n[2])][counter3])
                return True
            counter3 += 1
            ##print(counter3)
        except:
            return False

whereDict = indexEverything(input2)
counter = 0
##print("here")
##print(doesCodeExist("242", whereDict))
##print("fin")
for index in range(0, 1000):
    if (index < 100):
        if (index < 10):
            index = "00" + str(index)
        else:
            index = "0" + str(index)
    if (doesCodeExist(split(str(index)), whereDict)):
        ##print(index)
        counter += 1
print(counter)
