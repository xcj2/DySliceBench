import time
import random


class Problem:

    def __init__(self, D, s, c):
        self.last_days = [0] * 26
        self.D = D
        self.s = s
        self.c = c
        self.answer = [0] * self.D
        self.best_answer = [0] * self.D
        self.best_score = 0
        self.days = [0] * self.D
        self.best_answer_scores = [0] * self.D

    def scoring(self, day, ind):
        day_score = self.s[day][ind]
        minus_score = 0
        for i in range(26):
            if i != ind:
                minus_score += self.c[i] * (day + 1 - self.last_days[i])
        day_score -= minus_score
        return day_score

    def get_all_scores(self, day):
        """全ての選択肢のscoreを返す"""
        minus_score = 0
        all_scores = [0] * 26
        for i in range(26):
            if i == 0:
                for j in range(1, 26):
                    minus_score += self.c[j] * (day + 1 - self.last_days[j])
                all_scores[0] = self.s[day][0] - minus_score

            else:
                minus_score += self.c[i - 1] * (day + 1 - self.last_days[i - 1])
                minus_score -= self.c[i] * (day + 1 - self.last_days[i])
                all_scores[i] = self.s[day][i] - minus_score
        return all_scores

    def _strategy_greedy(self, day):
        score = self.scoring(day, self.days[day])
        return score, self.days[day]

    def solve(self):
        self.init()

        sum_score = 0
        scores = []
        for i in range(self.D):
            score, ind = self._strategy_greedy(i)
            self.last_days[ind] = i + 1
            self.answer[i] = ind
            sum_score += score
            scores.append(sum_score)
        return sum_score, self.answer, scores

    def _strategy_perturbation(self):
        # ランダムに１日を取り出し、一番その日の期待コストが大きくなるよう変化させる
        # 貪欲法に摂動を加えてみる
        day = random.randint(0, 3)

        # scores = [self.scoring()]

        random.randint(0, 3)

    def solve_greed(self):
        self.init()

    def init(self):
        self.last_days = [0] * 26
        self.answer = [0] * self.D


def main():
    D = int(input())
    c = list(map(int, input().split()))
    s = []
    for _ in range(D):
        s.append(list(map(int, input().split())))
    days = []
    for _ in range(D):
        days.append(int(input()) - 1)

    max_score = 0

    problem = Problem(D, s, c)
    problem.days = days
    score, answer,scores = problem.solve()

    for i in range(D):
        # problem.best_answer[i] += 1
        # print(problem.best_answer[i])
        print(scores[i])
    # print(ite)
    # print(max_answer)
    # print(max_score)
    # print(problem.get_all_scores(1))


main()
