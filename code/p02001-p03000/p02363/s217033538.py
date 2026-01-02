import sys
input = sys.stdin.readline

INF = float('inf')
    
def warshall_floyd(V, dist):
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

def check_negative_cycle(V, dist):
    dist = warshall_floyd(V, dist)
    
    for i in range(V):
        if dist[i][i] != 0: return dist, True
        
    return dist, False

def main():
    V, E = list(map(int, input().split()))
    
    dist = [[INF for i in range(V)] for j in range(V)]
    
    for i in range(V): dist[i][i] = 0
    
    for i in range(E):
        s, t, d = list(map(int, input().split()))
        dist[s][t] = min(dist[s][t], d)
    
    dist, negative_cycle = check_negative_cycle(V, dist)
    
    if negative_cycle: print('NEGATIVE CYCLE')
    else: 
        for i in range(V):
            for j in range(V):
                if dist[i][j] == INF: dist[i][j] = 'INF'
            print(' '.join(map(str, dist[i])))

if __name__ == '__main__':
    main()
    
