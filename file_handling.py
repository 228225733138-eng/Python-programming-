filename = "sample.txt"

# Write mode creates or overwrites a file.
with open(filename, "w", encoding="utf-8") as file:
    file.write("Python file handling\n")

# Read mode reads the file.
with open(filename, "r", encoding="utf-8") as file:
    print(file.read())

# Append mode adds to the end of the file.
with open(filename, "a", encoding="utf-8") as file:
    file.write("Appended line\n")
