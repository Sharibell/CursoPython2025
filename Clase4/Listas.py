'''
introduccion a las listas en python
'''
#definicion de una lista
array=["futbol","Pc",18.6,18,[6,7,10.5],True,False,"Pc"]
print(array)
#acceso a un elemento de la lista
print(array[0])

print("pc" in array)
print(array.index("futbol"))

print(array.count("Pc"))

array.clear()
print("Array",array)
array=["futbol","Pc",18.6,18,[6,7,10.5],True,False,"Pc"]
array.reverse() #invierte el orden de la lista
print("Array Invertido",array)