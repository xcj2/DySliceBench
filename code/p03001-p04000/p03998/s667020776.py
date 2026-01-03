from sys import stdin


def fetch_one_line():
    return stdin.readline().rstrip()


def fetch_int_input():
    return [int(s) for s in fetch_one_line().split()]


def fetch_inputs(times):
    return [fetch_one_line() for _ in range(times)]

def fetch_int_inputs(times):
    return [[int(s) for s in fetch_one_line()] for _ in range(times)]

def fetch_ints_inputs(times):
    return [fetch_int_input() for _ in range(times)]


cards = fetch_inputs(3)
cards = {
            "a": cards[0],
            "b": cards[1],
            "c": cards[2]
        }

turn = "a"

while True:
    if cards[turn]:
        tmp_turn = cards[turn][0]
        cards[turn] = cards[turn][1:]
        turn = tmp_turn
    else:
        winner = turn
        break

print(winner.upper())
