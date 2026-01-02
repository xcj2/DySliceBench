# -*- coding; utf 8 -*-
# Guidebook
# 2019. 5/28
# 市名をアルファベット順
# 同じ市内なら点数が高い順
# 出力は与えられた番号 (1 origin)


class Guidebook(object):
    def __init__(self, num, city, score):
        self.num = num
        self.city = city
        self.score = score


def print_number(N, guidebook):
    for i in range(N):
        print(guidebook[i].num)


def score_sort(N, guidebook):
    for i in range(N-1):
        for j in range(N-1):
            if guidebook[j].score < guidebook[j+1].score:
                guidebook[j], guidebook[j+1] = (
                    guidebook[j+1], guidebook[j] )


def city_sort(N, guidebook):
    for i in range(N-1):
        for j in range(N-1):
            if str(guidebook[j].city) > str(guidebook[j+1].city):
                guidebook[j], guidebook[j+1] = (
                    guidebook[j+1], guidebook[j] )


if __name__ == '__main__':
    N = int(input()) # number of restaurants
    guidebook = []
    for i in range(N):
        s, p = input().split()
        restaurant = Guidebook(i+1, s, int(p))
        guidebook.append(restaurant)

    score_sort(N, guidebook)
    city_sort(N, guidebook)
    print_number(N, guidebook)
