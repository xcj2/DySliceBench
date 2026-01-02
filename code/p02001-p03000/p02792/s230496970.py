def input_multiple_number():
    return map(int, input().split())

N = int(input())


memo = [[-1]*10 for i in range(10)]
def getCount(head,tail):
    if memo[head][tail] != -1:
        return memo[head][tail]

    if head == 0 or tail == 0:
        memo[head][tail] = 0
        return 0

    cnt = 0

    #digit = 1
    if head == tail and head <= N:
        cnt += 1

    #digit = 2
    if head * 10 + tail <= N:
        cnt += 1 

    for i in range(1,7):
        for j in range(10**i):
            if int(str(head)+str(j).zfill(i)+str(tail))<= N:
                cnt += 1
            else:
                memo[head][tail] = cnt
                return cnt
    return cnt
def getHead(n):
    while n >= 10:
        n //= 10
    return n
def getTail(n):
    return n%10

ans = 0
for i in range(1,N+1):
    ans += getCount(getTail(i),getHead(i))
print(ans)

