
#String Function Examples
a = "Learn Python Programming with Practical"

#Find length of String
print("Length of a String -> ", len(a))

#Count number of character in a string
print("Count of 'a' into given string -> ", a.count("a"))

#Find Index of a character into a string
print("Index of character -> ", a.index("Python"))

#Find String in a String
print("", a.find("Python"))

#Make Case as Uppercase
print(a.upper())

#Make Case as Lowercase
print(a.lower())

#Make Case as Capitalize
print(a.capitalize())

#Will return string which is suitable for caseless compare
print(a.casefold())

#Make String Center with char around it
print(a.center(100, "-"))