from sys import stdin
readline = stdin.readline
def i_input(): return int(readline().rstrip())
def i_map(): return map(int, readline().rstrip().split())
def i_list(): return list(i_map())


def main():
    N = i_input()
    x, y = i_map()
    z = x + y
    w = x - y
    z_max = z
    z_min = z
    w_max = w
    w_min = w
    for i in range(1, N):
        x, y = i_map()
        z = x + y
        w = x - y
        z_max = max(z_max, z)
        z_min = min(z_min, z)
        w_max = max(w_max, w)
        w_min = min(w_min, w)
    ans = max([z_max - z_min, w_max - w_min])
    print(ans)

if __name__ == "__main__":
    main()
