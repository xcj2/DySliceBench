def find_index(l,x,default=-1):
    return l.index(x) if x in l else default

def base_10_to_n(X, n):
    if (int(X/n)):
        return base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)


def main():
    n,A,B,C = map(int, input().split())
    l = [int(input()) for _ in range(n)]

    ans = 10**9
    for i in range(4**n):
        a = 0
        b = 0
        c = 0
        no_use = 0
        temp = 0
        status = base_10_to_n(i,4)
        status = status.zfill(n)
        status = list(map(int,list(status)))
        for j in range(n):
            if status[j] == 0:
                a += l[j]
                temp += 10
            if status[j] == 1:
                b += l[j]
                temp += 10
            if status[j] == 2:
                c += l[j]
                temp += 10
            if status[j] == 3:
                no_use += l[j]
        if a==0 or b==0 or c==0:
            continue
        temp += abs(A-a)+abs(B-b)+abs(C-c)-30
        ans = min(ans,temp)
    print(ans)


if __name__ == '__main__':
    main()
