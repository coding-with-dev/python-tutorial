"""
employeeData = []

#Add New record into employeeData dictionary
name = input("Enter employee name")
dept = input("Enter department name")
sal = input("Enter employee salary")

individualEmp = {
    "name" : name,
    "department": dept,
    "salary": sal
}

employeeData.append(individualEmp)

print(employeeData)
"""

employeeData = [
    {
        'name': 'Devendra',
        'department': 'IT',
        'salary': '10000'
    }
]

"""
#Edit data from dictionary
employeeData = [
    {
        'name': 'Devendra',
        'department': 'IT',
        'salary': '10000'
    }
]

name = input("Enter employee name -> ")
employeeData[0]['name'] = name
print(employeeData)
"""

#Delete data from dictionary
employeeData.pop(0)

print(employeeData)