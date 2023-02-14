class Shape():
    def __init__(self):
        pass

    def area(self):
        return 0

class rectangle(Shape):
    def __init__(self, length = 0, width = 0):
        Shape.__init__(self)
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
ex=rectangle(int(input()),int(input()))
print(ex.area())