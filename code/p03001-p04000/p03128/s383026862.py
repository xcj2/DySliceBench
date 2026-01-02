def func(latter, remains, former = []):
    #print(remains, former, latter)
    if remains == 0:
        return sum(x for _,x in former)
    if len(latter) == 0:      # 諦めて戻る
        while True:
            b, p = former.pop()    # formerの先頭から順に取り出し
            if p==0:               # ゼロの間は
                latter.append(b)   # latterに入れて
            else:             # ゼロでないものが見つかった時
                break         # ストップ
        return func(latter, remains+b, former+[(b, p-1)])
    a = latter.pop()
    q, r = divmod(remains, a)
    if r!=0: # 端数が出た時
        q = q-1 if q > 0 else 0  # ひとつ以上入るなら、ひとつ減らして入れ、入らないなら入れない
    return func(latter, remains-q*a, former+[(a, q)])

def func2(l, remains, remain_num, ans=[]):
    #print(l, remains, remain_num, ans)
    if len(l)>0:
        a, *l = l
        for i in range(min(remains//a, remain_num)+1):
            yield from func2(l, remains-a*i, remain_num-i, [(a, i)]+ans)
    elif remain_num==0 and remains==0:
        yield ans

n, m = map(int, input().split())
s = sorted((int(x) for x in input().split()), reverse=True)
num = [6,2,5,5,4,5,6,3,7,6]
t = sorted({num[i] for i in s}, reverse=True)
t_rev = {x:max(j for j in s if num[j]==x) for x in t}
t_min = t[-1]
m_num = func(t.copy(), n)   # 桁数
max_replacement = n - m_num*t_min        # 最小マッチでない数以外の数を最大何個使えるか
min_match_num = max(0, m_num - max_replacement)  # 最小マッチ数の数を少なくともどれだけ使うか
other_num = m_num - min_match_num   # 残された桁数
def func3(ans):
    l = {t_rev[x]:(i+min_match_num if x==t_min else i) for x,i in ans}
    return [l[x] for x in sorted(l, reverse=True)]
answer = max(func3(ans) for ans in func2(t.copy(), n-min_match_num*t_min, other_num))
print(*(str(x)*i for x, i in zip(sorted(t_rev.values(), reverse=True), answer)), sep='')