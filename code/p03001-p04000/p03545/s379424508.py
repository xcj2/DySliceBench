import sys,collections
sys.setrecursionlimit(10**7)
def Is(): return [int(x) for x in sys.stdin.readline().split()]
def Ss(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

s = S()
a,b,c,d = s[0],s[1],s[2],s[3]

def calc(i,j,k):
    if i == 0:
        i = 1
    else:
        i = -1
    if j == 0:
        j = 1
    else:
        j = -1
    if k == 0:
        k = 1
    else:
        k = -1       
    return int(a) + int(b)*i + int(c)*j + int(d)*k,i,j,k

def pm(s):
    if s == 0:
        return "+"
    else:
        return "-"
    
for i in range(2):
    for j in range(2):
        for k in range(2):
            if calc(i,j,k)[0] == 7:
                print(a+pm(i)+b+pm(j)+c+pm(k)+d+"=7")
                exit()