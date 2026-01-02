from random import randint

def solve0(L, R):
    m = 2019
    for i in range(L, R):
        for j in range(i+1, R+1):
            t = (i*j) % 2019
            if t < m:
                m = t
                I = i
                J = j
    return I, J, m

def solve(L, R):
    M = 2019
    I = L
    mi = []
    mj = []
    for i in range(L, R+1):
        m = i % 2019 
        if m == 0:
            return 0, 0, 0
        mi.append(i)
        I = i

    for i in range(I+1, R+1):
        m = i % 2019 
        if m == 0:
            return 0, 0, 0
        mj.append(i)
    #print(mi)
    m = 2019
    for a in range(0, len(mi)):
        i = mi[a]
        for b in range(a+1, len(mi)):
            j = mi[b]
            t = (i*j)%2019 
            #print(i, j, t)
            if t < m:
                I = i
                J = j
                m = t

    return I, J, m

if 0==1:
    N = 10000
    while True:
        l = randint(0, N)
        r = randint(l+1, N)
        if solve(l,r)[-1] != solve0(l,r)[-1]:
            print("bad", l, r)
            break


def main():
    L, R =[int(x) for x in input().split()]
    answer = solve(L, R)
    #print("solve0", solve0(L, R))
    #print("solve ", answer)
    print(answer[-1])

main()

