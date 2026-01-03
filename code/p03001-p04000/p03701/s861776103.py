def bugged(ss):
    ss2 = list(sorted(ss))
    total = sum(ss2)
    if total % 10 != 0:
        return total
    elm = None
    for s in ss2:
        if s % 10 != 0:
            elm = s
            break
    return total - elm if elm else 0

def main():
    N = int(input())
    ss = []
    for i in range(N):
        ss.append(int(input()))
    print(bugged(ss))

main()
    
def test():
    print(bugged([5,10,15]))
    print(bugged([10,10,15]))
    print(bugged([10,20,30]))
    print(bugged([32,53252,212,4324,122,10,43,32,3232,120]))
    print(bugged([12,23,45,65,43,42]))
  