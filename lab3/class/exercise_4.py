import math
class Point:
    def __init__(self, x = int(input()), y = int(input())):
        self.x_init = x
        self.y_init = y
    
    def show(self):
        return (self.x_init, self.y_init)

    def move(self, dx = int(input()), dy = int(input())):
        self.x_fin = dx
        self.y_fin = dy
        return (self.x_fin, self.y_fin)

    def dist(self):
        return math.sqrt((self.y_fin - self.y_fin)**2 +(self.x_fin - self.x_init)**2)
    
p = Point()

a = p.show()
b = p.move()
c = p.dist()

print("\n Initial point is: {}\n".format(a), 
      "Point was moved to: {}\n".format(b), 
      "Distance between two points:", c)
    
