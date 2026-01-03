import sys
## io ##
def IS(): return sys.stdin.readline().rstrip()
def II(): return int(IS())
def MII(): return list(map(int, IS().split()))
from enum import Enum
#======================================================#
class State(Enum):
    UP = 1
    DOWN = 2
    HORI = 3

def main():
    n = II()
    prev, *aa = MII()
    state = State.HORI
    cnt = 1
    for a in aa:
        if prev < a:
            if state == State.HORI:
                state = State.UP
            elif state == State.DOWN:
                cnt += 1
                state = State.HORI
        elif prev > a:
            if state == State.HORI:
                state = State.DOWN
            elif state == State.UP:
                cnt += 1
                state = State.HORI
        prev = a
    print(cnt)

if __name__ == '__main__':
    main()