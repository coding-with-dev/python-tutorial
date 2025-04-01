sample = ("Spiderman", "Ironman", "Superman", "Batman", "Antman", "Black Panther", "Captain America", "Antman")
print(type(sample))

#Print length of tuple
print(len(sample))

#Find Number of occurrence in a tuple
print(sample.count("Antman"))

#Convert tuple into list
sample = list(sample)
print(type(sample))

#Append item at the end of the tuple convert into list
sample.append("Captain Marvel")

#Insert item at the particular index in a tuple convert into list
sample.insert(2, "Flash")
print(sample)

sample = tuple(sample)
print(type(sample))