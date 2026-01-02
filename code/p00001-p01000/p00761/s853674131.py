def main():
    while True:
        line = input().split()
        num = line[0]
        digit = int(line[1])
        if digit == 0: break
        if num == '0':
            print("0 0 1")
            continue

        num = addzero(num, digit)

        numlist = [num]

        for i in range(20):
            nextt = nextnum(numlist[i])

            j = isnew(numlist, nextt)

            if not(j == -1):
                print(j, int(nextt), (i + 1) - j)
                break
            else: numlist.append(nextt)
        
def nextnum(strr):
    listt = []
    length = len(strr)
    for item in strr:
        listt.append(item)
    maxlist = listt.copy()
    minlist = listt.copy()
    maxlist.sort(reverse = True)
    minlist.sort(reverse = False)
    while True:
        if minlist == ['0']: break
        elif minlist[0] == '0':
            r = minlist.remove('0')
        else: break
    maxnum = int("".join(maxlist))
    minnum = int("".join(minlist))

    diststr = str(maxnum - minnum)
    diststr = addzero(diststr, length)

    return diststr

def addzero(strr, digit):
    return ("0" * (digit - len(strr)) + strr)

def isnew(listt, elem):
    for j in range(len(listt)):
        if listt[j] == elem: return j
    return -1

def StoI(strr):
    while True:
        for item in strr:
            if strr == '0': break
            elif minlist[0] == '0':
                r = minlist.remove('0')
            else: break

main()

