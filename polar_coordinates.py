import math

class Polar:
        def __init__(self,radius : int,angle : float):
                self.radius=radius
                self.angle=angle

        def __repr__(self):
                return f"Radius: {self.radius}\nAngle: {self.angle}"

        def converting_to_cartesian(self):
                x = self.radius*math.cos(self.angle)
                y = self.radius*math.sin(self.angle)
                return x, y

        def converting_to_polar(self, x, y):
                radius = math.sqrt(x**2 + y**2)
                theta = math.atan(y/x)
                theta = 180 * theta/math.pi
                return radius, theta

        def __add__(self, obj):
                x1, y1 = obj.converting_to_cartesian()
                x2, y2 = self.converting_to_cartesian()
                return Polar(x1+x2, y1+y2)

point1 = Polar(3, 45)
point2 = Polar(5,30)

point3 = point2.__add__(point1)
print(point3)


