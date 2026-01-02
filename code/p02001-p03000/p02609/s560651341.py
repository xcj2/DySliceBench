def find(x,ones):
    if ones == 0:
        return 0
    total = 0
    n = len(x)
    for i in range(n):
        total += int(x[i])*pow(2,n-i-1,ones)
        total %= ones

    return total

def solve(x,mod):
    x %= mod
    moves = 1
    while x != 0:
        x = x%(bin(x)[2:].count('1'))
        moves += 1

    return moves

def main():
    n = int(input())
    x = input()
    ones = x.count('1')
    less = find(x,ones-1)
    more = find(x,ones+1)
    for i in range(n):
        if x[i] == '0':
            print(solve(more+pow(2,n-i-1,ones+1),ones+1))
        else:
            if ones-1 == 0:
                print(0)
            else:
                print(solve(less-pow(2,n-i-1,ones-1),ones-1))


main()
