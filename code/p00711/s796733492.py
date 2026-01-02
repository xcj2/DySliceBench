from queue import Queue

def calcReachableTileNumByBFSearch(room, start_pos):
    q = Queue()
    q.put(start_pos)

    count = 1
    while not q.empty():
        cur_pos = q.get()
        D0 = [1, 0, -1, 0]
        D1 = [0, -1, 0, 1]
        for d in range(4):
            nc = [0,0]
            nc[0] = cur_pos[0]+D0[d]
            nc[1] = cur_pos[1]+D1[d]
            if room[nc[0]][nc[1]] == '.':
                room[nc[0]][nc[1]] = '*'
                q.put([nc[0],nc[1]])
                count +=1
    return count


def solve(width, height):
    room = [['#' for i in range(width+2)] for j in range(height+2)]
    for i in range(height):
        row = input()
        for j in range(width):
            room[i+1][j+1] = row[j]
            if room[i+1][j+1] == '@':
                start = [i+1,j+1]

    return calcReachableTileNumByBFSearch(room, start)


def main():
    while True:
        width, height = map(int, input().split())
        if width == 0 and height == 0:
            break
        print(solve(width, height))


if __name__ == "__main__":
    main()

