import psutil
import subprocess
import sys
import time
import matplotlib.pyplot as plt

def monitorear_proceso(ejecutable):
  # lista para almacenar los datos de uso de CPU y memoria
  cpu_uso = []
  mem_uso = []

  # iniciar el proceso
  proceso = subprocess.Popen(ejecutable)

  # monitorear el proceso cada segundo durante 60 segundos
  for _ in range(60):
    # obtener el porcentaje de uso de CPU y memoria
    cpu_percent = psutil.cpu_percent(interval=1)
    mem_percent = psutil.virtual_memory().percent

    # almacenar los datos en las listas correspondientes
    cpu_uso.append(cpu_percent)
    mem_uso.append(mem_percent)

  # esperar a que el proceso finalice
  proceso.wait()

  # graficar los datos
  plt.figure(figsize=(10,5)) # tamaño de la figura
  plt.plot(cpu_uso, label='Uso de CPU (%)')  # línea para el uso de CPU
  plt.plot(mem_uso, label='Uso de memoria (%)') # línea para el uso de memoria
  plt.xlabel('Tiempo (segundos)') # etiqueta del eje x
  plt.ylabel('Uso (%)') # etiqueta del eje y
  plt.title('Consumor de CPU y Memoria') # título de la gráfica
  plt.legend() # agregar leyenda
  plt.grid(True) # mostrar cuadrícula en la gráfica
  plt.show() # mostrar la gráfica

if __name__ == "__main__":
  # verificar si se proporciona un argumento
  if len(sys.argv) != 2:
    print("Uso: python script.py <ejecutable>")
    sys.exit(1)

  # obtener el ejecutable desde los argumentos de la línea de comandos
  ejecutable = sys.argv[1]

  # llamar a la función para monitorear el proceso
  monitorear_proceso(ejecutable)
