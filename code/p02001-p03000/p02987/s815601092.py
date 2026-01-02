import sys
sys.setrecursionlimit(10**7)
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
INF = 10 ** 18
MOD = 10 ** 9 + 7

def main(): 
    s = SI()
    from  collections import Counter
    co = Counter(s)
    if len(co) == 2:
        for i in co:
            if co[i] != 2:
                print('No')
                return
            print('Yes')
            return
    else:
        print('No')
        return
main()