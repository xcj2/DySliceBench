import sys

def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

N, A, B = LI()
s = S()
kokunai = 0
kaigai = 0
for i in range(N):
    if s[i] == "a":
        if kokunai + kaigai < A + B:
            kokunai += 1
            print("Yes")
        else:
            print("No")
    elif s[i] == "b":
        if kokunai + kaigai < A + B and kaigai < B:
            kaigai += 1
            print("Yes")
        else:
            print("No")
    elif s[i] == "c":
        print("No")
