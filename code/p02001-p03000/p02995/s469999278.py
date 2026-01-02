def main():
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a%b)
    def lcd(a, b):
        return int(a / gcd(a, b)) * b
    
    a, b, c, d = map(int, input().split())

    def anti_div(x, y, z):
        # x:n以下の対象の値, y:割る値1, z:割る値2
        # 全体からcで割れるものを引くそして、dで割れるものを引く c,dどちらでも割れるものをたす
        cnt = x
        cnt -= x // c
        cnt -= x // d
        # cでもdでも割れるものがいくつあるか
        cnt += x // lcd(c, d)
        return cnt
    # a以上b以下でどうこうっていう時の数え上げは
    # b以下で数えて「a-1以下」で数えたのを引く
    ans = anti_div(b, c, d) - anti_div(a-1, c, d)
    print(ans)

if __name__ == '__main__':
    main()