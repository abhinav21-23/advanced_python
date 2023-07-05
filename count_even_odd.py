numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9]
c1=0
c2=0
for num in numbers:
    if num % 2 == 0:
        c1+=1
    else:
        c2+=1
print("Number of even numbers:", c1)
print("Number of odd numbers:", c2)
