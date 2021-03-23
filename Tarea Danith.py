#Ejercicio 1 (0-9)
for n in range(0, 10):
    print(n)

#Ejercicio 2 (100-199)
for a in range(100, 200):
    print(a)

#Ejercicio 3 De 5 en 5, saltando de 3 números
for b in range(5, 21, 3):
    print(b)

#Ejercicio 4 Números correlativos
c = int(input("Digite un número: "))
for c in range(c, c*2):
    print(c)

#Ejercicio 5-6 Listado (Vocales sin repetir)
frase = input("Frase: ")
print("Vocales en la frase:")
for d in "aeiou":
  if d in frase:
    print(d)

#Ejercicio 7 Sumatoria
total = 0
for e in range(101):
    total = total + e
print("Sumatoria:", total)

#Ejercicio 8 Rango
añoInicio=int(input("Año inicial:"))
añoFin=int(input("Año final:"))
for año in range(añoInicio, añoFin+1):
   if not año%10==0:
       continue
   if not año%4==0:
       continue
   if año%100!=0 or año%400==0:
       print(año)

# Ejercicio 9 Factorial
numero=int(input("Número:"))
f=1
if numero!=0:
    for i in range(1,numero+1):
        f=f*i
print("Factorial:", f)

#Ejecicio 10 Fibonacci
n1=0
n2=1
print(n1)
print(n2)
for i in range(8):
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3