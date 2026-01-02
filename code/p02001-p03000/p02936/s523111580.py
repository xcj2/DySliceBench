import sys

def I(): return(int(sys.stdin.readline()))
def LI(): return([int(x) for x in sys.stdin.readline().split()])

def main():
    N,Q = LI()
    node=[[] for _ in range(N)]
    flag = [True for _ in range(N)]
    for _ in range(N-1):
        a,b = LI()
        node[a-1].append(b-1)
        node[b-1].append(a-1)

    counter = [0] * N
    for _ in range(Q):
        p,x = LI()
        counter[p-1] += x

    que = [[0,0]]
    while que:
        a,c = que.pop()
        flag[a]=False
        counter[a]+=c
        for b in node[a]:
            if flag[b]:
                que.append([b,counter[a]])

    r = [counter[i] for i in range(N)]

    return(" ".join(map(str,r)))

if __name__ == "__main__":
    print(main())
