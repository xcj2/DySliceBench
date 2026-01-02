from math import sqrt


def cross(P0, P1, P2):
    x0, y0 = P0; x1, y1 = P1; x2, y2 = P2
    x1 -= x0; x2 -= x0
    y1 -= y0; y2 -= y0
    return x1*y2 - x2*y1


def dot(P0, P1, P2):
    x0, y0 = P0; x1, y1 = P1; x2, y2 = P2
    x1 -= x0; x2 -= x0
    y1 -= y0; y2 -= y0
    return x1*x2 + y1*y2


def dist2(P0, P1):
    x0, y0 = P0; x1, y1 = P1
    return (x1 - x0)**2 + (y1 - y0)**2


def collision_ll(S0, S1, T0, T1):
    return cross(S0, S1, T0)*cross(S0, S1, T1) < 0 and cross(T0, T1, S0) * cross(T0, T1, S1) < 0


def dist_lp(S, E, P):
    dd = dist2(S, E)
    if 0 <= dot(S, E, P) <= dd:
        return abs(cross(S, E, P))/sqrt(dd)
    return sqrt(min(dist2(S, P), dist2(E, P)))


def dist_ll(S0, S1, T0, T1):
    if collision_ll(S0, S1, T0, T1):
        return 0
    return min(
            dist_lp(S0, S1, T0),
            dist_lp(S0, S1, T1),
            dist_lp(T0, T1, S0),
            dist_lp(T0, T1, S1)
            )


n = int(input())
for i in range(n):
    x0, y0, x1, y1, X0, Y0, X1, Y1 = map(int, input().split())
    print("%.010f" % dist_ll((x0, y0), (x1, y1), (X0, Y0), (X1, Y1)))
