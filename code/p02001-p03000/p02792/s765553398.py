def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

def main():
    N = Z()
    maxl = len(str(N))
    output = 0
    for n in range(1, N+1):
        if n%10 == 0: continue
        s = str(n)
        if s[0] == s[-1]:
            for j in range(1, maxl+1):
                if j == 1:
                    output += 1
                    continue
                if j == 2:
                    if 10*int(s[-1]) + int(s[0]) <= N:
                        output += 1
                    continue
                if j < maxl:
                    output += 10 ** (j-2)
                    continue
                #when j == maxl
                if int(s[-1]) < int(str(N)[0]):
                    output += 10 ** max(0, j-2)
                elif s[-1] == str(N)[0]:
                    output += int(str(N)[1:maxl-1]) + 1
                    if int(s[0]) > int(str(N)[-1]): output -= 1
        else:
            for j in range(2, maxl+1):
                if j < maxl:
                    output += 10 ** (j-2)
                    continue
                # when j == maxl
                if int(s[-1]) < int(str(N)[0]):
                    output += 10 ** (j-2)
                if s[-1] == str(N)[0]:
                    if j == 2:
                        if 10*int(s[-1]) + int(s[0]) <= N:
                            output += 1
                    else:
                        output += int(str(N)[1:maxl-1]) + 1
                        if int(s[0]) > int(str(N)[-1]): output -= 1
    print(output)
    return

if __name__ == '__main__':
    main()

