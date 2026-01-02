import math
import sys


def insertionSort(data, N, g, cnt):
    
    for i in range(g, N):
        v = data[i]
        j = i - g
        while j >= 0 and data[j] > v:
            data[j+g] = data[j]
            j = j - g
            cnt += 1
        data[j+g] = v
        
    return data, cnt


def shellSort(data, N, G, cnt):
    
    h = 1
    while (True):
        if h > N:
            break
        G.append(h)
        h = 3 * h + 1
    
    m = len(G)
    G.reverse()
    

    for i in range(m):
        data, cnt = insertionSort(data, N, G[i], cnt)
        
    return m, G, cnt


def main():
    N = int(input())
    data = [int(input()) for _ in range(N)]
    
    cnt = 0
    G = []
    m = 0
    
    m, G, cnt = shellSort(data, N, G, cnt)
    
    print(m)
    print(' '.join(map(str, G)))
    print(cnt)
    for i in range(N):
        print(data[i])
    
if __name__ == '__main__':
    main()
