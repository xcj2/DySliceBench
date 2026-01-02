from collections import Counter


class PickingUp:
    def __init__(self):
        self.N = int(input())
        self.points = []
        for n in range(self.N):
            self.points.append([int(n) for n in input().split()])

    def main(self):
        dif_list = []

        if self.N == 1:
            print(1)
            return

        for s in range(self.N):
            for e in range(self.N):
                if s == e:
                    continue
                dif = self.__cal_dif(self.points[s], self.points[e])
                dif_list.append("{},{}".format(dif[0], dif[1]))

        c = Counter(dif_list)
        most = c.most_common()[0][1]

        print(self.N - most)

    def __cal_dif(self, s, e):
        dif_x = s[0] - e[0]
        dif_y = s[1] - e[1]
        return [dif_x, dif_y]


pickingUp = PickingUp()
pickingUp.main()
