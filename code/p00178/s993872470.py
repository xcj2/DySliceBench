def v_block():
    block.insert(0, [' ']*5)
    for l, line in enumerate(block):
        if line[q-1:q+p-1] != [' ']*p:
            break
    else:
        l += 1
    block[l-1][q-1:q+p-1] = ['*']*p
    return delete()


def h_block():
    for _p in range(p):
        block.insert(0, [' ']*5)
    for l, line in enumerate(block):
        if line[q-1] == '*':
            break
    else:
        l += 1
    for _l in range(l-1, l-p-1, -1):
        block[_l][q-1] = '*'
    return delete()
                

def delete():
    b = len(block)
    l = 0
    while 0 < b:
        if block[l] == [' ']*5 or block[l] == ['*']*5:
            del block[l]
        else:
            l += 1
        b -= 1


def count():
    x = 0
    for line in block:
        for b in line:
            if b == '*':
                x += 1
    else:
        print(x)


while True:
    n = int(input())
    if n == 0:
        break
    block = [[' ']*5]
    for i in range(n):
        d, p, q = map(int, input().split())
        if d == 1:
            v_block()
        else:
            h_block()
    else:
        count()