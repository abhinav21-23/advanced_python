def check_triangle_type(x, y, z):
    if x == y == z:
        return "Equilateral triangle"
    elif x != y and y != z and z != x:
        return "Scalene triangle"
    else:
        return "Isosceles triangle"
x = float(input("Input length of side x: "))
y = float(input("Input length of side y: "))
z = float(input("Input length of side z: "))
triangle_type = check_triangle_type(x, y, z)
print(triangle_type)
