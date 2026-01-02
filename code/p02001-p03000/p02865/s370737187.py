import heapq
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))

def main():
    n = getN()
    ans = 0
    for i in range(1, n//2+1):
        if (n-i) != i and (n-1) > 0:
            ans += 1

    print(ans)

    return

if __name__ == "__main__":
    main()

"""
10
203941992 742164984
670850202 743524472
687298546 744891559
676493045 744182895
385467254 742631752
740505911 744926772
425723256 743348462
225362543 742332848
399450535 742706299
563528474 743419738
"""