import sys
sys.setrecursionlimit(700000)

def s_in():
    return input()

def n_in():
    return int(input())

def l_in():
    return list(map(int, input().split()))

n,a,b,c=l_in()
S=[s_in() for _ in range(n)]
current = [a,b,c]

def add_a():
    current[0]+=1
    res.append('A')

res = []

for i, s in enumerate(S):
    if s == 'AB':
        if a == 0 and b == 0:
            break
        if a > b:
            a -= 1
            b += 1
            res.append('B')
        elif a < b or i == n-1:
            a += 1
            b -= 1
            res.append('A')
        else:
            if 'A' in S[i+1]:
                a += 1
                b -= 1
                res.append('A')
            else:
                a -= 1
                b += 1
                res.append('B')
                
                
    if s == 'AC':
        if a == 0 and c == 0:
            break
        if a > c:
            a -= 1
            c += 1
            res.append('C')
        elif a<c  or i == n-1:
            a += 1
            c -= 1
            res.append('A')
        else:
            if 'A' in S[i+1]:
                a += 1
                c -= 1
                res.append('A')
            else:
                a -= 1
                c += 1
                res.append('C')
            
    if s == 'BC':
        if c == 0 and b == 0:
            break
        if b > c:
            b -= 1
            c += 1
            res.append('C')
            
        elif b<c  or i == n-1:
            b += 1
            c -= 1
            res.append('B')
        else:
            if 'B' in S[i+1]:
                b += 1
                c -= 1
                res.append('B')
            else:
                b -= 1
                c += 1
                res.append('C')
            
else:
    print('Yes')
    [print(r) for r in res]
    exit()

print('No')
            
            
        
