

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N = read_int()
    L = read_ints()
    L.sort()
    answer = 0
    for i in range(2, N):
        for j in range(1, i):
            start, end = -1, j
            while end-start > 1:
                mid = start+(end-start)//2
                if L[i]-L[j] < L[mid]: # valid
                    end = mid
                else:
                    start = mid
            answer += j-end
    return answer


if __name__ == '__main__':
    print(solve())
