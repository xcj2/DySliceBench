import sys
input = sys.stdin.readline

def two_int():
    N, K = map(int, input().split())
    return N,K

def one_int():
    return int(input())

def one_str():
    return input()

def many_int():
    return list(map(int, input().split()))


def main():
    N, M =two_int()

    key_list=[]
    treasures=[]
    check={}

    for i in range(M):
        mon,_ =two_int()
        temp = map(lambda x: 1<<(x-1), many_int())
        sums = sum(temp)
        
        if sums in check:
            if check[sums] > mon:
                check[sums]=mon
        else:
            check[sums]=mon
            
    for k,v in check.items():
        key_list.append(v)
        treasures.append(k)

    max_index=2**N
    INF=10**15

    dp=[INF for i in range(max_index)]
    dp[0]=0
    M=len(key_list)

    for i in range(max_index-1):
        for j in range(M):
            new_i = int(bin(treasures[j] | i),2)
            cost = dp[i] + key_list[j]
            dp[new_i] = min(dp[new_i], cost) 
        
    goal_index=max_index-1
    if dp[goal_index]!=INF:
        print(dp[goal_index])
    else:
        print(-1)

main()