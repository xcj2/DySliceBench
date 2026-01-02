import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n = I()
    s = S()
    rgb = [None for _ in range(n)]
    rgb_acc = [None for _ in range(n)]
    rgb_st = {"R","G","B"}
    rgb_lst = ["R","G","B"]
    for i, char in enumerate(s):
        if char == "R":
            rgb[i] = [1,0,0]
        elif char == "G":
            rgb[i] = [0,1,0]
        else:
            rgb[i] = [0,0,1]
    
    rgb_acc[0] = rgb[0]
    for i in range(1, n):
        rgb_acc[i] = rgb_acc[i-1][:]
        rgb_acc[i][rgb[i].index(1)] += 1
    
    ans = 0
    for i in range(n-2):
        for j in range(i+1,n-1):
           if s[i]!=s[j]:
                ex = rgb_st - {s[i], s[j]}
                ex = ex.pop()
                index = rgb_lst.index(ex)
                cnt = rgb_acc[n-1][index]-rgb_acc[j][index]
                if j+1 <= 2*j-i < n:
                    if s[2*j-i] == ex:
                        cnt -= 1
                ans += cnt

    print(ans)
main()