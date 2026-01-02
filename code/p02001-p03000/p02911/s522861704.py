class ScoreBoard:
    def __init__(self, n, k):
        self.answerd = [0 for i in range(n)]
        self.init_score = k
        self.num_questions = 0

    def answer(self, i):
        ai = i - 1
        self.answerd[ai] += 1
        self.num_questions += 1

    def calc_score(self, i):
        answerd = self.answerd[i]
        return self.init_score - self.num_questions + answerd

    def isWon(self, i):
        return self.calc_score(i) > 0


def main():
    n, k, q = (int(i) for i in input().split(' '))

    score_board = ScoreBoard(n, k)

    for i in range(q):
        ai = int(input())
        score_board.answer(ai)

    for i in range(n):
        if score_board.isWon(i):
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
