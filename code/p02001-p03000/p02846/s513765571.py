def solve():
    maxCycle = 10**20

    T1, T2 = map(int, input().split())
    A1, A2 = map(int, input().split())
    B1, B2 = map(int, input().split())

    C1, C2 = B1-A1, B2-A2
    if C1 > 0:
        C1, C2 = -C1, -C2

    dist = C1*T1 + C2*T2

    def binarySearch(isOK):
        ng, ok = -1, maxCycle
        while abs(ok-ng) > 1:
            mid = (ng+ok) // 2
            if isOK(mid):
                ok = mid
            else:
                ng = mid
        return ok

    def isOK1(c):
        return dist*(c+1) >= 0
    cycle1 = binarySearch(isOK1)
    if cycle1 == maxCycle:
        return 0

    def isOK2(c):
        return dist*c > 0
    cycle2 = binarySearch(isOK2)
    if cycle2 == maxCycle:
        return 'infinity'

    def isOK3(c):
        return dist*c + C1*T1 >= 0
    cycle3 = binarySearch(isOK3)

    def isOK4(c):
        return dist*c + C1*T1 > 0
    cycle4 = binarySearch(isOK4)

    ans = 1*(cycle2-cycle1) + 2*(cycle3-cycle2) + 1*(cycle4-cycle3)
    return ans


print(solve())
