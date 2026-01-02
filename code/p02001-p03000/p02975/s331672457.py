import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n = I()
    a = LI()
    cnt = collections.Counter(a)
    kind = len(cnt)

    ans = False
    if kind == 1:
        ans |= a[0] == 0
    elif kind == 2:
        key = list(cnt.keys())
        value = list(cnt.values())
        if 0 in key:
            x = key[0]^key[1]
            ans = cnt[0]*2 == cnt[x]
    elif kind == 3:
        key = list(cnt.keys())
        value = list(cnt.values())
        ans = True
        ans &= key[0]^key[1] == key[2]
        ans &= key[1]^key[2] == key[0]
        ans &= key[2]^key[0] == key[1]
        ans &= len(set(value)) == 1
    print("Yes" if ans else "No")
main()
