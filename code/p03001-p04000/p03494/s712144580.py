from sys import stdin
readline = stdin.buffer.readline
read = stdin.buffer.read
def i_input(): return int(input().rstrip())
def i_map(): return map(int, input().rstrip().split())
def i_list(): return list(i_map())

def main():
    N = i_input()
    A = i_list()
    ans = 0
    c = True
    while c:
        for i in range(N):
            if A[i] % 2 == 0 and A[i] > 0:
                A[i] //= 2
            else:
                c = False
                break
        else:
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()
