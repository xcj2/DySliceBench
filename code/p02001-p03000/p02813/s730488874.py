import itertools

def AllPatern(n, all):
    numbers = []
    all = []
    for i in range(n):
        numbers.append(i+1)
    for i in itertools.permutations(numbers):
        all.append(list(i))

    return all


def WhichNumber(p, q, all):
    val_p = 0
    val_q = 0
    for i in range(len(all)):
        val_p += 1
        if p == all[i]:
            break
    for i in range(len(all)):
        val_q += 1
        if q == all[i]:
            break

    return val_p, val_q

def main():
    n = int(input())
    p = [int(i) for i in input().split()]
    q = [int(i) for i in input().split()]
    all = []

    all = AllPatern(n, all)
    val_p, val_q = WhichNumber(p, q, all)
    print(abs(val_p - val_q))



if __name__ == '__main__':
    main()
