import sys
import re
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
def input():
    return sys.stdin.readline().rstrip()

def main():
    N=int(input())
    def is_ok(S):
        if re.match(r'(.?(AGC|GAC|ACG).?|A(.G|G.)C)',S):
            return False
        else:
            return True
    memo=[{} for _ in range(N+1)]
    def saiki(i,last3):
        if last3 in memo[i]:
            return memo[i][last3]
        if i==N:
            return 1
        c=0
        for s in 'ATGC':
            if is_ok(last3+s):
                c+=saiki(i+1,last3[1:]+s)
                c%=MOD
        memo[i][last3]=c
        return c
    print(saiki(0,'TTT'))
            
    

if __name__ == '__main__':
    main()
