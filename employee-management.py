class Employee:
    company_name = "Age of Dragons, Inc."
    total_employees = 0
    
    def __init__(self, first_name, last_name, id, position, salary):
        
        self.total_employees = self.total_employees + 1
        
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.position = position
        self.salary = salary

    def get_name(self):
        return f"{self.first_name } {self.last_name}"

