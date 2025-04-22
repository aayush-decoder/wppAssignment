class Convertor:
    def __init__(self, magnitude: int, unit: str):
        self.magnitude = magnitude
        self.unit = unit

    @property
    def baseUnit(self):
        if self.unit == "cm":
            return self.magnitude
        elif self.unit == "meter":
            return self.magnitude*100
        elif self.unit == "yards":
            return self.magnitude*91.44
        elif self.unit == "feet":
            return self.magnitude*30.48
        elif self.unit == "inches":
            return self.magnitude*2.54
        elif self.unit == "miles":
            return self.magnitude*160934.4
        elif self.unit == "kilometer":
            return self.magnitude*100*1000
        elif self.unit == "millimeter":
            return self.magnitude/10
        
    def feet(self):
        return self.baseUnit *0.394
    
    def miles(self):
        return self.baseUnit * (6.214/10**6)
    
    def inches(self):
        return self.baseUnit * 0.394
    
    def yards(self):
        return self.baseUnit * 0.0109
    
    def kilometer(self):
        return self.baseUnit / 100000
    
    def millmeter(self):
        return self.baseUnit * 10
    
    def centimeter(self):
        return self.baseUnit
        
convertor = Convertor(1000, "meter")
print(convertor.kilometer())
print(convertor.millmeter())
print(convertor.centimeter())
print(convertor.feet())
print(convertor.miles())
        
        