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

nums = [int(x) for x in stdin.readline().rstrip().split()]
q = int(stdin.readline().rstrip())
dice = Dice(nums)

# TとSに対応するクエリを記憶し, resをすぐに呼び出せるようにする
memo = [[False] * 7 for i in range(7)]
memo[dice.pos["T"]][dice.pos["S"]] = ""

# クエリとさいころの東面を記憶
res = { "" : dice.labels[dice.pos["E"]] }

# BFSで探索, 解を求めたらreturn Trueで抜け出す
# diceの中身をいじってはならない
def solve(T, S):
	que = queue.Queue()
	que.put(dice)
	sol_q = ["E", "N", "S", "W"]
	
	while not que.empty():
		d = que.get()
		if d.pos["T"] == T and d.pos["S"] == S:
			break
		else:
			for i in sol_q:
				d_next = Dice.rolled(d, i)
				que.put(d_next)
				memo[d_next.pos["T"]][d_next.pos["S"]] = memo[d.pos["T"]][d.pos["S"]] + i
				res[memo[d_next.pos["T"]][d_next.pos["S"]]] = d_next.labels[d_next.pos["E"]]
	else:
		return memo[T][S]

for i in range(q):
    ts = [int(x) for x in stdin.readline().rstrip().split()]
    T = dice.labels.index(ts[0])
    S = dice.labels.index(ts[1])
    
    if solve(T, S) != False:
        print(res[memo[T][S]])
