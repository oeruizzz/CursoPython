#print("Hola mundo")

# Input() ingresar datos
#print("Ingrese su nombre")
#x = input() #Este es la funcion imput

#Tipos de variables
#----------------------
# 1. LISTA
x = ["ana", 27, 3, "Hola"]
#----------------------
# 2. STRING MULTILINEA
x = """
Hola
Mundo
"""
#-----------------------

#Errores
#SintaxError
#NameError (Este error sale es cuando el compilador no reconoce una palabra clave o no está definida una variable o funcion)
#ZeroDivisionError (Cuando el resultado de una divisio es cero)

#Potencia **
#Raiz cuadrada ** 0.5
#modulo de una division %
#Mas igual += (Sirve para string y numeros)

###### ATENCIÓN SOLO SE PUEDE CONCATENAR STRING CON STRING ######
### Para concatenar string con numeros hay que usarla funcion str(int) en la variable numerica

print("¿Cómo te llamas?")
name = input()
print("Hola " + name + "!")

print("¿Cuales son tus apellidos?")
lastname = input()


print("Bienvenido " + name + " " + lastname)