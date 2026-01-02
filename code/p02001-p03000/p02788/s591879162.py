from collections import deque


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    """
    explosion = FIFO deque and damage, range
    """
    N, D, A = read_ints()
    XH = []
    for _ in range(N):
        XH.append(read_ints())
    XH.sort()
    explosion = deque([])
    current_damage = 0
    count = 0
    for i in range(N):
        while len(explosion) != 0 and explosion[0][1] < XH[i][0]:
            current_damage -= explosion.popleft()[0]
        if current_damage < XH[i][1]: # damage is not enough
            left_health = XH[i][1]-current_damage
            more_bombs = (left_health//A+(1 if left_health%A != 0 else 0))
            count += more_bombs
            more_damage = more_bombs*A
            current_damage += more_damage
            explosion.append((more_damage, XH[i][0]+2*D))
    return count


if __name__ == '__main__':
    print(solve())
