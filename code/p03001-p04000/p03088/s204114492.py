def int_raw():
    return int(input())

def ss_raw():
    return input().split()

def ints_raw():
    return list(map(int, ss_raw()))

N = int_raw()
memo = [{} for x in range(N+1)]

dna = ["A","C","G","T"]

def chk(last4):
    for i in range(len(last4)):
        l = list(last4)
        if i > 0:
            l[i],l[i-1] = l[i-1],l[i]
        if "AGC" in "".join(l):
            return False
    return True

def rec(idx, last3):
    if idx == N:
        return 1
    elif last3 in memo[idx]:
        return memo[idx][last3]
    else:
        ret =0
        for d in dna:
            if chk(last3 + d):
                ret+= rec(idx+1,last3[1:]+d)
                ret = ret % (10**9+7)
        memo[idx][last3] = ret
        return ret


def ans():
    return rec(0,"TTT")

print(ans())
