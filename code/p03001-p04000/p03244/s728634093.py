def count2(lst):
    ans = [["",0],0]
    def check():
        nonlocal ans
        if a > ans[0][1]:
            ans[1] = ans[0][1]
            ans[0][0] = last
            ans[0][1] = a
        elif a > ans[1]:
            ans[1] = a
    lst.sort()
    last =lst[0]
    a = 0
    for e in lst:
        if last == e:
            a +=1
        else:
            check()
            last = e
            a = 1
    check()
    return ans

def main(n:int,lst:list)->int:
    ans1 =count2(lst[::2])
    ans2 =count2(lst[1::2])
    if ans1[0][0] == ans2[0][0]:
        return n - max(ans1[0][1] + ans2[1],ans2[0][1] + ans1[1])
    else:
        return n - ans1[0][1] - ans2[0][1]
n = int(input())
lst = input().split()
print(main(n,lst))