import psutil # paquete para obtener información del sistema
import sys

def obtener_informacion_proceso(pid):
  try:
    proceso = psutil.Process(pid)
    info = {
      # nombre del proceso
      "a) Nombre del proceso": proceso.name(),

      # nombre del proceso
      "b) ID del proceso": proceso.pid,

      # parent process ID
      "c) Parent Process ID": proceso.ppid(),

      # usuario propietario
      "d) Usuario propietario": proceso.username(),

      # porcentaje de uso de CPU al momento de correr el script
      "e) Porcentaje de uso de CPU": proceso.cpu_percent(),

      # consumo de memoria
      "f) Consumo de memoria": proceso.memory_info().rss,

      # estado (status)
      "g) Estado": proceso.status(),

      # path del ejecutable
      "h) Path del ejecutable": proceso.exe()
    }

    return info
  except psutil.NoSuchProcess:
    return None

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Uso : python nombre_script.py <ID_del_proceso>")
  else:
    pid = int(sys.argv[1])
    informacion = obtener_informacion_proceso(pid)
    if informacion:
      for clave, valor in informacion.items():
        print(f"{clave}: {valor}")

    else:
      print(f"No existe ningún proceso con el ID {pid}")
