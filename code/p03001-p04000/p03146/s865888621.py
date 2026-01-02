def A():
    ab, bc, ca = map(int, input().split())
    print(int(bc * ab / 2))
#A()

def B():
    s = int(input())
    f_data = [s]
    i = 0
    tmp = [0 for i in range(1000001)]
    def f(n):
        if n % 2 == 0:
            return n // 2
        else:
            return 3 * n + 1
    ans = 0
    while True:
        if i == 0:
            f_data.append(s)
            tmp[s] = 1
        else:
            key = f(f_data[-1])
            f_data.append(key)
            if tmp[key] == 1:
                ans = i + 1
                break
            tmp[key] = 1
            
        if ans != 0:
            break
        i += 1
    #print(f_data)
    print(ans)
B()

