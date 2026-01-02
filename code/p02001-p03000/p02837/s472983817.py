import sys
input = sys.stdin.readline


class Human:

    def __init__(self, statements):
        self.statements = statements

    def is_honest(self, honest_list):
        for x, y in self.statements:
            if y:
                if x not in honest_list:
                    return False
            else:
                if x in honest_list:
                    return False
        return True


class Humans:

    def __init__(self):
        self.humans = [None]

    def add(self, human: Human):
        self.humans.append(human)

    def is_all_honest(self, honest_list):
        for i in honest_list:
            if not self.humans[i].is_honest(honest_list):
                return False
        return True


def main():
    n = int(input())
    humans = Humans()
    for _ in range(n):
        a = int(input())
        xy = [tuple(map(int, input().split())) for _ in range(a)]
        humans.add(Human(xy))
    max_honest = 0
    for bit in range(2**n):
        honest_list = []
        for i in range(n):
            if (bit >> i) & 1:
                honest_list.append(i+1)  # 1ずれるため補正
        if humans.is_all_honest(honest_list):
            max_honest = max(max_honest, len(honest_list))
    print(max_honest)


if __name__ == "__main__":
    main()
