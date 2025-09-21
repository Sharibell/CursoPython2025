'''
Entrada de datos en python unida

cadena2= input("Cual es tu proyecto:")

#Forma moderna
print(f"Tu proyecto se llama: {cadena} y es de: {cadena2}")

#Forma antigua
print("Tu proyecto se llama: ",cadena," y es de: ",cadena2)
'''

cadena=input("Como se llama tu proyecto:")
print(f"Tu proyecto es: {cadena}")

#cadena=input("que version es: ")
#print(f"Tu version es: {cadena+1}") #error

cadena=int(input("que version es: "))
print(f"Tu version es: {cadena+1}") #ok
