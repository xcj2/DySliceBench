import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n = I()
    s = S()
    rgb = ["R","G","B"]
    rgb_st = set(rgb)
    rgb_acc = [[0]*n for _ in range(3)]
    index = rgb.index(s[0])
    rgb_acc[index][0] += 1
    ans = 0

    for i in range(1,n):
        for j in range(3):
            rgb_acc[j][i] = rgb_acc[j][i-1]
        index = rgb.index(s[i])
        rgb_acc[index][i] += 1
    
    for i in range(n-2):
        for j in range(i+1,n-1):
            if s[i] != s[j]:
                ex = (rgb_st-{s[i],s[j]}).pop()
                index = rgb.index(ex)
                cnt = rgb_acc[index][-1] - rgb_acc[index][j]
                if j<2*j-i<n:
                    if s[2*j-i] == ex:
                        cnt -= 1
                ans += cnt
    print(ans)
main()
