def resolve():
    '''
    code here
    '''
    import collections
    N = int(input())
    A_list = [[int(item) for item in input().split()] for _ in range(N)]
    A_list.sort(key=lambda x:x[0])

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


    def preorder(node):
        if node == -1:
            return

        print('',node, end='')
        left = A_list[node][1]
        right = A_list[node][2]
        preorder(left)
        preorder(right)

    for i in range(N):
        if is_root(i):
            root = i
            break

    def inorder(node):
        if node == -1:
            return

        left = A_list[node][1]
        right = A_list[node][2]
        inorder(left)
        print('',node, end='')
        inorder(right)
    
    def postorder(node):
        if node == -1:
            return

        left = A_list[node][1]
        right = A_list[node][2]
        postorder(left)
        postorder(right)
        print('',node, end='')

    for i in range(N):
        if is_root(i):
            root = i
            break
    
    print('Preorder')
    preorder(root)
    print('')


    print('Inorder')
    inorder(root)
    print('')

    print('Postorder')
    postorder(root)
    print('')


if __name__ == "__main__":
    resolve()

