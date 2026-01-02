import collections

def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

def main():
    N = Z()

    def bunkai(num):
        i = 2
        ret = []
        a = num
        while i*i <= num:
            c = 0
            while a%i == 0:
                a //= i
                c += 1
            if c > 0: ret.append([i, c])
            i += 1
        if a != 1: ret.append([a, 1])
        return ret

    pl = bunkai(N)
    output = 0
    for i in range(len(pl)):
        _, c = pl[i]
        j = 1
        while c >= j:
            c -= j
            j += 1
            output += 1
    print(output)

    return

if __name__ == '__main__':
    main()
