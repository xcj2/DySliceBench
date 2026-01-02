#coding=utf-8

def check_circle(s):
    x = str(s)
    flag = True
    for i in range(int(len(x) / 2)):
         if x[i] != x[-1 * (i + 1)]:
              flag = False
    return flag

def solve(N, M):
    return abs((N - 2) * (M - 2))
    if N == 1:
        return N * M - 2
    if M == 1:
        return N * M - 2
    return N * M - 4
    if N == M and N == 1:
        return 1
    if N == M and N == 0:
        return 0

    if N >= 2:
        tate = 2 * (M - 2)
    elif N == 1:
        tate = M - 2
    if M >= 2:
        yoko = 2 * (N - 2)
    elif M == 1:
        yoko == M - 2
    else:
        yoko = N - 2
    ans = tate + yoko
    return ans

def main():
    N, M = input().split(' ')
    print(solve(int(N), int(M)))


if __name__ == '__main__':
    main()

