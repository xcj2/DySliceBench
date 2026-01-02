from sys import stdin, stdout # only need for big input

max_honest = 0
testomonies = []
state = []

def dfs(person):
    global max_honest
    if person >= len(state):
        correctState = True
        for p in range(len(state)):
            if state[p] == 1:
                for t in testomonies[p]:
                    x, y = t
                    if state[x] != y:
                        correctState = False
                        break
        if correctState:
            sum = 0
            for s in state:
                sum += s
            max_honest = max(max_honest, sum)
        return

    state[person] = 0
    dfs(person + 1)

    state[person] = 1 
    dfs(person + 1)
    

def solve():
    global state
    n = int(stdin.readline())
    for _ in range(n):
        a = int(stdin.readline())
        t = []
        for _ in range(a):
            x, y = [int(inp) for inp in stdin.readline().split()]
            t.append((x - 1,y))
        testomonies.append(t)
    # print(testomonies)
    state = [-1] * n
    dfs(0)
    print(max_honest)


def main():
    solve()


if __name__ == "__main__":
    main()