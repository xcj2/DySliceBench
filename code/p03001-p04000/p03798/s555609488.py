import sys

def check(pos, S, index):
    N = len(S)
    right = (index + 1) % N
    left = (index + (N - 1)) % N

    if pos[index] == 0:
        if S[index] == 'o':
            return pos[left] == pos[right]
        else:
            return pos[left] != pos[right]
    else:
        if S[index] == 'o':
            return pos[left] != pos[right]
        else:
            return pos[left] == pos[right]


def make_pos(pos, S):
    """Sheep: 0, Wolf: 1"""
    N = len(S)
    for i in range(1, N-1):
        if pos[i] == 0:
            if S[i] == 'o':
                pos[i+1] = pos[i-1]
            else:
                pos[i+1] = (pos[i-1] + 1) % 2

        else:
            if S[i] == 'o':
                pos[i+1] = (pos[i-1] + 1) % 2
            else:
                pos[i+1] = pos[i-1]

    if check(pos, S, 0) and check(pos, S, N-1):
        return pos
    else:
        return False


def main():
    input = sys.stdin.readline
    N = int(input())
    S = str(input().strip())

    # Case 1: SSxxx
    pos = [-1 for _ in range(N)]
    pos[0] = 0
    pos[1] = 0
    pos = make_pos(pos, S)
    if pos:
        ans = ['S' if n == 0 else 'W' for n in pos]
        return ''.join(ans)

    # Case 2: SWxxx
    pos = [-1 for _ in range(N)]
    pos[0] = 0
    pos[1] = 1
    pos = make_pos(pos, S)
    if pos:
        ans = ['S' if n == 0 else 'W' for n in pos]
        return ''.join(ans)

    # Case 3: WSxxx
    pos = [-1 for _ in range(N)]
    pos[0] = 1
    pos[1] = 0
    pos = make_pos(pos, S)
    if pos:
        ans = ['S' if n == 0 else 'W' for n in pos]
        return ''.join(ans)

    # Case 4: WWxxx
    pos = [-1 for _ in range(N)]
    pos[0] = 1
    pos[1] = 1
    pos = make_pos(pos, S)
    if pos:
        ans = ['S' if n == 0 else 'W' for n in pos]
        return ''.join(ans)

    return -1


if __name__ == '__main__':
    print(main())
