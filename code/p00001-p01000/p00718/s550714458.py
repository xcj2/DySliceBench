def main():
    d_num = int(input())
    for i in range(d_num):
        a, b = map(str, input().split(" "))
        print(NtoS(StoN(a) + StoN(b)))

def StoN(mcxi):
    slist = list(mcxi)
    for i in range(len(slist)):
        if slist[i] == 'm': slist[i] = 1000
        elif slist[i] == 'c': slist[i] = 100
        elif slist[i] == 'x': slist[i] = 10
        elif slist[i] == 'i': slist[i] = 1
        else: slist[i] = int(slist[i])
        
    num = 1
    summ = 0
    for item in slist:
        if item == 1000 or item == 100 or item == 10 or item == 1:
            summ += num * item
        else:
            num = item
            continue
        num = 1

    return summ

def NtoS(num):
    mcxi = ""
    n1000 = num // 1000
    n100 = (num - n1000 * 1000) // 100
    n10 = (num - n1000 * 1000 - n100 * 100) // 10
    n1 = (num - n1000 * 1000 - n100 * 100 - n10 * 10)
    
    if n1000 != 0:
        if n1000 == 1: mcxi = mcxi + "m"
        else: mcxi = mcxi + str(n1000) + "m"
    if n100 != 0:
        if n100 == 1: mcxi = mcxi + "c"
        else: mcxi = mcxi + str(n100) + "c"
    if n10 != 0:
        if n10 == 1: mcxi = mcxi + "x"
        else: mcxi = mcxi + str(n10) + "x"
    if n1 != 0:
        if n1 == 1: mcxi = mcxi + "i"
        else: mcxi = mcxi + str(n1) + "i"
    return mcxi
main()

