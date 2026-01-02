def parent(num):
    return int(num/2)

def left(num):
    return int(num*2)

def right(num):
    return int(num*2)+1

if __name__ == "__main__":    
    n = int(input())
    h_list = [-1] + list(map(int, input().split()))
    for i in range(1, n+1):
        sentence = 'node {0}: key = {1}, '.format(i, h_list[i])
        if parent(i) > 0:
            sentence += 'parent key = {0}, '.format(h_list[parent(i)])
        if left(i) <= n:
            sentence += 'left key = {0}, '.format(h_list[left(i)])
        if right(i) <= n:
            sentence += 'right key = {0}, '.format(h_list[right(i)])
        print(sentence)

