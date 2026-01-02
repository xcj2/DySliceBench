from sys import stdin
from copy import deepcopy
import queue

class Dice:
    def __init__(self, nums):
        self.labels = [None] + [ nums[i] for i in range(6) ]
        self.pos = {
            "E" : 3,
            "W" : 4,
            "S" : 2,
            "N" : 5,
            "T" : 1,
            "B" : 6
        }

    def rolled(dice, queries):
        d = deepcopy(dice)
        for q in queries:
            if q == "E":
                d.pos["T"], d.pos["E"], d.pos["B"], d.pos["W"] = d.pos["W"], d.pos["T"], d.pos["E"], d.pos["B"]
            elif q == "W":
                d.pos["T"], d.pos["E"], d.pos["B"], d.pos["W"] = d.pos["E"], d.pos["B"], d.pos["W"], d.pos["T"]
            elif q == "S":
                d.pos["T"], d.pos["S"], d.pos["B"], d.pos["N"] = d.pos["N"], d.pos["T"], d.pos["S"], d.pos["B"]
            elif q == "N":
                d.pos["T"], d.pos["S"], d.pos["B"], d.pos["N"] = d.pos["S"], d.pos["B"], d.pos["N"], d.pos["T"]
        else:
            return d

    def isDiceSame(d1, d2):
        if not isinstance(d1, Dice) or not isinstance(d2, Dice):
            return False

        if set(d1.labels[1:]) != set(d2.labels[1:]):
            return False

        else:
            q = ["T", "S", "E", "N", "W", "B"]
            memo = [[False] * 7 for i in range(7)]
            memo[d1.pos["T"]][d1.pos["S"]] = ""
            res = {}
            for i in q[:3]:
                if d1.labels[d1.pos[i]] != d2.labels[d2.pos[i]]:
                    break
            else:
                res[memo[d1.pos["T"]][d1.pos["S"]]] = d1

            def bfs_isDiceSame():
                que = queue.Queue()
                que.put(d1)

                while not que.empty():
                    d = que.get()
                    for i in q[1:5]:
                        d_next = Dice.rolled(d, i)
                        if memo[d_next.pos["T"]][d_next.pos["S"]] == False:
                            que.put(d_next)
                            memo[d_next.pos["T"]][d_next.pos["S"]] = memo[d.pos["T"]][d.pos["S"]] + i
                            for j in q[:3]:
                                if d_next.labels[d_next.pos[j]] != d2.labels[d2.pos[j]]:
                                    break
                            else:
                                res[memo[d_next.pos["T"]][d_next.pos["S"]]] = d_next

            bfs_isDiceSame()
            if len(res) == 0:
                return False
            else:
                for k, v in res.items():
                    for i in q[3:]:
                        if v.labels[v.pos[i]] != d2.labels[d2.pos[i]]:
                            break
                    else:
                        return True
                else:
                    return False

d1_nums = [int(x) for x in stdin.readline().rstrip().split()]
d2_nums = [int(x) for x in stdin.readline().rstrip().split()]
d1 = Dice(d1_nums)
d2 = Dice(d2_nums)
if Dice.isDiceSame(d1, d2):
    print("Yes")
else:
    print("No")
