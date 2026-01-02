def getN():
    return int(input())


def getNM():
    return map(int, input().split())


def getList():
    return list(map(int, input().split()))

n,m = getNM()
children = [[] for i in range(n+2)]
n_in = [0] * (n+1)
par_origin = [0] * (n+1)

#入力の処理
for i in range(n+m-1):
    a,b = getNM()
    children[a].append(b)
    n_in[b] += 1

#根を見つける
for i in range(1,n+m-1):
    if n_in[i]:
        pass
    else:
        root = i
        break

#次数を減らしながら探索
import queue
def bfs(root):
    q = queue.Queue()
    q.put(root)
    while(True):
        try:
            cur = q.get(block=False)
        except:
            break
        for c in children[cur]:
            if n_in[c] == 1:
                par_origin[c] = cur
                q.put(c)
            else:
                n_in[c] -= 1

bfs(root)
for i in range(1, n+1):
    print(par_origin[i])

