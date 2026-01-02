import sys
def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

def main():
    N = Z()
    output = 0
    x = y = z = 0
    for _ in range(N):
        s = sys.stdin.readline().rstrip()
        output += s.count('AB')
        if s[0] == 'B' and s[-1] == 'A': y += 1
        elif s[-1] == 'A': x += 1
        elif s[0] == 'B': z += 1
        
    if y == 0:
        output += min(x, z)
        print(output)
        return

    if x > 0:
        output += y + min(1, z) + max(min(x-1, z-1), 0)
        print(output)
        return

    output += y - 1 + min(1, z)
    print(output)

    return

if __name__ == '__main__':
    main()
