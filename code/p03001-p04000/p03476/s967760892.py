def sieve(N):
    global table,prime
    table = [True]*(N+1)
    table[0] = False
    table[1] = False
    prime = []
    for i in range(2,N+1):
        if table[i]:
            prime.append(i)
            for j in range(2*i,N+1,i):
                table[j] = False

def accmulate(array):
    global cs
    cs = [0]*(len(array)+1)
    for i in range(len(array)):
        cs[i+1] = cs[i] + array[i]

def query(l,r):
    return cs[r+1] - cs[l]

Q = int(input())

sieve(10**5)

def judge(x):
    return x % 2 and table[x] and table[(x+1)//2]

flag = [judge(x) for x in range(0,10**5+1)]

accmulate(flag)

ans_list = []

for _ in range(Q):
    l,r = map(int,input().split())
    ans = query(l,r+1)
    ans_list.append(ans)

print(*ans_list, sep="\n")