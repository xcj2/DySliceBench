def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
from collections import Counter
# import math
MOD = 998244353

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def main():
    n = getN()
    nums = getList()
    cnt = Counter(nums)
    items = sorted(cnt.items(), key=lambda x: x[0])
    # print(items)
    if nums[0] != 0:
        print(0)
        return

    ans = 1
    prev = 1
    for i, item in enumerate(items):
        if i != item[0]:
            print(0)
            return
        if item[0] == 0 and item[1] != 1:
            print(0)
            return
        else:
            # a,b = max(item[1], prev), min(item[1], prev)
            ans *= (prev**item[1])
            prev = item[1]
            ans %= MOD


    print(ans)
if __name__ == "__main__":
    main()