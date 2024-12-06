import os
import time

inicio = time.time()

# Se considera que el script a ejecutar está en el mismo directorio
# en que se encuenta este script y no importa si el directorio 
# de trabajo no coincide con el directorio desde donde se corre
os.system(f'python3 {os.path.dirname(__file__)}/024.py')

fin  = time.time()

tiempo_total = fin - inicio

print(f"Tiempo de ejecución: {tiempo_total:.5f} segundos")

