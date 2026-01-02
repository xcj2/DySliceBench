import sys, math
input = sys.stdin.readline

MAX = 2e9

def merge(A, left, mid, right):
    n1 = mid - left
    n2 = right - mid
    L = A[left:mid]
    L.append(MAX)
    R = A[mid:right]
    R.append(MAX)
    merged = []
    index_L = 0
    index_R = 0
    comp_cnt = 0
    for _ in range(n1+n2):
        cand_L = L[index_L]
        cand_R = R[index_R]
        comp_cnt += 1
        if (cand_L < cand_R):
            merged.append(cand_L)
            index_L += 1
        else:
            merged.append(cand_R)
            index_R += 1
    A[left:right] = merged
    return comp_cnt
        
def merge_sort(A, left, right):
    comp_cnt = 0
    if (left + 1 < right):
        # Devide
        mid = (left + right) // 2
        # Solve
        _, cnt = merge_sort(A, left, mid)
        comp_cnt += cnt
        _, cnt = merge_sort(A, mid, right)
        comp_cnt += cnt
        # Conquer
        comp_cnt += merge(A, left, mid, right)
    return A, comp_cnt

def main():
    N = int(input())
    S = list(map(int, input().split()))
    left = 0
    right = len(S)
    merged, cnt = merge_sort(S, left, right)
    print(" ".join([str(x) for x in merged]))
    print(cnt)

if __name__ == "__main__":
    main()
