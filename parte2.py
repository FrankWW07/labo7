import os
import subprocess
import sys
import time

def revisar_proceso(nombre_proceso, ruta_ejecutable):
  while True:
    # Revisar si el proceso está activo
    proceso_encontrado = False
    for line in os.popen('ps aux').readlines():
      if nombre_proceso in line:
        proceso_encontrado = True
        break

    if not proceso_encontrado:
      # Si el proceso se cierra, volver a levantarlo
      print(f"El proceso '{nombre_proceso}' se ha cerrado. Volviendo a levantarlo...")
      subprocess.Popen(['xdg-open', ruta_ejecutable])


    # intervalo de tiempo para revisar el estado del proceso (en segundos)
    tiempo_espera = 60 # revisar cada minuto

    # Esperar antes de volver a revisar el estado del proceso
    time.sleep(tiempo_espera)

if __name__ == "__main__":
  if len(sys.argv) != 3:
    print("Uso: python script.py <nombre_proceso> <comando>")
    sys.exit(1)

  nombre_proceso = sys.argv[1]
  ruta_ejecutable = sys.argv[2]

  revisar_proceso(nombre_proceso, ruta_ejecutable)
