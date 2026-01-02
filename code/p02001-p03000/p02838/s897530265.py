import sys

inf = float("inf")

def get_array(): return list(map(int, sys.stdin.readline().strip().split()))
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def input(): return sys.stdin.readline().strip()

mod = 10**9+7

def sumXOR(arr, n):
    sum = 0
    for i in range(0, 64):

        #  Count of zeros and ones
        zc = 0
        oc = 0

        # Individual sum at each bit position
        idsum = 0
        for j in range(0, n):
            if (arr[j] % 2 == 0):
                zc = zc + 1

            else:
                oc = oc + 1
            arr[j] = arr[j]//2

            # calculating individual bit sum
        idsum = oc * zc * (1 << i)

        # final sum
        sum = sum + idsum
        sum%=mod

    return sum

n = int(input())
Arr = get_array()
ans = sumXOR(Arr,n)
ans %= mod
print(ans)