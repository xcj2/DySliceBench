#インポート
import sys

#入力用
def ILI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def ISI(): return map(int, sys.stdin.readline().rstrip().split())
def II(): return int(sys.stdin.readline().rstrip())
def ISS(): return sys.stdin.readline().rstrip().split()
def IS(): return sys.stdin.readline().rstrip()

A, B = ISI()
S = IS()
Num = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9"]
a = S[:A]
b = S[A+1:]
c = S[A]
good = True
for _a in a:
    if _a in Num:
        continue
    else:
        good = False
for _b in b:
    if _b in Num:
        continue
    else:
        good = False
if c != "-":
    good = False
if good == True:
    print("Yes")
else:
    print("No")