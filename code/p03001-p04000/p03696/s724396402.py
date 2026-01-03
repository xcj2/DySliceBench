import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():

    n = I()
    s = S()

    cnt = 0
    right = 0
    
    for char in s:
        if char == "(":
            cnt += 1
        else:
            if cnt == 0:
                right += 1
            else:
                cnt -= 1

    ans = "("*right + s + ")"*cnt

    print(ans) 
    

        


main()
