from collections import defaultdict
import sys
def input(): return sys.stdin.readline().rstrip()
def I(): return int(input())
def S(): return input()
# ----------------------------------------------------------- #

n = I()
s = S()
sa = s[:n]
sb = s[n:][::-1]

A = defaultdict(int)
B = defaultdict(int)

for bit in range(1<<n):
    red_A = []
    red_B = []
    blue_A = []
    blue_B = []
    for i in range(n):
        if bit & 1<<i:
            red_A.append(sa[i])
            blue_B.append(sb[i])
        else:
            blue_A.append(sa[i])
            red_B.append(sb[i])
    a_key = ''.join(red_A) + ',' + ''.join(blue_A)
    b_key = ''.join(blue_B) + ',' + ''.join(red_B)
    A[a_key] += 1
    B[b_key] += 1

ans = 0
for key in A.keys():
    if key in B:
        ans += A[key]*B[key]

print(ans)
