lines = []
while True:
    line = input("Enter a line (or leave it blank to terminate): ")
    if line == "":
        break
    lines.append(line.lower())
print("Output:")
for line in lines:
    print(line)
