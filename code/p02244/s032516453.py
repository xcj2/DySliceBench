from functools import lru_cache
cc = [["." for i in range(8)] for j in range(8)]

@lru_cache(maxsize=None)     
def dia(s,a,b):
    d = []
    for i in range(8):
        for j in range(8):
            try:
                if j + (a - i) == b: 
                    d.append(s[i][j])
                if j -  (a - i) == b:
                    d.append(s[i][j])
                if j + (i - a) == b: 
                    d.append(s[i][j])
                if j -  (i - a) == b:
                    d.append(s[i][j])
            except IndexError: continue
    print(d)
    return d


def check(cc,a,b):
    ss = list(zip(*cc))
    if 'Q' in cc[a]: return False
    if 'Q' in ss[b]: return False
    d = []
    for i in range(8):
        for j in range(8):
            try:
                if j + (a - i) == b: 
                    d.append(cc[i][j])
                if j -  (a - i) == b:
                    d.append(cc[i][j])
                if j + (i - a) == b: 
                    d.append(cc[i][j])
                if j -  (i - a) == b:
                    d.append(cc[i][j])
            except IndexError: continue
    if 'Q' in d: return False
    return True

def chess(s,queen):
    if queen == 8:
        return s
    for i in range(8):
        for j in range(8):
            if check(s,i,j):
                sol = s
                sol[i][j] = 'Q'
                if chess(sol,queen+1) != [[]]:
                    return sol
                else: sol[i][j] = "."
    return [[]]


k = int(input())
for i in range(k):
    a, b = input().split()
    cc[int(a)][int(b)] = 'Q'
ans = chess(cc,k)
print('\n'.join(list(map(lambda x: ''.join(x),ans))) )
