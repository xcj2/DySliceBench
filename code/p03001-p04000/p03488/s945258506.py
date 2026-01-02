def main():
    s = input()
    x, y = map(int, input().split())
    if solve(s, x, y):
        print('Yes')
    else:
        print('No')

def solve(s, x, y):
    moves = split_moves(s)
    if not match(x - moves[0][0], moves[0][1:]):
        return False
    if not match(y, moves[1]):
        return False

    return True

def match(x, moves):
    s = sum(moves)
    if x > s:
        return False

    if (s - x) % 2 != 0:
        return False

    return knapsack((s - x) // 2, moves)

def knapsack(x, moves):
    if x == 0:
        return True

    prev = set([0])
    for m in moves:
        curr = set(i + m for i in prev if i + m <= x)
        if x in curr:
            return True
        curr |= prev
        prev = curr
    return False

def split_moves(s):
    moves = [[0], []]
    i = 0

    for c in s:
        if c == 'F':
            moves[i][-1] += 1
        else:
            i = 1 - i
            moves[i].append(0)

    return moves

main()
