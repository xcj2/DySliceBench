# ABC159e

ans = 10 ** 12


def main():
    import sys
    import numpy as np
    sys.setrecursionlimit(10 ** 6)
    from copy import deepcopy
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    h, w, K = map(int, input().split())
    s = [list(map(int, list(input()))) for _ in range(h)]
    s = np.array(s).T
    s = s.tolist()
    # print(s)

    waru = set()

    def dfs(i):
        if i == h-1:
            cho = [0] * (len(waru) + 1)
            bunkatsu = [False]*(w-1)
            sl = [0]
            sl.extend(list(waru))
            sl.append(h)
            t = len(waru)
            j = 0
            while j < w:
                for k in range(1, len(sl)):
                    #print(sl[k - 1], sl[k])
                    cho[k - 1] += sum(s[j][sl[k - 1]: sl[k]])
                #print(waru, j, cho)
                for k in range(len(sl)-1):
                    if cho[k] > K:
                        if bunkatsu[j-1]:
                            return
                        cho = [0] * (len(waru) + 1)
                        bunkatsu[j-1] = True
                        t += 1
                        j -= 1
                j += 1
            #print(waru, t)
            global ans
            ans = min(ans, t)
            return
        waru.add(i+1)
        dfs(i + 1)
        waru.remove(i+1)
        dfs(i + 1)
    dfs(0)
    print(ans)


if __name__ == '__main__':
    main()
