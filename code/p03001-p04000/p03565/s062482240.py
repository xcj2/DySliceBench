import sys
 
S = sys.stdin.readline().rstrip()
T = sys.stdin.readline().rstrip()
 
def checkValid(S, i, T):
    try:
        if S[i] == T[0]:
            for j in range(0, len(T)):
                if S[i+j] == T[j] or S[i+j] == '?':
                    pass
                else:
                    return False
        else:
            return False
        return True
    except Exception as e:
        return False
 
def checkValid2(S, i, T):
    try:
        for j in range(0, len(T)):
            if S[i+j] == T[j] or S[i+j] == '?':
                pass
            else:
                return False
        return True
    except Exception as e:
        return False
def getResult(S, i, T):
    res = ""
    for k in range(0, len(S)):
        if k < i:
            res = res + S[k]
        elif k >= i and k < i+len(T):
            res = res + T[k-i]
        else:
            res = res + S[k]
    S = res.replace('?', 'a')
    return S
 
res_list = []
 
res = False
for i in range(0, len(S)):
    if S[i] != '?':
        if checkValid(S, i, T) == True:
            res_list.append(getResult(S, i, T))
            res = True
    else:
        if checkValid2(S, i, T) == True:
            res_list.append(getResult(S, i, T))
            res = True
 
if res == False:
    print("UNRESTORABLE")
else:
    smallest = res_list[0]
    for i in range(0, len(res_list)):
        if smallest > res_list[i]:
            smallest = res_list[i]
    print (smallest)