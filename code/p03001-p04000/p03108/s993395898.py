import math

def nCr(n,r):

    if n-r >= 0:
        return math.factorial(n) // (math.factorial(n-r) * math.factorial(r))
    else:
        return 0

def nC2(n):
    if n-2 >= 0:
        return (n*(n-1)) // 2
    else:
        return 0

def wantp(n): #Union-Find木の親の探索

    nown = n
    Q = []
    cnt = 0
    while True:

        if nown != p[nown]:
            Q.append(nown)
            nown = p[nown]

        else:
            for i in Q: #探索した途中にあるノードの親を根に変更
                p[i] = nown
                cnt += 1

            break

        cnt += 1

        if cnt > 10:
            print (n,nown,p[nown])

    return nown


N,M = map(int,input().split())

AB = []
for i in range(M):

    A,B = map(int,input().split())

    AB.append([A-1,B-1])

AB.reverse()


ans = []
ans.append(nCr(N,2))

p = [] #親
c = [] #子の数
rank = [1] * N #そのノードの子で構成された木の深さ

for i in range(N):

    p.append(i)
    c.append(1)

for i in range(M): #最後の橋から1本ずつ足していく

    #if i % 1000 == 0 or i > 25000:
        #print (i)

    #if i > 25000 : print ("A")

    a = AB[i][0]
    b = AB[i][1]

    #if i > 25000 : print ("B") 

    ap = wantp(a)
    bp = wantp(b)

    #if i > 25000 : print ("C")

    now = ans[-1]

    if ap != bp: #前回の答えから導出、Union-Find木の結合
        now = now + nC2(c[ap]) + nC2(c[bp]) - nC2(c[ap]+c[bp])

        #if i > 25000 : print ("D")

        if rank[ap] > rank[bp]:

            p[bp] = ap
            c[ap] += c[bp]

        elif rank[ap] < rank[bp]:

            p[ap] = bp
            c[bp] += c[ap]

        else:

            p[ap] = bp
            c[bp] += c[ap]

            rank[bp] += 1

        #if i > 25000 : print ("E")

    ans.append(now)
    #if i > 25000 : print ("F")
    #print (now,p)

#print ("test")
ans.reverse()

for i in range(M):
    print (ans[i+1])
