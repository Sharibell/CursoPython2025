'''
crea un programa que pida dos numeros y 
obtengan como resultado cual de ellos es 
par o si ambos lo son
'''
num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
if num1 % 2 == 0 and num2 % 2 == 0:
    print("Ambos numeros son pares")
elif num1 % 2 == 0:
    print("El primer numero es par")
elif num2 % 2 == 0:
    print("El segundo numero es par")
else:
    print("Ninguno de los dos numeros es par") 