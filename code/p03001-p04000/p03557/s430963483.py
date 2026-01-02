import bisect

def find_lt(a, x):
    i = bisect.bisect_left(a, x)
    if i:
        return i
    return 0

def find_l(a, x):
    i = bisect.bisect_right(a, x)
    if i == 0:
        return len(a)
    else:
        return len(a) - i

def main():
    N = int(input())

    partA = list(map(int, input().split()))
    partA.sort()
    partB = list(map(int, input().split()))
    partB.sort()
    partC = list(map(int, input().split()))
    partC.sort()
    cnt = 0


    for b in partB:
        A = find_lt(partA, b)
        #print (A)
        B = find_l(partC, b)
        #print (B)
        cnt += (A * B)

    print(cnt)

if __name__ == '__main__':
    main()