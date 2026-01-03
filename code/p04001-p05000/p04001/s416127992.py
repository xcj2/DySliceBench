import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    s = S()
    lenth = len(s)
    itr = itertools.product([0,1],repeat=lenth-1)
    ans = 0

    for i in itr:
        tmp = s[0]
        cnt = 0
        for plus,char in zip(i, s[1:]):
            if plus == 1:
                cnt += int(tmp)
                tmp = char
            else:
                tmp += char
        cnt += int(tmp)
        ans += cnt

    print(ans)                
        
main()            
