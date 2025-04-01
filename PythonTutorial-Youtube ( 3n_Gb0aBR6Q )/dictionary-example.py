studentData = { "name" : "Devendra", "class" : "12th", "rollNo" : 1}

"""
# print dictionary
print(studentData["name"])
print(type(studentData))
"""

"""
#Iterate dictionary 
for x in studentData:
    print(x)
"""


"""
#Iterate dictionary to get values
for x in studentData:
    print(studentData[x])
"""

"""
# get function
print(studentData.get("class"))
"""

"""
# get all keys
print(studentData.keys())
"""

"""
# get all values
print(studentData.values())
"""

"""
# get items wise
print(studentData.items())
for x,y in studentData.items():
    print(x, " -> ", y)
"""