from collections import deque
def son(generation,life):
    if life > 1:
        nextson = (generation+1, life//2)
    else:
        nextson = (0, 0)
    return nextson
    
def generationnum(generation):
    return 2**generation

def bfs(startlife,startgeneration):
    queue = deque([(startgeneration,startlife)])
    totalnum = 0
    while queue:
        label = queue.popleft()
        if label == (0, 0):
            break
        totalnum += generationnum(label[0])
        queue.append(son(label[0],label[1]))
    return totalnum
            
if __name__ == '__main__':
    print(bfs(int(input()), 0))