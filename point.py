from math import sqrt
pi = 3.14
pi = int(pi)

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

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def length(self):
        return (self.p2.y - self.p1.y)

    def width(self):
        return (self.p2.x - self.p1.x)
    
    def area(self):
        l = self.length()
        w = self.width()
        return (l*w)
    
    def perimiter(self):
        l = self.length()
        w = self.width()

        return ((2*l)+(2*w))

class Circle:

    def __init__(self, r, mp):
        self.r = r
        self.mp = mp

    def pointCheck(self):
        '''
        Check if point (0, 1) is inside of the circle
        '''

    def cArea(self):
        return (pi*(self.r*self.r))
    
    def cPerimiter(self):
        '''
        get the perimiter of the circle
        '''

def main():
    '''
    p12 = Point(3.0, 4.0)
    print("The point ({}, {}) is at a distance of {} from the origin.".format(p1.x, p1.y, p1.abs()))

    p22 = Point(-1.0, 6.5)
    print("It is a distance {:.5} away from the point ({}, {}).".format(p1.dist_to(p2), p2.x, p2.y))
    '''

    p12 = Point(1.0, 1.0)
    p22 = Point(4.0, 5.0)
    rect = Rectangle(p12, p22)
    print('The area of this rectangle is {}'.format(rect.area()))
    print('The perimiter of this rectangle is {}'.format(rect.perimiter()))

    r = 2
    r = int(r)
    mp = Point(-2, 3)
    circ = Circle(r, mp)
    print('The area of this circle is {}'.format(circ.cArea()))

if __name__ == "__main__":
    main()