from sys import stdin
readline = stdin.readline
# read = stdin.read
def i_input(): return int(readline().rstrip())
def i_map(): return map(int, readline().rstrip().split())
def i_list(): return list(i_map())

def main():
    A, B, C, D = i_map()
    if B <= 0 and D <= 0:
        ans = A * C
    elif B < 0 and C < 0:
        ans = A * C
    elif A < 0 and D < 0:
        ans = A * C
    elif B <= 0 and C >= 0:
        ans = B * C
    elif D <= 0 and A >= 0:
        ans = A * D
    elif A * C > B * D:
        ans = A * C
    else:
        ans = B * D
    print(ans)

if __name__ == "__main__":
    main()
