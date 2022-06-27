a = int(input("Geef een getal tussen de 0 en 10:"))
b = int(input("Geef een getal tussen de 0 en 10:"))

while a > 10 or a < 0:
    a = int(input("Geef een getal tussen de 0 en 10:"))
while b > 10 or b < 0:
    b = int(input("Geef een getal tussen de 0 en 10:"))
    

if a >= b:
    print(a, "+", b, "=", a + b)
    print(a, "-", b, "=", a - b)
    print(a, "*", b, "=", a * b)
    print(a, "/", b, "=", a / b)
    print("v", a, "=", a ** 0.5)
    print("v", b, "=", b ** 0.5)
    print(a, "^", "2", "=", a ** 2)
    print(b, "^", "2", "=", b ** 2)
    print(a, "^", b, "=", a ** b)
    
if b > a:
    print(b, "+", a, "=", b + a)
    print(b, "-", a, "=", b - a)
    print(b, "*", a, "=", b * a)
    print(b, "/", a, "=", b / a)
    print("v", b, "=", b ** 0.5)
    print("v", a, "=", a ** 0.5)
    print(b, "^", "2", "=", b ** 2)
    print(a, "^", "2", "=", a ** 2)
    print(b, "^", a, "=", b ** a)
    