import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip.split())
def main():
    s = S()
    alldic = collections.Counter(s)
    wnum = alldic["W"]
    leftdic = collections.Counter(s[:wnum])
    leftbnum = leftdic["B"]
    right_w_in = wnum-1
    left_b_in = right_w_in + 1
    ans = leftbnum

    for i,x in enumerate(s):
        if i<=right_w_in:
            if x == "B":
                ans += right_w_in - i
        elif i>=left_b_in:
            if x == "W":
                ans += i - left_b_in
    
    print(ans)
main()