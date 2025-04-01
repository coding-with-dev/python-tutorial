employeeData = [
    {
        'name': 'Arun',
        'department': 'IT',
        'salary': 20000
    },
    {
        'name': 'Bhuvan',
        'department': 'Operations',
        'salary': 18000
    },
    {
        'name': 'Chetan',
        'department': 'Finance',
        'salary': 13500
    }
]

for x in employeeData:
    newSalary = x['salary'] + ( x['salary'] * 0.10 )
    x['salary'] = float(newSalary)

print(employeeData)

