textData = "Lorem Ipsum is simply dummy text of the printing and typesetting industry"

duplicates = set()
seen = set()

for char in textData:
    if char == " ":
        continue

    if char in seen:
        duplicates.add(char)
    else:
        seen.add(char)

print("".join(duplicates))