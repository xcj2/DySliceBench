def main():
    n=int(input())
    MOD=10**9+7
    memo = [{} for i in range(n+1)]

    def ok(l4):
        for i in range(4):
            t=list(l4)
            if i>=1:
                t[i],t[i-1]=t[i-1],t[i]
            if ''.join(t).count('AGC')>=1:
                return False
        return True

    def dfs(cur,l3):
        if l3 in memo[cur]:
            return memo[cur][l3]
        if cur==n:
            return 1
        ret=0
        for c in 'ACGT':
            if ok(l3+c):
                ret=(ret+dfs(cur+1,l3[1:]+c))%MOD
        memo[cur][l3]=ret
        return ret
    
    print(dfs(0,'TTT'))

if __name__ == '__main__':
    main()