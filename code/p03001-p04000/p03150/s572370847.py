import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    s = S()
    key_lst = []
    for i in range(0,8):
        key_lst.append(["keyence"[:i],"keyence"[i:]])
    ans = False
    for b,f in key_lst:
        st = s[:len(b)]
        go = s[len(s)-len(f):]
        if st == b and go == f:
            ans = True
    

    print("YES" if ans else "NO")
main()                  
