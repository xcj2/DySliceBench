import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

# シミュレーション関数
def to_end(num, board, query, goal):
    for (qs, qd) in query:
        if qs == board[num]:
            if qd == 'L':
                num -= 1
            elif qd == 'R':
                num += 1
                
            if num == goal:
                return True
            
    return False


# 左へ二分探索
def find_rightest_left(board, query):
    left = 0
    right = len(board)-1
    
    while right-left > 1:
        mid = (left+right) // 2
        if to_end(mid, board, query, 0):
            left = mid
        else:
            right = mid
            
    return left
            
# 右へ二分探索
def find_leftest_right(board, query):
    R = len(board)-1
    left = 0
    right = R
    
    while right-left > 1:
        mid = (left+right) // 2
        if to_end(mid, board, query, R):
            right = mid
        else:
            left = mid
            
    return R - right
    
n,q = li()
board = "0" + ns() + "0"
query = [tuple(ls()) for _ in range(q)]

rightest_left = find_rightest_left(board, query)
leftest_right = find_leftest_right(board, query)

print(max(n - rightest_left - leftest_right, 0))