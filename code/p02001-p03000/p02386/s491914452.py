from copy import deepcopy
from itertools import groupby
import queue
import sys

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

n = int(sys.stdin.readline().rstrip())
d_nums = [tuple([int(x) for x in sys.stdin.readline().rstrip().split()]) for _ in range(n)]

if len(d_nums) != len(set(d_nums)):
    print("No")
else:
	
    def var(data):
        ava = sum(data)/len(data)
        return sum([(ava-data[i])**2 for i in range(len(data))])/len(data)

    d_nums.sort(key=lambda t: sum(t))
    d_nums.sort(key=lambda t: var(t))
    for (_, g) in groupby(d_nums, key=lambda t: var(t)):
        gl = list(g)
        if len(gl) == 1:
            continue
        else:
            for i in range(len(gl)):
                for j in range(i+1, len(gl)):
                    if Dice.isDiceSame(Dice(gl[i]), Dice(gl[j])):
                        print("No")
                        sys.exit()
    else:
        print("Yes")
