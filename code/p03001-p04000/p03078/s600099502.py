

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    X, Y, Z, K = read_ints()
    A = read_ints()
    B = read_ints()
    C = read_ints()
    BC = [b+c for b in B for c in C]
    BC.sort(reverse=True)
    A.sort(reverse=True)
    low, high = 2, max(A)+max(BC)+1
    while high-low > 1:
        min_deliciousness = low+(high-low)//2
        count_k = 0
        i = len(BC)-1
        for a in A:
            while i > -1 and a+BC[i] < min_deliciousness:
                i -= 1
            count_k += (i+1)
        if count_k > K:
            low = min_deliciousness
        else:
            high = min_deliciousness
    answer = []
    for a in A:
        for bc in BC:
            if a+bc < low:
                break
            else:
                answer.append(a+bc)
    answer.sort(reverse=True)
    for a in answer[:K]:
        print(a)


if __name__ == '__main__':
    solve()
