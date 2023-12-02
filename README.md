# laboratorio 7
### Estudiante: Frank Wang Wu
### Carné: B57946

## Parte I
En este ejercicio se quiere usar un scripting en bash a scripting en Python, por lo que se realiza los siguientes ajustes para programar.
### Paquetes utilizados
#### 1. `psutil`
Es un paquete de utilidades del sistema que permite obtener información detallada sobre el sistema operativo y los procesos en ejecución. Proporciona una API sencilla y consistente para realizar consultas del sistema.

### Funciones del Script
#### `obtener_informacion_proceso (pid)`
Esta función toma un `pid` (identificador de proceso) como argumento y utiliza `psutil` para recopilar información sobre el proceso correspondiente al `pid` proporcionado. 

#### - `psutil.Process (pid)`:
Crea un objeto `Process` que representa el proceso con el PID proporcionado.

#### - `proceso.name()`: 
Devuelve el nombre del proceso.

#### - `proceso.pid`:
Devuelve el ID del proceso.

#### - `proceso.ppid()`:
Devuelve el ID del proceso padre (PPID).

#### - `proceso.username()`: 
Devuelve el nombre de usuario propietario del proceso.

#### - `proceso.cpu_percent()`:
Devuelve el porcentaje de uso de CPU por parte del proceso.

#### - `proceso.memory_info().rss`: 
Devuelve la cantidad de memoria utilizada por el proceso en bytes.

#### - `proceso.status()`:
Devuelve el estado actual del proceso.

#### - `proceso.exe()`: 
Devuelve la ruta al ejecutable del proceso.

La función construye un diccionario con todas estas informaciones y las devuelve. Si el proceso con el `pid` proporcionado no existe, maneja la excepción `psutil.NoSuchProcess` y devuelve `None`.

### Línea de comandos
Para realizar el scripting en bash usando el comando:
`python3 nombre_script.py 12345` 
