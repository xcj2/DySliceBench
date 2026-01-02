from itertools import combinations, permutations
from bisect import bisect_right, bisect_left

def solve(N, S):
    left = [-1]*10
    right = [-1]*10
    place = [[] for i in range(10)]
    for i in range(N):
        c = int(S[i])
        if left[c] == -1:
            left[c] = i
        right[c] = i
        place[c].append(i)

    def ok(s, dbg=False):
        l, m, r = [int(c) for c in s]
        if left[l] == -1 or right[r] == -1:
            return False
        if not left[l] < right[r]:
            return False
        j = bisect_right(place[m], left[l])
        if j == len(place[m]):
            return False
        mid = place[m][j]
        if mid < right[r]:
            #print(left[l], place[m], right[r])
            #print(left[l], mid, right[r])
            return True
        return False

    count = 0
    for i in range(0, 1000):
        s = "%03d" % i
        if ok(s):
            count += 1
    #print(ok("224", True))

    return count

def check(N, S):
    c = set()
    for s in combinations(range(N), 3):
        s = tuple(S[i] for i in s)
        #s = S[:i] + S[i+1:j] + S[j+1:k] + S[k+1:]
        if s not in c:
            pass
        c.add(s)
        
    return len(c)

def main():
    N = int(input())
    S = input()
    #print(check(N, S))
    print(solve(N, S))

def test(S):
    print(S,check(len(S), S), "==", solve(len(S), S))

#test("0224")
#test("123123")
#test("3141592653589793238")
main()
