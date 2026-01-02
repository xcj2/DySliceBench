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
    s = s.replace('LR', 'LxR').split('x')

    ans = []
    for rl in s:
        r_pos = rl.find('RL')
        for _ in range(r_pos):
            ans.append(0)
        if len(rl)%2 == 0:
            r_count = len(rl)//2
            l_count = len(rl)//2
        else:
            if r_pos%2 == 0:
                r_count = len(rl)//2 + 1
                l_count = len(rl)//2
            else:
                r_count = len(rl)//2
                l_count = len(rl)//2 + 1
        ans.append(r_count)
        ans.append(l_count)
        for _ in range(r_pos+2, len(rl)):
            ans.append(0)
    print(' '.join([str(i) for i in ans]))
        


main()