import copy

def init(init_val):
    for j in range(26):
        #set_val
        for i in range(n):
            if init_val[i] == j:
                seg[j][i+num-1] = 1
        #built
        for i in range(num-2,-1,-1):
            seg[j][i] = seg[j][2*i+1] | seg[j][2*i+2]


def update(k, cs):
    ls = s[k]
    if ls == cs:
        return
    k += num-1
    seg[cs][k] = 1
    seg[ls][k] = 0
    while k:
        k = (k-1)//2
        seg[ls][k] = seg[ls][k*2+1] | seg[ls][k*2+2]
        seg[cs][k] = seg[cs][k*2+1] | seg[cs][k*2+2]


def query(pp, qq): # pからq-1までの最大値
    pp += num-1
    qq += num-2
    total = 0
    for j in range(26):
        p = copy.deepcopy(pp)
        q = copy.deepcopy(qq)
        res = 0
        while q - p > 1:
            if res == 1:
                break
            if p&1 == 0:
                res = res | seg[j][p]
            if q&1 == 1:
                res = res | seg[j][q]
                q -= 1
            p = p//2
            q = (q-1)//2
        if q - p > 1:
            total += res
            continue
        if p == q:
            res = res | seg[j][p]
        else:
            res = res | seg[j][p] | seg[j][q]
        total += res
    return total


n = int(input())
s = list(input())
q = int(input())

for i in range(n):
    s[i] = ord(s[i]) - 97
#num:n以上の最小の2のべき乗
num = 2**(n-1).bit_length()
seg = [[0]*(2*num) for i in range(26)]
init(s)
for i in range(q):
    cq = list(input().split())
    if cq[0] == '1':
        cn, cs = int(cq[1]) - 1, ord(cq[2]) - 97
        update(cn, cs)
        s[cn] = cs
    if cq[0] == '2':
        p, q = int(cq[1]) - 1, int(cq[2])
        print(query(p, q))
