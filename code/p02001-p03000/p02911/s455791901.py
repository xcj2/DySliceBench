

class Quiz(object):
    def __init__(self, n, k, answers):
        self._n = n
        self._k = k
        self._answers = answers

    def _solve(self):
        points = [0 for _ in range(self._n)]

        for a in self._answers:
            points[a - 1] = points[a - 1] + 1

        return points

    def get_answers(self):
        points = self._solve()
        q = len(self._answers)
        return ['Yes' if self._k - q + p > 0 else 'No' for p in points]


def main():
    conditions = input()
    c = conditions.split(' ')

    n = int(c[0])
    k = int(c[1])
    q = int(c[2])

    answers = []
    for i in range(q):
        answers.append(int(input().strip()))

    p = Quiz(n, k, answers)
    print('\n'.join(p.get_answers()))


if __name__ == '__main__':
    main()
