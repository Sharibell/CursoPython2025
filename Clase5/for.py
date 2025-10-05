'''
Bucle for
'''

for i in [6,8,9,4,7,True,"Hola",[0,1,2]]:
    print(f"Datos: {i}")


print("------")
data=["futbol","Pc",18.6,18,[6,7,10.5],True,False,"Pc"]
for i in data:
    print(f"Datos: {i}")

print("---For Range---")
for i in range(0,20): #range(inicio,fin,salto)
    print(f"Datos: {i}")

print("---While---")
numero=0
while numero < 20:
    print("El numero es:",numero)
    numero+=1 #numero=numero+1