import sys
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def II(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def SI(): return input()
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')

def main():
    N, M = LI()
    demands = []
    for i in range(M):
        demands.append(LI())

    demands = sorted(demands, key=lambda x: x[1])
    demands_met_flag = [False]*len(demands)

    counter = 0
    deleting_bridge = 0
    for i in range(len(demands)):
        if demands_met_flag[i] == True: continue
        if demands[i][0] <= deleting_bridge:
            demands_met_flag[i] = True
            continue
        demand = demands[i]
        demands_met_flag[i] = True
        counter += 1
        deleting_bridge = demand[1]-1

    print(counter)

main()
