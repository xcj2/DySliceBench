def getN():
    return int(input())

def getMN():
    a = input().split()
    b = [int(i) for i in a]
    return b[0],b[1]

def getlist():
    a = input().split()
    b = [int(i) for i in a]
    return b

def zen(n,used, new):

    usednum = len(used|set([new]))
    #print("keta",usednum)
    if n == 0:
        if usednum == 3:
            return 1
        else:
            return 0

    if usednum == 3:
        return 3**n
    if usednum == 2:
        return 3**n - 2**n
    if usednum == 1:
        return 3**n - 2*(2**n) +1
    return 3**n - 3*(2**n) + 3

def simo_init(n):
    if n == 0:
        return 0
    return 3 ** n - 3 * (2 ** n) + 3

n = input()
digit = len(n)

answer = 0
for i in range(digit):
    answer += simo_init(i)

def get_simo(n, dig,used):
    global answer
    if n == "":
        if len(used) == 3:
            answer += 1
        return
    if int(n[0]) > 3:
        answer += zen(dig-1, used, 3)
    if int(n[0]) > 5:
        answer += zen(dig-1, used, 5)
    if int(n[0]) > 7:
        answer += zen(dig-1, used, 7)

    #print("all: ",answer)
    #print("dig: ", dig, n)
    first = int(n[0])
    if first in [3,5,7]:
        get_simo(n[1:], dig-1, used|set([first]))


get_simo(n,digit,set())
print(answer)

#print(zen(3,set()))
