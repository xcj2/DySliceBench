def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def lcm(a, b):
    return a * b // gcd (a, b)



def mas():
    n,m = map(int,input().split())
    s = list(input())
    t = list(input())


    length = lcm(n,m)
    stepn = length//n
    stepm = length//m
    step_lcm = lcm(stepn,stepm)

    if s[0] != t[0]:
        print(-1)
        return 0
    else:
        if step_lcm >= length:
            print(length)
            return 0
        else:
            steps = step_lcm//stepn
            stept = step_lcm//stepm

            pos_s = 0
            pos_t = 0
            i = 0
            pos_s = 0
            pos_t = 0
            while pos_s < n and pos_t < m:
                if not s[pos_s] == t[pos_t]:
                    print(-1)
                    return 0
                i+=1
                pos_s = i*steps
                pos_t = i*stept
            print(length)

mas()