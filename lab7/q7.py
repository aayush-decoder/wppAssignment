import math

class vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otherVector):
        if isinstance(otherVector, vector2D):
            return vector2D(self.x + otherVector.x, self.y + otherVector.y)
        else:
            return NotImplemented
        
    @property
    def magnitude(self):
        return (self.x**2 + self.y**2)**0.5
    
    def rotate(self, angle):
        angle = math.radians(angle)
        x = self.x * math.cos(angle) - self.y * math.sin(angle)
        y = self.x * math.sin(angle) + self.y * math.cos(angle)
        return vector2D(x, y)
    
    def distance(self, otherVector):
        if isinstance(otherVector, vector2D):
            return ((self.x - otherVector.x)**2 + (self.y - otherVector.y)**2)**0.5
        else:
            return NotImplemented
        
    def dot_product(self, otherVector):
        return self.x * otherVector.x + self.y * otherVector.y + self.z * otherVector.z 
    
    def cross_product(self, otherVector):
        return self.x * otherVector.y - self.y * otherVector.x

    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    

class vector3D(vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    

    



    
v1 = vector2D(3, 4)
v2 = vector2D(1, 2)
print(v1.rotate(90))
print(v1 + v2)
print(v1.magnitude)