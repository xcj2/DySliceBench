
maxscore = 0



def solve():
    ans = [-1]*n
    ans[-1] = m
    rek(ans, m, 1)
    return

def rek(ans, m, rekdepth):
    global maxscore
    curr_ans = ans.copy()
    for i in range(1, m+1):
        curr_ans[-rekdepth-1] = i
        if rekdepth == n-1:
            score = get_score(curr_ans)
            maxscore = max(maxscore, score)
        else:
            rek(curr_ans.copy(), i, rekdepth + 1)


def get_score(arr):
    score = 0
    for (a, b, c, d) in abcd:
        if (arr[b-1] - arr[a-1] == c):
            score += d
    return score



# n = int(input())
n, m, q = [int(s) for s in input().split(" ")]
abcd = []
for i in range(q):
    abcd.append([int(s) for s in input().split(" ")])

solve()
print(maxscore)
