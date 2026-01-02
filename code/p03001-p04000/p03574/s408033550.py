def aroundbom(i , q , h , w , sl):
    bomcount = 0
    dx = [1 , 1 , 0 , -1 , -1 , -1 , 0 , 1]
    dy = [0 , 1 , 1 , 1 , 0 , -1 , -1 , -1]

    for b in range(len(dx)):
        t = i + dx[b]
        y = q + dy[b]
        if t >= 0 and t < h and y >= 0 and y < w and sl[t][y] == "#":
            bomcount += 1

    return str(bomcount)

def minesweeper(h , w , sl):

    ans = []

    for i in range(h):
        count = []
        for q in range(w):
            if sl[i][q] == ".":
                count.append(aroundbom(i , q , h , w , sl))
            else:
                count.append("#")
        ans.append(count)

    return ans

def main():
    h , w = map(int , input().split())
    sl = [list(str(input())) for i in range(h)]
    ans = minesweeper(h , w , sl)

    for i in ans:
        print("".join(i))

if __name__ == '__main__':
    main()