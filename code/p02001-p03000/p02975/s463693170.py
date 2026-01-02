import itertools
N = int(input())
a = list(map(int, input().split()))

def all_zero(a):
    for e in a:
        if e != 0:
            return False
    return True

def three_mod_same(a):
    counts = {}
    for e in a:
        if e not in counts:
            counts[e] = 1
        else:
            counts[e] += 1

    for v in counts.values():
        if v != len(a) // 3:
            return False
    return True

def two_elem_one_zero(a):
    if len(set(a)) != 2:
        return False
    counts = {}
    for e in a:
        if e not in counts:
            counts[e] = 1
        else:
            counts[e] += 1
            
    for key, v in counts.items():
        if key == 0:
            if v != len(a) // 3:
                return False
        else:
            if v != (len(a) // 3) * 2:
                return False
    return True

if len(set(a)) != 3:
    if all_zero(a) or ((len(a) % 3 == 0) and two_elem_one_zero(a)):
        print("Yes")
    else:
        print("No")
else:
    p = itertools.permutations(list(set(a)), 3)
    yes = False
    for permed_a in p:            
        good_perm = True
        for i in range(3):
            if permed_a[(i + 1) % 3] != (permed_a[i] ^ permed_a[(i + 2) % 3]):
                good_perm = False
                break
        if good_perm:
            yes = True
            break
    if not yes:
        print("No")
    else:
        if three_mod_same(a):
            print("Yes")
        else:
            print("No")