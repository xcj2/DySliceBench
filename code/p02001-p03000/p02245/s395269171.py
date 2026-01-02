from queue import Queue
goal = [1,2,3,4,5,6,7,8,0]
SIZE = 3
cmds = ['up','down','left','right']

def puz_hash(p):
    hash = ''.join(map(str, p))
    return hash

def up(p,z,c):
    if z >= 3 and c != 'down':
        p[z], p[z - 3] = p[z - 3], p[z]
    return p

def down(p,z,c):
    if z <= 5 and c != 'up':
        p[z], p[z + 3] = p[z + 3], p[z]
    return p

def left(p,z,c):
    if z % 3 != 0 and c != 'right':
        p[z], p[z - 1] = p[z - 1], p[z]
    return p

def right(p,z,c):
    if z % 3 != 2 and c != 'left':
        p[z], p[z + 1] = p[z + 1], p[z]
    return p

def search(p):
    q = Queue()
    # init
    q.put((p,0,''))
    visited = set()#[]

    while True:
        if(q.empty()):
            return None
        current_p, current_d, prev_move = q.get()
        current_z = current_p.index(0)
        current_p_hash = puz_hash(current_p)

        if(current_p_hash in visited):
            continue
        if(current_p_hash == goal_hash):
            return current_d
        visited.add(current_p_hash)

        next_p = current_p.copy()
        next_p = up(next_p, current_z, prev_move)
        if(next_p.index(0) != current_z):
            q.put((next_p, current_d+1, cmds[0]))

        next_p = current_p.copy()
        next_p = down(next_p, current_z, prev_move)
        if(next_p.index(0) != current_z):
            q.put((next_p, current_d+1, cmds[1]))

        next_p = current_p.copy()
        next_p = left(next_p, current_z, prev_move)
        if(next_p.index(0) != current_z):
            q.put((next_p, current_d+1, cmds[2]))

        next_p = current_p.copy()
        next_p = right(next_p, current_z, prev_move)
        if(next_p.index(0) != current_z):
            q.put((next_p, current_d+1, cmds[3]))

        # kkkkkusso jikan kakaru
        # for cmd in cmds:
        #     next_p = current_p.copy()
        #     next_p = get_next_states(cmd,next_p,current_z,prev_move)#eval(cmd)(next_p, current_z, prev_move)
        #     if(next_p is not None):
        #         print(current_d+1)
        #         q.put((next_p, current_d+1, cmd))

p = []
for i in range(3):
    p.extend(map(int, input().split()))

goal_hash = puz_hash(goal)
res = search(p)
print(res)

