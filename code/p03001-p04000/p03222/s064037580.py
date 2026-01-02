def f(n):
    memo = {}
    def compute(n):
        if n in memo:
            return memo[n]
        if n == 2:
            return 2
        if n <= 1:
            return 1
        ret = compute(n-1) + compute(n-2)
        memo[n] = ret
        return ret
    return compute(n)


memo = {}

def gen_patterns(c, h, w, k):
    if (c, h) in memo:
        return memo[(c,h)]
    elif h == 1:
        if c == k:
            return f(c-1) * f(w-c) % 1000000007
        elif c+1 == k:
            return f(c-1)* f(w-c-1) % 1000000007
        elif c-1 == k:
            return f(c-2)*f(w-c) % 1000000007
        else:
            return 0
    else:
        ret = 0
        ret += f(c-1) * f(w-c) * gen_patterns(c,h-1,w,k)
        ret = ret % 1000000007
        if c != 1:
            ret += f(c-2)*f(w-c)*gen_patterns(c-1,h-1,w,k)
            ret = ret % 1000000007
        if c != w:
            ret += f(c-1)*f(w-c-1)*gen_patterns(c+1,h-1,w,k)
            ret = ret % 1000000007
        memo[(c,h)] = ret
        return ret


def main():
    H, W, K = list(map(int, input().split(' ')))
    print(gen_patterns(1, H, W, K))



if __name__ == '__main__':
    main()