# 1002 
R = float(input())
π = 3.14159

A = π * R ** 2

print(f"A={A:.4f}")

# 1005
A = float(input())
B = float(input())

media = (A * 3.5 + B * 7.5) / 11

print(f"MEDIA = {media:.5f}")


#1010
total = 0
for i in range(2):
    item = input().split(" ")
    code = int(item[0])
    qt = int(item[1])
    value = float(item[2])
    total = total + qt * value

print(f"VALOR A PAGAR: R$ {total:.2f}")

#1012
values = input().split(" ")
A = float(values[0])
B = float(values[1])
C = float(values[2])
pi = 3.14159

triangulo = (A * C) / 2
circulo = pi * C ** 2
trapezio = (A + B) * C / 2
quadrado = B * B
retangulo = A * B


print(f"TRIANGULO: {triangulo:.3f}")
print(f"CIRCULO: {circulo:.3f}")
print(f"TRAPEZIO: {trapezio:.3f}")
print(f"QUADRADO: {quadrado:.3f}")
print(f"RETANGULO: {retangulo:.3f}")

#1013
A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)

maiorAB = (A + B + abs(A - B)) / 2
maior = (maiorAB + C + abs(maiorAB - C)) / 2
print(f"{maior:.0f} eh o maior")

#1014
X = int(input())
Y = float(input())

total = X / Y

print(f"{total:.3f} km/l")

#1015
import math

values = input().split()
x1 = float(values[0])
y1 = float(values[1])

values2 = input().split()
x2 = float(values2[0])
y2 = float(values2[1])

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


print(f"{distance:.4f}")

#1016 
value = int(input())

value = value * 2

print(f"{value} minutos")

#1017
X = int(input())
Y = int(input())

total = X * Y / 12

print(f"{total:.3f}")  

# 1018
value = int(input())

print(value)
notas100 = value / 100
value = value % 100

notas50 = value / 50
value = value % 50

notas20 = value / 20
value = value % 20

notas10 = value / 10
value = value % 10

notas5 = value / 5
value = value % 5

notas2 = value / 2
value = value % 2

notas1 = value / 1
value = value % 1

print(f"{int(notas100)} nota(s) de R$ 100,00")
print(f"{int(notas50)} nota(s) de R$ 50,00")
print(f"{int(notas20)} nota(s) de R$ 20,00")
print(f"{int(notas10)} nota(s) de R$ 10,00")
print(f"{int(notas5)} nota(s) de R$ 5,00")
print(f"{int(notas2)} nota(s) de R$ 2,00")
print(f"{int(notas1)} nota(s) de R$ 1,00")

#1019
N = int(input())

hour = N / 3600
N = N % 3600

minutes = N / 60
N = N % 60

seconds = N

print(f"{int(hour)}:{int(minutes)}:{int(seconds)}")


#1035
value = input().split(" ")
A = int(value[0])
B = int(value[1])
C = int(value[2])
D = int(value[3])

CD = C + D
AB = A + B

if B > C and D > A and CD > AB and C > 0 and D > 0 and A % 2 == 0:
    print("valores aceitos")
else:
    print("valores nao aceitos")

# 1036
import math

value = input().split(" ")
A = float(value[0])
B = float(value[1])
C = float(value[2])

discriminant = B ** 2 - 4 * A * C

if A == 0 or discriminant < 0:
    print("Impossivel calcular")

else:
    R1 = (-B + math.sqrt(discriminant)) / (2 * A)
    R2 = (-B - math.sqrt(discriminant)) / (2 * A)

    print(f"R1 = {R1:.5f}")
    print(f"R2 = {R2:.5f}")

value = float(input())

if value < 0 or value > 100.00:
    print("Fora de intervalo")
elif value <= 25.00:
    print("Intervalo [0,25]")
elif value <= 50.00:
    print("Intervalo (25,50]")
elif value <= 75.00:
    print("Intervalo [50,75]")
elif value <= 100.00:
    print("Intervalo (75,100]")


# STORAGE
print(value)
print(f"{} nota(s) de R$ 100,00")
print(f"{} nota(s) de R$ 50,00")
print(f"{} nota(s) de R$ 20,00")
print(f"{} nota(s) de R$ 10,00")
print(f"{} nota(s) de R$ 5,00")
print(f"{} nota(s) de R$ 2,00")
print(f"{} nota(s) de R$ 1,00")

print("MOEDAS:")
print(f"{m_1} moeda(s) de R$ 1.00")
print(f"{m_050} moeda(s) de R$ 0.50")
print(f"{m_025} moeda(s) de R$ 0.25")
print(f"{m_010} moeda(s) de R$ 0.10")
print(f"{m_005} moeda(s) de R$ 0.05")
print(f"{m_001} moeda(s) de R$ 0.01")