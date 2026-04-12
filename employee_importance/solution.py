"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
from typing import List

class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def find_employee(self, employees: List['Employee'], id: int) -> Employee:
        for employee in employees:
            if employee.id == id:
                return employee

    def getImportance(self, employees: List['Employee'], id: int) -> int:
        root_employee = self.find_employee(employees, id)
        number = root_employee.importance

        for employee in root_employee.subordinates:
            # person = self.find_employee(employees, employee)
            # number += person.importance

            number += self.getImportance(employees, employee)


        return number
