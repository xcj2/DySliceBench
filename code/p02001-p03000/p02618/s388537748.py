import time
import copy
import random


class Answer:
    """

    """

    def __init__(self, answer, score):
        self.answer = copy.deepcopy(answer)
        self.score = copy.deepcopy(score)
        self.last_days = [0] * 26


class Problem:
    def __init__(self, num_day, s, c):
        self.d = num_day
        self.s = s
        self.c = c
        self.last_days = [0] * 26
        self.answer = Answer([0] * self.d, 0)
        self.best_answer = Answer([0] * self.d, 0)
        self.not_change_duration = 1000

        self.solve_greedy()
        self._update_best()
        self.answer.score = 0

    def scoring(self, day, ind) -> int:
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
                    minus_score += self.c[j] * (day + 1 - self.answer.last_days[j])
                all_scores[0] = self.s[day][0] - minus_score

            else:
                minus_score += self.c[i - 1] * (day + 1 - self.answer.last_days[i - 1])
                minus_score -= self.c[i] * (day + 1 - self.answer.last_days[i])
                all_scores[i] = self.s[day][i] - minus_score
        return all_scores

    def repeat(self):
        self.initialize()
        self.solve()
        self._update_best()

        return copy.deepcopy(self.best_answer)

    def solve(self):
        self.initialize()

        change_day = set([random.randint(0, self.d - 1) for _ in range(10)])
        for day in range(self.d):
            if day in change_day:
                pert = random.randint(1, 10)
            else:
                pert = 1
            all_scores = self.get_all_scores(day)
            all_scores_with_ind = [[i, all_scores[i]] for i in range(26)]
            all_scores_with_ind.sort(key=lambda x: x[1])
            ind = all_scores_with_ind[-pert][0]
            score = self.scoring(day, ind)
            self.answer.last_days[ind] = day + 1
            self.answer.answer[day] = ind
            self.answer.score += score
            # print(self.answer.answer)

    def score_answer(self, answer: Answer):
        score = 0
        answer.last_days = [0] * 26
        for day in range(self.d):
            score += self.scoring(day, answer.answer[day])
            answer.last_days[answer.answer[day]] = day + 1

        return score

    def solve_greedy(self):
        for day in range(self.d):
            all_scores = self.get_all_scores(day)
            all_scores_with_ind = [[i, all_scores[i]] for i in range(26)]
            all_scores_with_ind.sort(key=lambda x: x[1])
            ind = all_scores_with_ind[-1][0]
            score = self.scoring(day, ind)
            self.answer.last_days[ind] = day + 1
            self.answer.answer[day] = ind
            self.answer.score += score

    def _update_best(self):
        self.not_change_duration += 1
        # print(self.best_answer.score , self.answer.score)
        if self.best_answer.score < self.answer.score:
            # print("fgooo")
            # print(self.answer.answer)
            self.best_answer = copy.deepcopy(self.answer)
        if self.not_change_duration > 10:
            # print("hooo")
            self.answer = copy.deepcopy(self.best_answer)
            self.not_change_duration = 0

    def initialize(self):
        # self.answer = copy.deepcopy(self.best_answer)
        self.answer.last_days = [0] * 26
        self.answer.score = 0


def main():
    time_start = time.time()
    limited_time = 2 * 0.90
    D = int(input())
    c = list(map(int, input().split()))
    s = []

    for _ in range(D):
        s.append(list(map(int, input().split())))

    problem = Problem(D, s, c)
    while time.time() - time_start < limited_time:
        problem.repeat()

    # print(problem.best_answer.score)
    for i in range(D):
        print(problem.best_answer.answer[i] + 1)


main()
