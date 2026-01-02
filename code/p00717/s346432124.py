class Line:
    def __init__(self, n, points):
        self.n = n
        self.points = points

    def getDesc(self):
        desc1 = self.getDist(self.points[0], self.points[1])
        faceDir = self.getDir(self.points[0], self.points[1])
        for i in range(1, self.n - 1):
            newDir = self.getDir(self.points[i], self.points[i+1])
            desc1 += self.getTurn(faceDir, newDir)
            desc1 += self.getDist(self.points[i], self.points[i+1])
            faceDir = newDir

        desc2 = self.getDist(self.points[-1], self.points[-2])
        faceDir = self.getDir(self.points[-1], self.points[-2])
        for i in range(self.n - 2, 0, -1):
            newDir = self.getDir(self.points[i], self.points[i-1])
            desc2 += self.getTurn(faceDir, newDir)
            desc2 += self.getDist(self.points[i], self.points[i-1])
            faceDir = newDir

        return sorted([desc1, desc2])

    def getTurn(self, origDir, destDir):
        if origDir == 'N':
            if destDir == 'E':
                return '1'
            elif destDir == 'S':
                return '2'
            elif destDir == 'W':
                return '3'
        if origDir == 'E':
            if destDir == 'S':
                return '1'
            elif destDir == 'W':
                return '2'
            elif destDir == 'N':
                return '3'
        if origDir == 'S':
            if destDir == 'W':
                return '1'
            elif destDir == 'N':
                return '2'
            elif destDir == 'E':
                return '3'
        if origDir == 'W':
            if destDir == 'N':
                return '1'
            elif destDir == 'E':
                return '2'
            elif destDir == 'S':
                return '3'
        
    def getDir(self, p1, p2):
        if p1[1] < p2[1]:
            return 'N'
        if p1[0] < p2[0]:
            return 'E'
        if p1[0] > p2[0]:
            return 'W'
        if p1[1] > p2[1]:
            return 'S'

    def getDist(self, p1, p2):
        if p1[0] != p2[0]:
            return str(abs(p1[0] - p2[0]))
        return str(abs(p1[1] - p2[1]))

def getPolyLine():
    n = int(input())
    points = []
    for _ in range(n):
        x, y = list(map(int, input().strip().split()))
        points.append( (x, y) )
    return Line(n, points)

if __name__ == '__main__':
    while True:
        N = int(input())
        if N == 0:
            break

        polyLine = getPolyLine()
        template = polyLine.getDesc()
        P = polyLine.n

        for idx in range(1, N + 1):
            polyLine = getPolyLine()
            desc = polyLine.getDesc()
            if polyLine.n == P and desc[0] == template[0] and desc[1] == template[1]:
                print(idx)

        print("+++++")
