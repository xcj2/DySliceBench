

def solve():

    mini = 10**9
    combs = getcombs(n)
    for com in combs:
        skill = [0] * m
        price = 0
        for i in range(n):
            if int(com[i]):
                price += c[i]
                addvec(skill, a[i])
                if min(skill) >= x:
                    mini = min(mini, price)
    if mini!=10**9:
        print(mini)
    else:
        print(-1)
    return


def getcombs(n):
    combs = []
    for i in range(2**n):
        combs.append(format(i, '#0{}b'.format(n+2))[2:])
    return combs






def addvec(a,b):
    for i in range(len(a)):
        a[i] += b[i]


#s= input()
n,m, x = [int(i) for i in input().split(" ")]
c = []
a = []
for _ in range(n):
    read = [int(i) for i in input().split(" ")]
    c.append(read[0])
    a.append(read[1:])
solve()
