class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __add__(self, otherEmployee):
        if isinstance(otherEmployee, Employee):
            return Employee(f"{self.name} + {otherEmployee.name}", self.salary + otherEmployee.salary)
        else:
            return NotImplemented
        
    def __sub__(self, otherEmployee):
        if isinstance(otherEmployee, Employee):
            if otherEmployee.salary != self.salary:
                result = otherEmployee.name if otherEmployee.salary > self.salary else self.name
            else:
                print("Both have equal salary")
                return Employee(f"Comapare {self.name} - {otherEmployee.name}", self.salary-otherEmployee.salary)
            print(f"{result} have more salary by {abs(self.salary - otherEmployee.salary)}")
            return Employee(f"Comapare {self.name} - {otherEmployee.name}", abs(self.salary - otherEmployee.salary))
        else:
            return NotImplemented
        
        
    def __str__(self):
        return f"Name: {self.name}, Salary: {self.salary}"

emp1 = Employee("Rahul", 500000)
emp2 = Employee("Adarsh", 500000)
print(emp1 - emp2)
print(emp1 + emp2)

emp3 = Employee("Raj", 100000)
emp4 = Employee("Sohan", 80000)
print(emp1 + emp4)
print(emp3 + emp4)
print(emp3 - emp4)