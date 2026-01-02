import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    s = S()
    if len(s)<26:
        for char in string.ascii_lowercase:
            if char not in s:
                print(s+char)
                break
    else:
        for i in range(25, -1, -1):
            ex = s[i:]
            late = list(ex)
            late.sort(reverse=True)
            late = "".join(late)
            if ex != late:
                index = late.index(s[i])
                ans = s[:i] + late[index-1]
                print(ans)
                break
        else:
            print(-1)
    

main()
