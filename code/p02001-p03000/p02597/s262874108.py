

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N = read_int()
    C = list(input())
    Rs = []
    for i in range(N):
        if C[i] == 'R':
            Rs.append(i)
    count = 0
    for i in range(N):
        if C[i] == 'W':
            if len(Rs) == 0:
                break
            j = Rs.pop()
            if i < j:
                C[i], C[j] = C[j], C[i]
                count += 1
    return count


if __name__ == '__main__':
    print(solve())
