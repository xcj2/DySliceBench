
def get_next_str():
    return input().rstrip("\n")
def get_next_ints(delim=" "):
    return tuple([int(float(x)) for x in input().split(delim)])
def solve(maze, start_r, start_c):
    
    distances = {}
    offsets = [(-1,0),(1,0),(0,-1),(0,1)]
    
    distances[start_r, start_c] = 0
    candidates = [(start_r, start_c)]
    
    while candidates:
        r, c= candidates.pop(0)
        
        for offset_r, offset_c in offsets:
            move_r, move_c = r + offset_r, c + offset_c
            if not (move_r, move_c) in distances and maze[move_r, move_c] == ".":
                distances[move_r, move_c] = distances[r, c] + 1
                candidates.append((move_r, move_c))
    
    return max(distances.values())
    

def main():
    h, w = get_next_ints()
    from collections import defaultdict
    maze = defaultdict(str)
    for r in range(h):
        line = get_next_str()
        for c in range(w):
            maze[r,c] = line[c]
    
    results = []
    for r in range(h):
        for c in range(w):
            if maze[r,c] != "#":
                result = solve(maze, r, c)
                results.append(result)
    
    print(max(results))
    
if __name__ == '__main__':
    main()