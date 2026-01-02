
def make_hikaku(num, n):
    org = num
    retval = []
    for i in range(n):
        retval.append(org)
        if org == 0:
            org = 1
        elif org == 1:
            org = 0
    return retval

def hikaku(a, b):
    if a == b:
        return 0
    else:
        return 1
    

def main(s):
    n = len(s)
    hikaku_a = make_hikaku(0, n)
    hikaku_b = make_hikaku(1, n)
    s_bit = 0
    s_l = list(map(int, list(s)))
    s_a = []
    s_b = []
    for i in range(n):
        s_a.append(hikaku(s_l[i], hikaku_a[i]))
        s_b.append(hikaku(s_l[i], hikaku_b[i]))
    
    print(min(sum(s_a), sum(s_b)))
    
if __name__ == '__main__':
    try:
        s = input().strip()
        main(s)
    except EOFError:
        pass
