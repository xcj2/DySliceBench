import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
nums = [None]*n

### BIT 
def init(bit, values):
    for i,v in enumerate(values):
        update(bit,i,v)
#a1 ~ aiまでの和 O(logn)
def query(bit,i):
    res = 0
    while i > 0:
        res += bit[i]
        i -= i&(-i)
    return res

#ai += x(logN)
def update(bit,i,x):
    while i <= len(bit)-1:
        bit[i] += x
        i += i&(-i)
    return


# 転倒数を求める例
def tento(l):
    n = len(l)
    # 1-indexedなので注意
    bit = [0] * (n+1)
    ans = 0
    for i,ind in enumerate(l):
        ans += (i - query(bit, ind+1))
        update(bit, ind+1, 1)
    return ans


def pp(func):
    def wrapped(*args, **keys):
        print(args, keys)
        val = func(*args, **keys)
        print(val)
        return val
    return wrapped

# @pp
def sub(fr, to, bb):
    # frをtoのいずれかに対応付ける
    elist = []
    olist = []
    for ff,bbb in zip(fr, bb):
        if (ff+bbb)%2:
            olist.append(ff)
        else:
            elist.append(ff)

    elist2 = []
    olist2 = []
    for item in to:
        if item%2:
            olist2.append(item)
        else:
            elist2.append(item)
    if len(olist2)==len(olist) and len(elist2)==len(elist):
        olist.sort()
        elist.sort()
        if to[0]%2==0:
            res = [(elist if i%2==0 else olist)[i//2] for i in range(len(to))]
            return res
        else:
            res = [(olist if i%2==0 else elist)[i//2] for i in range(len(to))]
            return res
    else:
        return None
    
    
best = 10**9
for bit in range(1<<n):
    for i in range(n):
        val = b[i] if bit>>i&1 else a[i]
        nums[i] = (val, i, bit>>i&1)
    nums.sort()
    prev, fr, bb = nums[0]
    to = [0]
    fr = [fr]
    bb = [bb]
    valid = True
    array = []
    for i in range(1,n):
        cv, cfr, cbb = nums[i]
        if prev!=cv:
            res = sub(fr, to, bb)
            if res is None:
                valid = False
                break
            array.extend(res)
            prev, fr, bb = cv, [cfr], [cbb]
            to = [i]
        else:
            fr.append(cfr)
            to.append(i)
            bb.append(cbb)
    else:
        res = sub(fr, to, bb)
        if res is None:
            valid = False
        else:
            array.extend(res)
    if valid:
        ans = tento(array)
#         print(array)
        best = min(best, ans)
#         print(nums, ans)
if best==10**9:
    print(-1)
else:
    print(best)