class measure:
    def __init__(self, init, station_count):
        self.init = init
        self.station_count = station_count
    def clockwise(self, pos):
        return (self.station_count - self.init + pos) % self.station_count
    def anticlockwise(self, pos):
        return (self.station_count + self.init - pos) % self.station_count
    
import sys
from bisect import bisect

f = sys.stdin


n, _, init = map(int, f.readline().split())
d = sorted(list(map(int, f)))


m = measure(init, n)

dist = []

n_pos = bisect(d, init) if d[0] < init < d[-1] else 0
dist.append(m.anticlockwise(d[n_pos]))

p_pos = n_pos - 1
dist.append(m.clockwise(d[p_pos]))

for di, dj in zip(d, d[-1:] + d[:-1]):
    dist.append(m.anticlockwise(di) * 2 + m.clockwise(dj))
    dist.append(m.anticlockwise(di) + 2 * m.clockwise(dj))

print(min(dist) * 100)