from math import sqrt

class Point:

    x = 0.0
    y = 0.0

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def dist_to(self, p):
        return sqrt((self.x - p.x)**2 + (self.y - p.y)**2)

    
    def abs(self):
        return sqrt(self.x**2 + self.y**2)

class Rectangle:
    x = 0.0
    y = 0.0

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def length(self, p, p2):
        return (p2[2] - p[2]) 

    def width(self, p, p2):
        return (p2[1] - p[1])

    def area(self, p, p2):
        l = length(p, p2)
        w = width(p, p2)

        return (l*w)

    def perimiter(self, p, p2):
        l = length(p, p2)
        w = width(p, p2)

        return ((2*l)+(2*w))
        
 

def main():
    p12 = Point(3.0, 4.0)
    print("The point ({}, {}) is at a distance of {} from the origin.".format(p1.x, p1.y, p1.abs()))

    p22 = Point(-1.0, 6.5)
    print("It is a distance {:.5} away from the point ({}, {}).".format(p1.dist_to(p2), p2.x, p2.y))


if __name__ == "__main__":
    main()
