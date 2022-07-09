class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return "({}, {}, {})".format(self.a, self.b, self.c)

    def contains(self, p):
        det = (self.b.x - self.a.x) * (self.c.y - self.a.y) - (self.b.y - self.a.y) * (self.c.x - self.a.x)
        return  det * ((self.b.x - self.a.x) * (p.y - self.a.y) - (self.b.y - self.a.y) * (p.x - self.a.x)) >= 0\
            and det * ((self.c.x - self.b.x) * (p.y - self.b.y) - (self.c.y - self.b.y) * (p.x - self.b.x)) >= 0\
            and det * ((self.a.x - self.c.x) * (p.y - self.c.y) - (self.a.y - self.c.y) * (p.x - self.c.x)) >= 0


# Open text file
triangles = []
count = 0
origin = Point(0, 0)

with open('triangles.txt', 'r') as f:
    for line in f.readlines():
        coordinates = list(map(int, line.split(",")))
        points = []
        for i in range(0, len(coordinates), 2):
            p = Point(coordinates[i], coordinates[i+1])
            points.append(p)
        t = Triangle(*points)
        if t.contains(origin):
            count += 1
        triangles.append(t)


print(triangles[0])
print('Solution = {}'.format(count))
