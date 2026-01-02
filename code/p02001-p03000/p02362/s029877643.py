import math
inf = math.inf
negative_cycle_flag = False

def INITSS (G, s): # s means start
    # for u in G.V:
    #      u.d = inf
    #      u.pi = None
    G.V_d[s] = 0


def RELAX(u, v, w, V_d, V_pi):
    if V_d[v] > V_d[u] + w[u][v]:
        V_d[v] = V_d[u] + w[u][v]
        V_pi[v] = u


def BELLMANFORD (G, s, w):# w is weight matrix
    global negative_cycle_flag
    INITSS(G, s)
    for i in range(1,len(G.V_d)):
        for u, v in G.E:
            RELAX(u, v, w, G.V_d, G.V_pi)

    for u, v in G.E:
        if G.V_d[u] + w[u][v] < G.V_d[v]:
            negative_cycle_flag = True
            break

class Graph:
    def __init__(self, v_num, e_num, E):
        self.V_d = [inf for _ in range(v_num)]
        self.V_pi = [None for _ in range(v_num)]
        self.E = E

v_num, e_num, s = map(int, input().split())
E =[]
w = [[inf for _ in range(v_num)] for _ in range(v_num)]
for _ in range(e_num):
    u, v, weight = map(int, input().split())
    w[u][v] = weight
    E.append((u, v))

G = Graph(v_num, e_num, E)

BELLMANFORD(G, s, w)
if negative_cycle_flag == True:
    print("NEGATIVE CYCLE")
else:
    for k in range(v_num):
        if(G.V_d[k]==inf):
            print("INF")
        else:
            print(G.V_d[k])


