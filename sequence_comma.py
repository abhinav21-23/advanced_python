items = []
num = [x for x in input("Enter the binary numbers:\n").split(',')]
for p in num:
    x = int(p, 2)
    if x%5!=0:
        items.append(p)
print(','.join(items))