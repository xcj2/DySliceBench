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

d1_nums = [int(x) for x in stdin.readline().rstrip().split()]
d2_nums = [int(x) for x in stdin.readline().rstrip().split()]
if set(d1_nums) != set(d2_nums):
    print("No")

d1 = Dice(d1_nums)
d2 = Dice(d2_nums)

# TとSに対応するクエリを記憶し, resをすぐに呼び出せるようにする
memo = [[False] * 7 for i in range(7)]
memo[d1.pos["T"]][d1.pos["S"]] = ""

# クエリとさいころd1の状態を記憶
res = {}
for j in ["T", "S", "E"]:
    if d1.labels[d1.pos[j]] != d2.labels[d2.pos[j]]:
        break        
    else:
        res[memo[d1.pos["T"]][d1.pos["S"]]] = d1

# BFSで探索, 今回は目の数字が同一である可能性があるため全探索
# ただし, T, S, Eがd2と同一のもののみresに登録
# diceの中身をいじってはならない
def solve(dice=d1):
    que = queue.Queue()
    que.put(dice)
    sol_q = ["E", "N", "S", "W"]
    
    while not que.empty():
        d = que.get()
        for i in sol_q:
            d_next = Dice.rolled(d, i)
            if memo[d_next.pos["T"]][d_next.pos["S"]] == False:
                que.put(d_next)
                memo[d_next.pos["T"]][d_next.pos["S"]] = memo[d.pos["T"]][d.pos["S"]] + i
                for j in ["T", "S", "E"]:
                    if d_next.labels[d_next.pos[j]] != d2.labels[d2.pos[j]]:
                        break
                else:
            	    res[memo[d_next.pos["T"]][d_next.pos["S"]]] = d_next
    else:
        return True

solve()
check_pos = ["N", "W", "B"]
if len(res) == 0:
	print("No")
else:
    for k, v in res.items():
        for i in check_pos:
            if v.labels[v.pos[i]] != d2.labels[d2.pos[i]]:
                break
        else:
            print("Yes")
            break
    else:
        print("No")
