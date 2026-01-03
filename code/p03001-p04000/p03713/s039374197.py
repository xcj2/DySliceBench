H, W = map(int,input().split())

def side(h, W):
    Sa = W * h
    Sb = W * ((H-h)//2)
    Sc = W * ((H-h+1)//2)
    # print (Sa, Sb, Sc)
    return max(Sa, Sb, Sc) - min(Sa, Sb, Sc)

def vertical(h, W):
    Sa = W * h
    Sb = W//2 * (H-h)
    Sc = ((W+1)//2) * (H-h)
    # print (Sa, Sb, Sc)
    return max(Sa, Sb, Sc) - min(Sa, Sb, Sc)


def judge(H, W):
    ans = H * W
    for h in range(0, H):
        # print (side(h, W), vertical(h, W))
        ans = min(ans, side(h, W), vertical(h, W))
        # print (h, W, ans)
    return ans

tmp = judge(H, W)
H, W = W, H
tmp = min(tmp, judge(H, W))
print (tmp)


# print (judge(3, 5))