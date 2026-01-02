#!/usr/bin/env python3

import sys


def lms(t, i):
    return i > 0 and not t[i-1] and t[i]


def induced_sort(s, k, t, lmss):

    sa = [-1] * len(s)
    cbin = [0]*k

    for c in s:
        cbin[c] += 1

    ssum = 0
    for i in range(k):
        ssum += cbin[i]
        cbin[i] = ssum

    count = [0] * k
    for i in reversed(lmss):
        c = s[i]
        sa[cbin[c]-1 - count[c]] = i
        count[c] += 1

    count = [0] * k
    for i in sa:
        if i <= 0 or t[i-1]:
            continue
        c = s[i-1]
        sa[cbin[c-1] + count[c]] = i-1
        count[c] += 1
        
    count = [0] * k
    for i in reversed(sa):
        if i <= 0 or not t[i-1]:
            continue
        c = s[i-1]
        sa[cbin[c]-1 - count[c]] = i-1
        count[c] += 1

    return sa


def sa_is(s, k):
    slen = len(s)
    t = [True] * slen # S -> True, T -> False
    for i in range(slen-2, -1, -1):
        #if s[i] < s[i+1]:   t[i] = True #'S'
        if s[i] > s[i+1]:
            t[i] = False # 'L'
        elif s[i] == s[i+1]:
            t[i] = t[i+1]

    lmss = []
    for i in range(1,slen):
        if not t[i-1] and t[i]: # lms(t, i):
            lmss.append(i)

    seed = lmss

    sa = induced_sort(s, k, t, seed)

    new_sa = []
    for i in sa:
        if lms(t, i): new_sa.append(i)

    nums = dict() #    nums = [[]] * (max(new_sa)+1)
    nums[new_sa[0]] = 0
    num = 0
    for o in range(len(new_sa)-1):
        i, j = new_sa[o], new_sa[o+1]
        diff, d = False, 0
        for d in range(slen):
            if s[i+d] != s[j+d] or lms(t, i+d) != lms(t, j+d):
                diff = True
                break
            elif d > 0 and (lms(t, i+d) or lms(t, j+d)):
                break
        if diff:
            num += 1
        nums[j] = num

#    for i in range(len(nums)-1,-1,-1):
#        if not nums[i]: nums.pop(i)
    nums = list(map(lambda x: x[1], sorted(nums.items())))

    if num + 1 < len(nums):
        sa = sa_is(nums, num+1)
    else:
        sa = [[]] * (max(nums)+1)
        for i, c in enumerate(nums):
            sa[c] = i

    seed = list(map(lambda x:lmss[x], sa))
    sa = induced_sort(s, k, t, seed)

    return sa


def strcmp(a, b):
    for i, bi in enumerate(b):
        if a[i] == bi: continue
        return a[i]-bi
    return 0


def search(s, sa, slen, q):
    ss = 0
    ee = slen
    while ss <= ee:
        mid = (ss+ee)//2
        if mid >= slen: break
        rr = strcmp(s[sa[mid]:], q)
        if rr==0: return 1
        if rr >= 0:
            ee = mid-1
        else:
            ss = mid+1
    return 0


if __name__ == '__main__':

    b = sys.stdin.readline().rstrip()
    b = (b+'$').encode()
    sa = sa_is(b, 128) #ord('z'))
    n = int(sys.stdin.readline())
    for _ in range(n):
        q = sys.stdin.readline().rstrip().encode()
        if search(b, sa, len(b), q) > 0:
            print(1)
        else:
            print(0)

