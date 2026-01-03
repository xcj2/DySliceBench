import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    s = S()

    while "B" in s:
        index = s.index("B")
        if index == 0:
            s = s.replace("B","",1)
        else:
            before = s[index-1]
            delete = before+"B"
            s = s.replace(delete,"",1)
    print(s)
main()            
