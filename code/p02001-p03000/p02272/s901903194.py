import math
import sys

def merge(nums, left, mid, right):
    sentiel = sys.maxsize

    lefts = [nums[left+i] for i in range(mid - left)]
    lefts.append(sentiel)

    rights = [nums[mid+i] for i in range(right - mid)]
    rights.append(sentiel)

    l = 0
    r = 0
    cnt = 0

    for k in range(left, right):
        if lefts[l] <= rights[r]:
            nums[k] = lefts[l]
            l += 1
        else:
            nums[k] = rights[r]
            r += 1
        cnt += 1

    return nums, cnt

def mergeSort(nums, left, right):
    if right - left <= 1:
        return nums, 0

    mid = left + math.ceil((right - left)/2)

    nums, cntl = mergeSort(nums, left, mid)
    nums, cntr = mergeSort(nums, mid, right)

    nums, cnt  = merge(nums, left, mid, right)

    return nums, cnt+cntl+cntr

def main():
    n = int(input())
    nums = [int(x) for x in input().split(' ')]

    snums, cnt = mergeSort(nums, 0, n)

    print(' '.join([str(x) for x in snums]), cnt, sep="\n")

if __name__ == '__main__':
    main()

