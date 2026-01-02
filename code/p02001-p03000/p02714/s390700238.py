from collections import *
import sys
try: inp = raw_input
except: inp = input
def err(s):
    sys.stderr.write('{}\n'.format(s))

def ni():
    return int(inp())

def nl():
    return [int(_) for _ in inp().split()]

N = ni()
S = inp()

NO = {}
for c in 'RBG':
    NO[c] = S.count(c)

left = {}
nbr = {k:0 for k in 'RGB'}
for i, c in enumerate(S):
    nbr[c] += 1
    for c in 'RBG':
        left[i,c] = NO[c] - nbr[c]

sm = 0
for i in range(N):
    for j in range(i+1, N):
        if S[i] == S[j]: continue
        c = 'RGB'.replace(S[i], '').replace(S[j], '')
        cnt = left[j,c]
        k = 2*j - i
        if k < N and S[k] == c:
            cnt -= 1
        sm += cnt
print(sm)

