def resolve():
    '''
    code here
    '''
    H, W = [int(item) for item in input().split()]

    grid = [[item for item in input()] for _ in range(H)]

    # print(grid)

    def chk(i,j):
        next_node_list = [
            [max(0, i-1), j],
            [min(H-1, i+1), j],
            [i, max(0, j-1)],
            [i, min(W-1, j+1)]
        ]


        if grid[i][j] == '#':
            for next_node in next_node_list:
                if next_node == [i, j]:
                    pass
                else:
                    if grid[next_node[0]][next_node[1]] == '#':
                        return True
            else:
                return False
        else:
            return True


    def loop_chk(H, W):
        for i in range(H):
            for j in range(W):
                # print(i,j, chk(i,j))
                if chk(i,j):
                    pass
                else:
                    return False
        else:
            return True

    if loop_chk(H, W):
        print('Yes')
    else:
        print('No')
    

if __name__ == "__main__":
    resolve()
