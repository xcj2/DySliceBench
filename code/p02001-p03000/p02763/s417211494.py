import sys
input = sys.stdin.readline
N = int(input())
S = input().rstrip()
Q = int(input())
qs = [input().split() for i in range(Q)]

def ctoi(c):
    return ord(c) - ord('a')

bit = [[0]*(N+2) for _ in range(26)]
def bit_add(x,w,ci):
    while x <= N+1:
        bit[ci][x] += w
        x += (x & -x)
def bit_sum(x,ci):
    ret = 0
    while x > 0:
        ret += bit[ci][x]
        x -= (x & -x)
    return ret

for i,c in enumerate(S):
    bit_add(i+1,1,ctoi(c))

s = list(S)
ans = []
for a,b,c in qs:
    if a=='1':
        x = int(b)
        bit_add(x,1,ctoi(c))
        bit_add(x,-1, ctoi(s[x-1]))
        s[x-1] = c
    else:
        tmp = 0
        for i in range(26):
            if bit_sum(int(c),i) - bit_sum(int(b)-1,i) > 0:
                tmp += 1
        ans.append(tmp)
print(*ans, sep='\n')