N, M = [int(n) for n in input().split()]
A = [list(input()) for _ in range(N)]
B = [list(input()) for _ in range(M)]

def create_coords(x, y, l):
    return [(_x, _y) for _x in range(x, x + l) 
                     for _y in range(y, y + l)]

def concat(li, coords):
    return ''.join(map(lambda c: li[c[0]][c[1]], coords))

def main():
    ans = 'No'
    r = range(N - M + 1)
    l = M
    b = concat(B, create_coords(0, 0, l))
    for x in r:
        for y in r:
            a = concat(A, create_coords(x, y, l))
            if a == b:
                ans = 'Yes'
                break
    print(ans)

if __name__ == '__main__':
    main()