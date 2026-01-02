from sys import stdin
readline = stdin.buffer.readline
def r_map(): return map(int, readline().rstrip().split())
def r_list(): return list(r_map())

def main():
    N = int(readline().rstrip())
    A = r_list()
    M = max(A)
    d = [0] * (M + 1)
    g = True
    for a in A:
        d[a] += 1
    for i in range(2, M + 1):
        c = sum(d[i::i])
        if c == N:
            print("not coprime")
            exit()
        elif c > 1:
            g = False
    if g:
        print('pairwise coprime')
    else:
        print('setwise coprime')

if __name__ == "__main__":
    main()
