from math import  *

input = int(input())

def getMoney(money):
    prices = [100, 101, 102, 103, 104, 105]
    rem = []
    for element in prices:
        rem.append(money - money * floor(money/element))
    bounds = [floor(money/element) + 1 for element in prices]
    for index1 in range(bounds[0]):
        for index2 in range(bounds[1]):
            for index3 in range(bounds[2]):
                for index4 in range(bounds[3]):
                    for index5 in range(bounds[4]):
                        for index6 in range(bounds[5]):
                            if (index1 * prices[0] + index2 * prices[1] +index3 * prices[2] + index4 * prices[3] + index5 * prices[4] + index6 * prices[5] == money):
                                return 1
    return 0

def getmoneyFast(money):
    prices = [105, 104, 103, 102, 101, 100]
    initialBounds = [floor(money/element) + 1 for element in prices]
    for index1 in range(initialBounds[0]):
        nmoney = money - index1 * prices[0]
        for index2 in range(getNewBound(nmoney,1)):
            nmoney = money - index1 * prices[0] - index2*prices[1]
            for index3 in range(getNewBound(nmoney, 2)):
                nmoney = money - index1 * prices[0] - index2*prices[1] - index3 * prices[2]
                for index4 in range(getNewBound(nmoney, 3)):
                    nmoney = money - index1 * prices[0] - index2*prices[1] - index3 * prices[2] - index4 * prices[3]
                    for index5 in range(getNewBound(nmoney, 4)):
                        nmoney = money - index1 * prices[0] - index2*prices[1] - index3 * prices[2] - index4 * prices[3] - index5 * prices[4]
                        index6 = ((money - (index1 * prices[0] + index2 * prices[1] + index3 * prices[2] + index4 * prices[3] + index5 * prices[4]))/prices[5])
                        if (index6.is_integer()):
                            if (money - index1 * prices[0] - index2*prices[1] - index3 * prices[2] - index4 * prices[3] - index5 * prices[4] - index6*prices[5] == 0):
                                return 1
    return 0



def getNewBound(nmoney, index):
    prices = [105, 104, 103, 102, 101, 100]
    return floor(nmoney/prices[index])+1


print(getmoneyFast(input))
