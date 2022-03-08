from mimetypes import init


class Employee:
    number_employees = 0
    sum_ages = float()
    sum_salary = float()
    average_age = sum_ages * number_employees
    average_salary = sum_salary / number_employees

    # Write your code here
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        Employee.number_employees += 1
        Employee.sum_ages += self.age
        Employee.sum_salary += self.salary
        Employee.average_age = Employee.sum_ages * Employee.number_employees
        Employee.average_salary = Employee.sum_salary / Employee.number_employees


el = Employee("George", 34, 65000)
el = Employee("George", 25, 95000)
print(Employee.average_age)
