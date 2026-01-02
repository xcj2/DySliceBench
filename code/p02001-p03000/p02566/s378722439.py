import sys
input = sys.stdin.readline

def SA_IS(s, upper=127):
    n = len(s)
    sa = [-1 for _ in range(n)]
    bucket = [0 for _ in range(upper + 1)]
    smaller = [True for _ in range(n)]
    is_lms = [False for _ in range(n)]
    lmss = []

    for x in s:
        bucket[x+1] += 1
    for i in range(upper):
        bucket[i+1] += bucket[i]
    
    for i in range(n-2, -1, -1):
        if s[i] > s[i+1] or (s[i] == s[i+1] and not smaller[i+1]):
            smaller[i] = False
            if smaller[i+1]:
                is_lms[i+1] = True
                lmss.append(i+1)

    count = [0 for _ in range(upper + 1)]
    for i in lmss:
        sa[bucket[s[i] + 1] - 1 - count[s[i] + 1]] = i
        count[s[i] + 1] += 1

    count = [0 for _ in range(upper + 1)]
    for i in range(n):
        if sa[i] > 0 and not smaller[sa[i] - 1]:
            sa[bucket[s[sa[i] - 1]] + count[s[sa[i] - 1] + 1]] = sa[i] - 1
            count[s[sa[i] - 1] + 1] += 1

    count = [0 for _ in range(upper + 1)]
    for i in range(n-1, -1, -1):
        if sa[i] > 0 and smaller[sa[i] - 1]:
            sa[bucket[s[sa[i] - 1] + 1] - 1 - count[s[sa[i] - 1] + 1]] = sa[i] - 1
            count[s[sa[i] - 1] + 1] += 1

    new_num = 0
    new_array = [-1 for _ in range(len(lmss))]
    lms_to_ind = dict()
    for i, x in enumerate(lmss):
        lms_to_ind[x] = len(lmss) - 1 - i
    last = sa[0]
    new_array[lms_to_ind[sa[0]]] = 0
    for i in range(1, n):
        if is_lms[sa[i]]:
            tmp, j = sa[i], 0
            while True:
                if s[last + j] != s[tmp + j]:
                    new_num += 1
                    break
                if j > 0 and (is_lms[last + j] or is_lms[tmp + j]):
                    break
                j += 1
            new_array[lms_to_ind[tmp]] = new_num
            last = tmp
            
    if new_num == len(lmss) - 1:
        seed = [-1 for _ in range(len(lmss))]
        for i, x in enumerate(new_array):
            seed[x] = i

    else:
        seed = SA_IS(new_array, upper=new_num + 1)

    new_lmss = [-1 for _ in range(len(lmss))]
    for i, x in enumerate(seed):
        new_lmss[len(lmss) - 1 - i] = lmss[len(lmss) - 1 - x]

    sa = [-1 for _ in range(n)]
    count = [0 for _ in range(upper + 1)]
    for i in new_lmss:
        sa[bucket[s[i] + 1] - 1 - count[s[i] + 1]] = i
        count[s[i] + 1] += 1

    count = [0 for _ in range(upper + 1)]
    for i in range(n):
        if sa[i] > 0 and not smaller[sa[i] - 1]:
            sa[bucket[s[sa[i] - 1]] + count[s[sa[i] - 1] + 1]] = sa[i] - 1
            count[s[sa[i] - 1] + 1] += 1

    count = [0 for _ in range(upper + 1)]
    for i in range(n-1, -1, -1):
        if sa[i] > 0 and smaller[sa[i] - 1]:
            sa[bucket[s[sa[i] - 1] + 1] - 1 - count[s[sa[i] - 1] + 1]] = sa[i] - 1
            count[s[sa[i] - 1] + 1] += 1

    return sa

def suffix_array(s):
    lis = [ord(x)-96 for x in s] + [0]
    sa = SA_IS(lis, 30)[1:]
    return sa

def lcp_array(s, sa):
    n = len(s)
    rnk = [0] * n
    for i in range(n):
        rnk[sa[i]] = i
    lcp = [0] * (n - 1)
    h = 0
    for i in range(n):
        if h > 0:
            h -= 1
        if rnk[i] == 0:
            continue
        j = sa[rnk[i] - 1]
        while j + h < n and i + h < n:
            if s[j + h] != s[i + h]:
                break
            h += 1
        lcp[rnk[i] - 1] = h
    return lcp

def main():
    s = input()[:-1]
    n = len(s)
    sa = suffix_array(s)

    lcp = lcp_array(s, sa)
    
    ans = n * (n+1) // 2 - sum(lcp)
    print(ans)

    
if __name__ == "__main__":
    main()

