def read_data():
    X, Y, E = map(int, input().split())
    Ss = list(range(X))
    Ts = list(range(X, X + Y))
    Es = []
    for i in range(E):
        x, y = map(int, input().split())
        Es.append((x, y + X))
    return Ss, Ts, Es
    

def bp_match(Ss, Ts, Es):
    '''2??¨??°???????????????????????°???????????¨??????
    '''
    super_source = len(Ss) + len(Ts)
    super_target = super_source + 1
    Cs = [dict() for i in range(super_target + 1)]
    for si, ti in Es:
        Cs[si][ti] = 1
        Cs[ti][si] = 0
    for si in Ss:
        Cs[super_source][si] = 1
        Cs[si][super_source] = 0
    for ti in Ts:
        Cs[super_target][ti] = 0
        Cs[ti][super_target] = 1
    return dinic(Cs, super_target + 1, super_source, super_target)

def dinic(cf, nV, s, t):
    dist = get_distance(cf, s, t)
    while dist[t] > 0:
        df = dfs(dist, cf, s, t, float('inf'))
        while df:
            df = dfs(dist, cf, s, t, float('inf'))
        dist = get_distance(cf, s, t)
    return sum(cf[t].values())

def get_distance(cf, s, t):
    dist = [-1] * len(cf)
    dist[s] = 0
    frontiers = [s]
    while frontiers:
        new_frontiers = []
        for u in frontiers:
            for v, capacity in cf[u].items():
                if dist[v] == -1 and capacity > 0:
                    dist[v] = dist[u] + 1
                    new_frontiers.append(v)
        frontiers = new_frontiers
    return dist

def dfs(dist, cf, u, t, df):
    if u == t:
        return df
    for v, capacity in cf[u].items():
        if dist[v] > dist[u] and capacity > 0:
            new_df = dfs(dist, cf, v, t, min(df, capacity))
            if new_df > 0:
                cf[u][v] -= new_df
                cf[v][u] += new_df
                return new_df
    return 0

if __name__ == '__main__':
#    Ss = [0, 1, 2, 3, 4]
#    Ts = [5, 6, 7, 8]
#    Es = [(0, 5), (1, 5), (1, 7), (2, 6), (2, 7), (2, 8), (3, 7), (4, 7)]
    Ss, Ts, Es = read_data()
    print(bp_match(Ss, Ts, Es))