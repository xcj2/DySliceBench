import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    s = "#" + S()
    llst = [0 for _ in range(len(s))]
    rlst = [0 for _ in range(len(s))]
    ans_lst = [0 for _ in range(len(s))]
    num = 10**100

    for i in range(len(s)):
        if s[i] == "L":
            llst[i] = llst[i-1] + 1

    for i in range(len(s)-1, -1, -1):
        if s[i] == "R":
            rlst[i] = rlst[i+1] + 1

    for i in range(1,len(s)):
        if s[i] == "L":
            x = i - llst[i]
            ans_lst[i] = x if (num-(i-x))%2==0 else x+1
            # print(x,i,(num-(i-x))%2==0)
        else:
            x = i + rlst[i]
            ans_lst[i] = x if (num-(x-i))%2==0 else x-1
            # print(x,i,(num-(x-i))%2==0)


    # print(*ans_lst[1:])

    ans = [0 for _ in range(len(s))]
    for i in range(1,len(s)):
        ans[ans_lst[i]] += 1

    print(*ans[1:])

main()
