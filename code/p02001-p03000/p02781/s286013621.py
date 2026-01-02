def factorial(n):
    a = 1
    for i in range(1, n + 1):
        a *= i
    return a

def nCr(n,r):
    if r > n:
        return 0
    return factorial(n) // factorial(r) // factorial(n - r)

def normal(d, k):
    #print("normal d,k ", d, k)
    return nCr(d, k) * (9**k)

def main():
    tmp = input()
    N = [int(c) for c in tmp]
    D = len(N)
    K = int(input())
    #print(D, K)

    x = 0
    ans1, ans2, ans3, ans4, ans5, ans6 = 0, 0, 0, 0, 0, 0
    if K == 1:
        ans1 = normal(D-1, K)
        ans2 = N[0]
    elif K == 2:
        ans1 = normal(D-1, K)
        ans2 = (N[0] - 1) * normal(D-1, K-1)
        x = 1
        found = False
        for i in range(x, D):
            if N[i] != 0:
                x = i
                found = True
                break
        if found:
            if x == D - 1:
                ans4 = N[x]
            else:
                ans3 = normal(D-(x+1), K-1)
                ans4 = N[x]
    elif K == 3:
        ans1 = normal(D-1, K)
        ans2 = (N[0] - 1) * normal(D-1, K-1)
        x = 1
        found = False
        for i in range(x, D):
            if N[i] != 0:
                x = i
                found = True
                break
        if found:
            if x == D - 1:
                pass
            else:
                ans3 = normal(D-(x+1), K-1)
                ans4 = (N[x] - 1) * normal(D-(x+1), K-2)
                x = x + 1
                found = False
                for i in range(x, D):
                    if N[i] != 0:
                        x = i
                        found = True
                        break
                if found:
                    if x == D - 1:
                        ans6 = N[x]
                    else:
                        ans5 = normal(D-(x+1), K-2)
                        ans6 = N[x]

    #print("ans1", ans1)
    #print("ans2", ans2)
    #print("ans3", ans3)
    #print("ans4", ans4)
    #print("ans5", ans5)
    #print("ans6", ans6)

    ans = ans1+ans2+ans3+ans4+ans5+ans6
    #print("ans", ans)
    print(ans)

main()