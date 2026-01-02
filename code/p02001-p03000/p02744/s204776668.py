from collections import deque # BFSはこいつを使え！
def dfs(n):
    adj = 'abcdefghij'
    
    stack = deque(['a'])
    while stack:
        # node = stack.pop(0) # pop(0)がO(n)かかっているのでとても遅い！
        node = stack.popleft()
        if len(node) == n:
            print(node)
        else:
            
            for child in adj[:len(set(node))+1]:
                stack.append(node+child)
    return -1

# 再帰での実装
# def dfs(s,n,adj):
#     if len(s) == n:
#         print(s)
#     else:
#         for child in adj[:len(set(s))+1]:
#             dfs(s+child,n,adj)
#     return -1

def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    n = int(input())
    # adj = 'abcdefghij'
    # dfs('a',n,adj)
    dfs(n)

if __name__ == '__main__':
    main()