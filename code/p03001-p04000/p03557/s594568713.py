def lower_elements(A, b):
    lower_bound = -1
    upper_bound = len(A)
    while upper_bound - lower_bound > 1:  # ア
        middle = (lower_bound + upper_bound) // 2
        if A[middle] < b:  # イ
            lower_bound = middle
        else:
            upper_bound = middle
    return lower_bound + 1  # ウ upper_boundでも可


def upper_elements(C, b):
    lower_bound = -1
    upper_bound = len(C)
    while upper_bound - lower_bound > 1:  # ア
        middle = (lower_bound + upper_bound) // 2
        if C[middle] <= b:
            lower_bound = middle
        else:
            upper_bound = middle
    return len(C) - upper_bound


def answer(N: int, A: list, B: list, C: list):
    assert N == len(A) == len(B) == len(C)
    A.sort()
    B.sort()
    C.sort()
    count = 0
    for b in B:
        count += lower_elements(A, b) * upper_elements(C, b)
    return count


def snuke_festival():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    print(answer(N, A, B, C))


if __name__ == '__main__':
  snuke_festival()