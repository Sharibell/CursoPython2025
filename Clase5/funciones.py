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
