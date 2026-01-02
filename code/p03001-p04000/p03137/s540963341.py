def iread():
    return int(input())


def sread():
    return input()


def aread_int():
    tmp = input().split()
    ret = [int(i) for i in tmp]
    return ret


def aread_str():
    return input().split()

if __name__ == '__main__':
    n, m = map(int, input().split())
    
    x = aread_int()
    x = sorted(x)
    x_dist = [0] * (m - 1)
    for i in range(m - 1) :
        x_dist[i] += abs(x[i] - x[i + 1])
    
    if n > m :
        print(0)
        exit()
    
    x_dist = sorted(x_dist)
    idx = len(x_dist) - 1
    cost = sum(x_dist)
    for i in range(n - 1) :
        cost -= x_dist[idx]
        x_dist[idx] = 0
        idx -= 1

    print(cost)