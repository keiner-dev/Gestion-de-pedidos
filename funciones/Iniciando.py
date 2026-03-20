from .colores import *
import time
import os
import random

def Iniciando():
    print(CYAN + "Iniciando ..." + RESET)
    time.sleep(0.5)
    
    # Conteo regresivo 
    print(VERDE + "3..." + RESET)
    time.sleep(1)
    print(AMARILLO + "2..." + RESET)
    time.sleep(1)
    print(ROJO + "1..." + RESET)
    time.sleep(1)

def cargar():
    print(f"{VERDE}Cargando", end="")
    for _ in range(3):
        time.sleep(random.uniform(0.1, 0.4))
        print(".", end="", flush=True)

def Limpiar_pantalla():
    os.system('clear')