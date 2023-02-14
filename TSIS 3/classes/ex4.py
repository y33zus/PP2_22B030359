import math

class point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        return self.x, self.y
    
    def move(self, x, y):
        self.x += x
        self.y += y
        return self.x, self.y
        
    def dist(self, point):
        dx = point.x - self.x
        dy = point.y - self.y
        return math.sqrt(dx ** 2 + dy ** 2)
pointex=point(int(input()),int(input()))
pointex2=point(int(input()),int(input()))
print(pointex.show())
print(pointex.move(10,10))
print(pointex.dist(pointex2))