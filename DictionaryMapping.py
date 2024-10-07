employees_to_departments = {
    "John": "HR",
    "Levi": "RD",
    "Anna": "Marketing",
    "Bob": "RD",
    "Cathy": "HR",
    "David": "Finance",
    "Eve": "Marketing",
    "Frank": "Finance",
    "Grace": "HR",
    "Hank": "RD"
}

departments_to_employees = {}

for key, value in employees_to_departments.items():
    if value not in departments_to_employees:
        departments_to_employees[value] = []
    departments_to_employees[value].append(key)
print(departments_to_employees)