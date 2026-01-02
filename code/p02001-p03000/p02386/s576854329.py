import sys
reverse = {
    "E":"W",
    "W":"E",
    "S":"N",
    "N":"S"
    }
        
class dice:
    def __init__(self,A):
        self.list = sorted(A)
        self.max = max(A)
        self.min = min(A)
        self.side = {
            "TOP":A[0],
            "S":A[1],
            "E":A[2],
            "W":A[3],
            "N":A[4],
            "BOT":A[5],
            }
    def get_list(self):
        return self.list
    def get_dict(self):
        return self.side
    def check(self):
        pass
    def main(self,A):
        for s in A:
            var = int(self.side[s])
            self.side[s] = self.side["TOP"]
            self.side["TOP"] = self.side[reverse[s]]
            self.side[reverse[s]] = self.side["BOT"]
            self.side["BOT"] = var
    def rot(self):
        var = self.side["N"]
        self.side["N"] = self.side["E"]
        self.side["E"] = self.side["S"]
        self.side["S"] = self.side["W"]
        self.side["W"] = var
n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]


for i in range(0,n-1):
    a = dice(data[i])
    a_dict = a.get_dict()
    for j in range(i+1,n):
        b = dice(data[j])
        for do in ["N","N","N","N","E","EE"]:
            b.main(do)
            for _ in range(4):
                b.rot()
                b_dict = b.get_dict()
                if a_dict == b_dict:
                    print("No")
                    exit()

        
print("Yes")


