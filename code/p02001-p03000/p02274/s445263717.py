import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
cnt = 0
inf = float('inf')

def merge_sort(left, right):
    if right-left > 1:
        middle = (left+right) // 2
        merge_sort(left, middle)
        merge_sort(middle, right)
        merge(left, middle, right)

def merge(left, middle, right):
    left_part = A[left:middle]
    right_part = A[middle:right]
    left_part.append(inf)
    right_part.append(inf)
    l, r = 0, 0
    global cnt
    left_size = middle-left
    for i in range(left, right):
        if left_part[l] < right_part[r]:
            A[i] = left_part[l]
            l += 1
        else:
            A[i] = right_part[r]
            cnt += max(left_size-l, 0)
            r += 1

def main():
    merge_sort(0, n)
    print(cnt)

if __name__ == "__main__":
    main()
