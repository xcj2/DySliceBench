#http://abc057.contest.atcoder.jp/tasks/abc057_b
import sys

def myabs(a):
    return a if a >= 0 else -a

def dist(x1, y1, x2, y2):
    return myabs(x1-x2) + myabs(y1-y2)

def calc(people_points, check_points):
    ans = []

    #それぞれの人に関して、チェックポイントまでの距離を求める
    for x_p, y_p in people_points:
        dists = [ dist(x_p, y_p, check_point[0], check_point[1]) for check_point in check_points ]
        ans_ind, ans_dist = sorted(list(enumerate(dists)), key=lambda tpl:tpl[1])[0]
        ans_tpl = (ans_ind, ans_dist)
        ans.append(ans_tpl)


    return ans

def main():
    n_m = sys.stdin.readline().split()
    n = int(n_m[0])
    m = int(n_m[1])

    people_points = []
    check_points = []

    for i in range(n):
        a_b = sys.stdin.readline().split()
        a = int(a_b[0])
        b = int(a_b[1])
        people_points.append((a, b))

    for i in range(m):
        c_d = sys.stdin.readline().split()
        c = int(c_d[0])
        d = int(c_d[1])
        check_points.append((c, d))

    ans = [ind + 1 for ind, dist in calc(people_points, check_points)]
    print("\n".join([str(i) for i in ans]))

    return 0

if __name__ == '__main__':
    sys.exit(main())
