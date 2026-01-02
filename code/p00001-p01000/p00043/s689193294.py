from itertools import combinations_with_replacement, combinations

def gen_dict(nums):
    r = {}
    for i in nums:
        if i in r.keys():
            r[i] += 1
        else:
            r[i] = 1
    return r

def has_more_4(num_dict):
    for i in num_dict.values():
        if i > 4: return True
    return False

def gen_conseq3(nums):
    r = []
    for i in range(1, 8):
        for j in range(i, i+3):
            if j not in nums: break
        else:
            r.append((i, i+1, i+2))
    return r

def gen_same(n, num_dict):
    r = []
    for i, v in num_dict.items():
        if v >= n: r.append(i)
    return r

def gen_prec(c1s, c2s, c3):
    r = []
    for i in c1s:
        for j in i:
            r.append(j)
    for i in c2s:
        for j in range(3): r.append(i)
    for j in range(2):
        r.append(c3)
    return sorted(r)

while True:
    try: line = input()
    except EOFError: break
    
    founds = []
    for i in range(1, 10):
        ln = line + str(i)
        nums = sorted(list(map(int, ln[:])))
        num_dict = gen_dict(nums)
        if has_more_4(num_dict):
            continue
        conseq_3s = gen_conseq3(nums)
        same_3s = gen_same(3, num_dict)
        same_2s = gen_same(2, num_dict)
        was_found = False
        for r in range(1, 5):
            if was_found: break
            for c1s in combinations_with_replacement(conseq_3s, r):
                if was_found: break
                for c2s in combinations(same_3s, 4-r):
                    if was_found: break
                    for c3 in same_2s:
                        pred = gen_prec(c1s, c2s, c3)
                        if pred == nums:
                            founds.append(str(i))
                            was_found = True
    if founds:
        print(' '.join(founds))
    else:
        print(0)

