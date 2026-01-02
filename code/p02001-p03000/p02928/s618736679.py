

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def merge_sort(A):
    N = len(A)
    if N < 2:
        return A, 0
    mid = N//2
    left, left_count = merge_sort(A[:mid])
    right, right_count = merge_sort(A[mid:])
    total_count = left_count+right_count
    lowers = 0
    answer = []
    for l in left:
        while lowers < len(right) and right[lowers] < l:
            answer.append(right[lowers])
            lowers += 1
        total_count += lowers
        answer.append(l)
    while lowers < len(right):
        answer.append(right[lowers])
        lowers += 1
    return answer, total_count


def solve():
    N, K = read_ints()
    A = read_ints()
    _, left_greater = merge_sort(A)
    _, right_greater = merge_sort(A[::-1])
    modulo = 10**9+7
    return (K*(K+1)//2*left_greater+K*(K-1)//2*right_greater)%modulo


if __name__ == '__main__':
    print(solve())
