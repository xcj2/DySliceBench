import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    s = S()
    k = I()
    same = len(set(list(s)))==1
    ans = None

    if same:
        ans = len(s)*k//2
    else:
        if s[0]!=s[-1]:
            cnt = 0
            change = False
            for i in range(1,len(s)):
                if s[i] == s[i-1] and not change:
                    cnt += 1
                    change = True
                else:
                    change = False
            ans = cnt*k
        else:
            char = s[0]
            start = len(s)
            goal = -1
            cnt = 0
            while s[start-1] == char:
                start -= 1
            while s[goal+1] == char:
                goal += 1
            lenth = len(s)-start + goal+1
            cnt += lenth//2 * (k-1)

            ccnt = 0
            change = False
            for i in range(goal+1+1,start):
                if s[i] == s[i-1] and not change:
                    ccnt += 1
                    change = True
                else:
                    change = False
            cnt += ccnt * (k-2)

            ccnt = 0
            change = False
            for i in range(1,start):
                if s[i] == s[i-1] and not change:
                    ccnt += 1
                    change = True
                else:
                    change = False
            cnt += ccnt

            
            ccnt = 0
            change = False
            for i in range(goal+1+1, len(s)):
                if s[i] == s[i-1] and not change:
                    ccnt += 1
                    change = True
                else:
                    change = False
            cnt += ccnt
            ans = cnt
    print(ans)
                
main()
