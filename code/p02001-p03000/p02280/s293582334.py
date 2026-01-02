def resolve():
    '''
    code here
    '''
    import collections
    N = int(input())
    A_list = [[int(item) for item in input().split()] for _ in range(N)]
    A_list.sort(key=lambda x:x[0])

    # print(A_list)
    T = [[0 for _ in range(7)] for _ in range(N)]

    # bfs
    def bfs(root):
        que = collections.deque([[root, 0, -1]])
        temp_depth = 0
        while que:
            # print(que)
            temp = que.popleft()
            temp_node = temp[0]
            temp_depth = temp[1]
            temp_parent = temp[2]
            T[temp_node][0] = temp_node
            T[temp_node][1] = temp_parent 
            T[temp_node][4] = temp_depth
            children = A_list[temp_node][1:3]
            cnt = 0
            # print(children)
            for child in children:
                if child >= 0:
                    cnt +=1
                    que.append([child, temp_depth+1, temp_node])
                    # print(que)
            T[temp_node][3] = cnt

            siblings = A_list[temp_parent][1:3]
            for sibling in siblings:
                if sibling != temp_node:
                    T[temp_node][2] = sibling


    def height(node):

        max_depth = 0
        height_que = collections.deque([[node, 0]])

        while height_que:
            temp = height_que.popleft()
            temp_node = temp[0]
            temp_depth = temp[1]
            children = A_list[temp_node][1:3]
            # print(children)
            for child in children:
                if child >= 0:
                    height_que.append([child, temp_depth+1])
            max_depth = max(max_depth, temp_depth)
        
        return max_depth 

    def is_root(node):
        root_check_que = collections.deque([node])
        foot_print = [False for _ in range(N)]

        while root_check_que:
            temp_node = root_check_que.popleft()
            foot_print[temp_node] = True
            children = A_list[temp_node][1:3]

            for child in children:
                if child >= 0 and foot_print[child] == False:
                    root_check_que.append(child)

        return all(foot_print)

    
    for i in range(N):
        if is_root(i):
            root = i
            break

    bfs(root)

    for node, left, right in A_list:

        if T[node][1] == -1:
            T[node][6] = 'root' #type
        elif left == -1 and right == -1:
            T[node][6] = 'leaf'
        else:
            T[node][6] = 'internal node'

        T[node][5] = height(node)


    for node, parent, sibling, degree, depth, height, node_type in T:
        print('node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}'.format(node, parent, sibling, degree, depth, height, node_type))
    
if __name__ == "__main__":
    resolve()

