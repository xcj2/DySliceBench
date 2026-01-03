a = list(map(int, input().split()))
b = a[:]
c = a[:]

def aa(a):
    total = a[1]
    i6 = min(a[0],a[3],a[4])
    a[0] -= i6
    a[3] -= i6
    a[4] -= i6
    total += i6 * 3
    total += a[0]//2*2
    total += a[3]//2 *2
    total += a[4]//2 *2
    return total

def bb(a):
    total = a[1]
    if a[0] > 0 and a[3]%2 ==  a[4]%2 == 1:
        a[0] -= 1
        a[3] -= 1
        a[4] -= 1
        total += 3
    total += a[0]//2 * 2
    total += a[3]//2 * 2
    total += a[4]//2 * 2
    return total

def cc(a):
    total = a[1]
    if (a[0]%2 == a[3]%2 == 1 and a[4]>0) or (a[0]%2 == a[4]%2 == 1 and a[3]>0) or(a[4]%2 == a[3]%2 == 1 and a[0]>0):
        total += 3
        a[0] -= 1
        a[3] -= 1
        a[4] -= 1
    total += a[0]//2 * 2
    total += a[3]//2 * 2
    total += a[4]//2 * 2
    if a[0]%2 == a[3]%2 ==  a[4]%2 == 1:
        a[0] -= 1
        a[3] -= 1
        a[4] -= 1
        total += 3
    return total
print(max(aa(a),bb(b), cc(c)))