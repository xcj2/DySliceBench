def A():
    ab, bc, ca = map(int, input().split())
    print(int(bc * ab / 2))
#A()

def B():
    s = int(input())
    f_data = [s]
    i = 1
    a = [s]
    tmp = [0 for i in range(1000000)]
    def f(n):
        if n % 2 == 0:
            return n // 2
        else:
            return 3 * n + 1

    while True:
        key = f(f_data[-1])
        f_data.append(key)
        if tmp[key] == 1:
            ans = i + 1
            break
        tmp[key] = 1
        i += 1
    print(ans)
#B()

def C():
    N = int(input())
    cnt = 0
    h = list(map(int, input().split()))
    while sum(h) != 0:
        cnt += 1
        for i in range(N):
            if h[i] > 0:
                #print(i)
                for j in range(i, N):
                    #print(i, j)
                    if h[j] == 0:
                        break
                    else:
                        h[j] -= 1
                #print(h, cnt)
                break
    print(cnt)
C()