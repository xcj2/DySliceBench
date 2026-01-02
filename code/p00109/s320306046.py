import math
def calc_zyouzyo(siki) :
    j = 0
    while True :
        if '*' not in siki and '/' not in siki:
            break
        if siki[j] == '*' :
            siki[j-1] = str(int(siki[j-1]) * int(siki[j+1]))
            del siki[j:j+2]
        elif siki[j] == '/' :
            if (int(siki[j-1]) < 0 and int(siki[j+1]) < 0) or (int(siki[j-1]) >= 0 and int(siki[j+1]) >= 0) :
                siki[j-1] = str(int(siki[j-1]) // int(siki[j+1]))
            else :
                if int(siki[j-1]) % int(siki[j+1]) == 0 :
                    siki[j-1] = str(int(siki[j-1]) // int(siki[j+1]))
                else :
                    siki[j-1] = str(int(siki[j-1]) // int(siki[j+1]) + 1)
            del siki[j:j+2]
        else :
            j += 1
    if len(siki) == 1 :
        return(siki[0])
    else :
        return(siki)
    
def calc_kagen(siki) :
    j = 0
    while True :
        if '+' not in siki and '-' not in siki:
            break
        if siki[j] == '+' :
            siki[j-1] = str(int(siki[j-1]) + int(siki[j+1]))
            del siki[j:j+2]
        elif siki[j] == '-' :
            siki[j-1] = str(int(siki[j-1]) - int(siki[j+1]))
            del siki[j:j+2]
        else :
            j += 1
    if len(siki) == 1 :
        return(siki[0])
    else :
        return(siki)

def calc(siki) :
    siki = calc_zyouzyo(siki)
    siki = calc_kagen(siki)
    return(siki)

n = int(input())
for i in range(n) :
    tmp = list(input())
    siki = []
    num = ''
    for j in range(len(tmp)) :
        if tmp[j] in ['*', '/', '+', '-', '(', ')', '='] :
            if num != '' :
                siki.append(num)
            siki.append(tmp[j])
            num = ''
        else :
            num += tmp[j]
    siki.remove('=')
    j = 0
    while True :
        if j == len(siki) or ')' not in siki:
            break
        stack = []
        if siki[j] == ')' :
            for k in range(j-1,-1, -1) :
                if siki[k] == '(' :
                    break
                else :
                    stack.append(siki[k])
            stack.reverse()
            siki[k] = calc(stack)
            del siki[k+1 : j+1]
            j = k+1
        else :
            j += 1
    siki = calc(siki)
    print(siki)
