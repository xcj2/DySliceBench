def saiki(bang, abbali, tf):

    ans = 0
    if all(tf) == True:
        return 1
    stack = []
    for i in range(len(abbali)):
        if abbali[i][0] == bang and tf[abbali[i][1]-1] == False:
            stack.append(abbali[i][1])

    for i in range(len(stack)):
        tf[stack[i]-1] = True
        ans += saiki(stack[i], abbali, tf)
    return ans

def bridge(n , m , abl):

    ans = 0
    for i in range(m):
        abbali = []
        count = 0
        tf = [False]*n
        for q in range(m):
            if i != q:
                abbali.append(list((abl[q])))
                abbali.append(list(reversed(abl[q])))
        count = saiki(1, abbali, tf)
        ans += count if count < 1 else 1

    return m - ans

def main():
    n , m = map(int , input().split())
    abl = [list(map(int , input().split())) for i in range(m)]
    print(bridge(n , m , abl))

if __name__ == '__main__':
    main()
