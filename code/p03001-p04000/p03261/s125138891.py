"""#################################################################
【ABC109】
B_Shiritori
#################################################################"""

#インポート
import sys

#入力用
def ILI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def ISI(): return map(int, sys.stdin.readline().rstrip().split())
def II(): return int(sys.stdin.readline().rstrip())
def ISS(): return sys.stdin.readline().rstrip().split()
def IS(): return sys.stdin.readline().rstrip()

N = II()
txt = []
good = True
for i in range(N):
    txt += [IS()]
for s in txt:
    if txt.count(s) > 1:
        good = False
for i in range(N-1):
    if txt[i][-1] != txt[i+1][0]:
        good = False
if good == True:
    print("Yes")
else:
    print("No")