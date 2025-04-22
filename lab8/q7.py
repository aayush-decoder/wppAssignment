import math  


class Point2D:
    def __init__(self, x,y):
        self.x =x
        self.y= y

    def magnitude(self):  
        return math.sqrt(self.x**2 + self.y**2)
    def rotation(self): 
        return math.atan2(self.y, self.x)  

def distance(p1, p2):  
    return math.sqrt((p1.x - p2.x) **2 + (p1.y - p2.y)**2)  

def dot_prod(v1, v2):  
    return v1.x*v2.x + v1.y * v2.y

def cross_prod(v1, v2):  
    return v1.x*v2.y - v1.y*v2.x  

class Point3D(Point2D): 
    def __init__(self,x,y,z):
        super().__init__(x, y)  
        self.z= z  

    def magnitude(self):   
        return math.sqrt(self.x**2 + self.y**2+ self.z**2)

def dot_prd(v1, v2):
    return v1.x*v2.x + v1.y*v2.y + v1.z * v2.z

def cross_prd(v1, v2):  
    return Point3D(v1.y * v2.z - v1.z * v2.y, v1.z * v2.x - v1.x*v2.z, v1.x*v2.y - v1.y*v2.x)  

p1 = Point2D(3, 4)  
p2 = Point2D(1, 2)
print("magnitude:", p1.magnitude())  
print("rotation:", p1.rotation()) 
print("dist:", distance(p1, p2))  
print("dotProduct:", dot_prod(p1, p2)) 
print("crossProduct:", cross_prod(p1, p2))

v1 = Point3D(1,2,3) 
v2 = Point3D(4,5,6)

print("3D Mag:", v1.magnitude())
print("3D Dot:", dot_prd(v1, v2))
print("3D Cross:", vars(cross_prd(v1,v2)))
