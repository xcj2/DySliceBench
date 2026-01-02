### input test
"""
N = 6
rawP = [
(16,24,0),
(2,3,0),
(2,1,0),
(1,2,0),
(3,2,0),
(2,2,1),
]
# => expected(2,2,1)
###
"""
N = int(input())
rawP = [tuple(map(int, input().split())) for _ in range(N)]


###
# get 1 index where h is not 0
# N < 101*101 ==> h > 0 at least 1 point
P = []
for i in range(N):
    if rawP[i][2] > 0:
       P.append(rawP[i])
REGi = len(P)-1

# if only 1 point (h>0) given, that is the center
if len(P) == 1:
    print(*P[REGi])
    exit(0)

def dist(p1, p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])

def is_correct_center(cx, cy):
    now_C = (cx, cy, 0)  # Is this the center?
    # get first sample where h is not 0
    reg_D = dist(P[REGi], now_C)
    reg_H = P[REGi][2]
    for i in range(len(P)):
        now_D = dist(P[i], now_C)
        now_H = P[i][2]
        # higher_H if nearer_D
        if (- now_D + reg_D) != (now_H - reg_H):
            return False
    return True

def get_answers(cx, cy):
    H = P[REGi][2] + dist(P[REGi], (cx, cy, 0))
    return cx, cy, H

### Start from here...
for cx in range(101):
    for cy in range(101):
        if is_correct_center(cx, cy):
            print(*get_answers(cx, cy))
            exit(0)
