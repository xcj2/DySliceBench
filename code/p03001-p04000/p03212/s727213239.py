
ans = 0
def C4():
    N = int(input())
    def check(S):
        global ans
        s = 0
        f = 0
        t = 0
        #print(S)
        for j in list(S):
            if j == "7":
                s += 1
            if j == "5":
                f += 1
            if j == "3":
                t += 1
        if s != 0 and t != 0 and f != 0 and int(S) <= N:
            ans += 1

    def sarch(s):
        if int(s) <= N:
            check(s)
            sarch(s + '3')
            sarch(s + '5')
            sarch(s + '7')
    sarch("0")
    print(ans)
C4()