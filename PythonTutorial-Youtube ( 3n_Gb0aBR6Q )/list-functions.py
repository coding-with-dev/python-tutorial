arr_list = ["Spiderman", "Ironman", "Superman", "Batman", "Antman", "Black Panther", "Captain America"]

"""

print(arr_list)

#Print length of list
print(len(arr_list))

#Find Number of occurrence in a list
print(arr_list.count("Antman"))

#Append item at the end of the list
arr_list.append("Captain Marvel")
print(arr_list)

#Insert item at the particular index in a list
arr_list.insert(2, "Flash")
print(arr_list)

arr_list.remove("Antman")
print(arr_list)

arr_list.pop(2)
print(arr_list)
"""

# -------------------------------------------------------------------------------------------------------------- #

for i in arr_list:
    print(i)

arr_list.sort()
print(arr_list)

arr_list.sort(reverse=True)
print(arr_list)
