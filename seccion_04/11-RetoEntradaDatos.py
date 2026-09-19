# Reto: Entrada datos
from random import randint

numero_usuario = input('Escribe un número: ')
numero_entero = int(numero_usuario)

numero_secreto = randint(0, 1) # Generamos un valor aleatorio entre 0 y 1

resultado_logico = bool(numero_secreto)

print(f"¿El cofre magico se abre? {resultado_logico}")