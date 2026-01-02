def find_index(l, x):
    return l.index(x) if x in l else -1

def water(sum, H):
    if len(H)==0:
        return sum
    elif len(H)==1:
        sum += H[0]
        return sum
    minimum = min(H)
    sum += minimum
    for i in range(len(H)):
        H[i] -= minimum
    index = find_index(H, 0)
    H1 = H[:index]
    sum = water(sum,H1)
    H2 = H[index+1:]
    sum = water(sum,H2)
    return sum


    water(sum, array)

def main():
    n = int(input())
    H = list(map(int, input().split()))
    sum = 0
    sum += water(sum, H)
    print(sum)


if __name__ == '__main__':
    main()
