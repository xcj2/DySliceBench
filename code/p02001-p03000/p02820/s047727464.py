class Hand:

    def __init__(self):
        self.flag_r = False
        self.flag_s = False
        self.flag_p = False

    def set_flag(self,str,bool):

        if str == "r":
            self.flag_r = bool

        elif str == "s":
            self.flag_s = bool

        elif str == "p":
            self.flag_p = bool

    def get_flag(self,str):

        if str == "r":
            return self.flag_r

        elif str == "s":
            return self.flag_s

        elif str == "p":
            return self.flag_p

class Point:

    def __init__(self,r,s,p):
        self._R = r#ぐ
        self._S = s#ch
        self._P = p#pa

    def get_point(self,str):

        if str == "r":
            return self._P

        elif str == "s":
            return self._R

        elif str == "p":
            return self._S


if __name__ == '__main__':

    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = list(input())
    #print(T)


    Hands = [Hand() for i in range(len(T))]
    Point = Point(R,S,P)
    ans = 0

    for i in range(len(T)):

        #じゃんけん
        if Hands[i].get_flag(T[i]) == False:
            #print(Point.get_point(T[i]))
            ans += Point.get_point(T[i])

            #k回目のflagがtrue
            try:
                Hands[i+K].set_flag(T[i],True)
            except:
                pass

        else:
            continue


    print(ans)
