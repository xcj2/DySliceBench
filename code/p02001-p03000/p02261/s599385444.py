from typing import List


def get_value(card: str) -> int:
    return card[1]


def bublle_sort(C: List[str]) -> None:
    for i in range(len(C)):
        for j in reversed(range(i + 1, len(C))):
            if get_value(C[j]) < get_value(C[j - 1]):
                C[j], C[j - 1] = C[j - 1], C[j]


def selection_sort(C: List[str]) -> None:
    for i in range(len(C)):
        min_j = i
        for j in range(i, len(C)):
            if get_value(C[j]) < get_value(C[min_j]):
                min_j = j
        C[i], C[min_j] = C[min_j], C[i]


def is_stable(A_in, A_out) -> bool:
    for i in range(len(A_in)):
        for j in range(i + 1, len(A_in)):
            for a in range(len(A_out)):
                for b in range(a + 1, len(A_out)):
                    if get_value(A_in[i]) == get_value(A_in[j]) and A_in[i] == A_out[b] and A_in[j] == A_out[a]:
                        return False
    return True


N = int(input())
C = [str(i) for i in input().split()]
C1 = [i for i in C]
C2 = [i for i in C]

bublle_sort(C1)
print(' '.join(C1))
if is_stable(C, C1):
    print('Stable')
else:
    print('Not stable')

selection_sort(C2)
print(' '.join(C2))
if is_stable(C, C2):
    print('Stable')
else:
    print('Not stable')

