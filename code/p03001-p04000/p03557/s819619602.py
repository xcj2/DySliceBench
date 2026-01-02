def binarySearchLeft(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = low + high >> 1
        if target == nums[mid]:
            if mid == 0 or target != nums[mid - 1]:
                return mid
            else:
                high = mid - 1
        elif target < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return low

def binarySearchRight(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = low + high >> 1
        if target == nums[mid]:
            if mid == len(nums) - 1 or target != nums[mid + 1]:
                return mid
            else:
                low = mid + 1
        elif target < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return high

def solve(N, A, B, C):
     A.sort()
     B.sort()
     C.sort()
     ret = 0
     for j in range(N):
         i = binarySearchRight(A, B[j] - 1)
         k = binarySearchLeft(C, B[j] + 1)
         ret += (i + 1) * (N - k) if 0 <= i < N and 0 <= k < N else 0
     print(ret)

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    solve(N, A, B, C)
