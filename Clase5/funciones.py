'''
ejemplo de funciones
'''
def suma(a,b):
    r=a+b
    print(f"sumando dentro de la funcion {a} + {b} = {r}")
    return r

a=5
b=3
resultado=suma(a,b) 
print("---fuera de la funcion---")
print(f"El resultado de la suma es:  {resultado}")
if resultado>5:
    print
    print("El resultado es mayor a 5")
else:
    print("El resultado es menor o igual a 5")
    