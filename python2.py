import math

print("Завдання 1: Обчислення площ трьох прямокутників")
for i in range(1, 4):
    a = float(input(f"Введіть сторону a прямокутника {i}: "))
    b = float(input(f"Введіть сторону b прямокутника {i}: "))
    area = a * b
    print(f"Площа прямокутника {i}: {area}")

def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

print("\nЗавдання 2: Гіпотенузи двох прямокутних трикутників")
a1 = float(input("Катет a1: "))
b1 = float(input("Катет b1: "))
a2 = float(input("Катет a2: "))
b2 = float(input("Катет b2: "))

h1 = hypotenuse(a1, b1)
h2 = hypotenuse(a2, b2)

print(f"Гіпотенуза 1: {h1:.2f}")
print(f"Гіпотенуза 2: {h2:.2f}")
if h1 > h2:
    print("Гіпотенуза 1 більша")
elif h1 < h2:
    print("Гіпотенуза 2 більша")
else:
    print("Гіпотенузи рівні")

def is_inside_circle(x, y, a, b, R):
    return (x - a)**2 + (y - b)**2 < R**2

print("\nЗавдання 3: Точки і коло")
a = float(input("Введіть a (центр кола по x): "))
b = float(input("Введіть b (центр кола по y): "))
R = float(input("Введіть R (радіус кола): "))

p1 = float(input("Координата р1 (x точки P): "))
p2 = float(input("Координата р2 (y точки P): "))
f1 = float(input("Координата f1 (x точки F): "))
f2 = float(input("Координата f2 (y точки F): "))
l1 = float(input("Координата l1 (x точки L): "))
l2 = float(input("Координата l2 (y точки L): "))

count_inside = 0
for x, y, name in [(p1, p2, 'P'), (f1, f2, 'F'), (l1, l2, 'L')]:
    if is_inside_circle(x, y, a, b, R):
        print(f"Точка {name} лежить всередині кола.")
        count_inside += 1
    else:
        print(f"Точка {name} не лежить всередині кола.")
print(f"Кількість точок всередині кола: {count_inside}")

print("\nЗавдання 4: Площа чотирикутника (з прямим кутом)")
X = float(input("X: "))
Y = float(input("Y: "))
Z = float(input("Z: "))
T = float(input("T: "))

area1 = (X * Y) / 2  
area2 = (Z * T) / 2 
total_area = area1 + area2
print(f"Площа чотирикутника: {total_area}")

print("\nЗавдання 5: Числа, що діляться на всі задані")
n = int(input("Введіть n: "))
divs = input("Введіть дільники через пробіл: ").split()
divs = [int(x) for x in divs if int(x) != 0]

print("Числа, що діляться на всі задані дільники:")
for i in range(1, n + 1):
    if all(i % d == 0 for d in divs):
        print(i, end=' ')
print()