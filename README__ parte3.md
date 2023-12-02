# laboratorio 7
### Estudiante: Frank Wang Wu
### Carné: B57946

## Parte III
En este ejercicio se realiza un script monitoreando el uso del CPU 
y la memoria de un determinado proceso ejecutable, lo cual toma 
como argumento el proceso ejecutable y grafica este con los datos 
en tiempo real.

### Paquetes Utilizados

#### 1. `psutil`: 
Proporciona una interfaz para acceder a información del sistema, 
como el uso de CPU, memoria, etc.

#### 2. `subprocess`: 
Permite generar procesos secundarios y obtener control sobre los mismos.

#### 3. `sys`: 
Proporciona acceso a variables y funciones específicas del intérprete
de Python y al sistema.

#### 4. `time`: 
Ofrece funcionalidades relacionadas con el tiempo, como el intervalo 
de espera (`sleep`).

#### 5. `matplotlib.pyplot`: 
Es una librería para trazar gráficos en Python.

### Funciones del Script

`monitorear_proceso(ejecutable)`

Esta función lleva a cabo el monitoreo del proceso ejecutable pasado 
como argumento.

#### - Listas para almacenar datos: 
Crea listas vacías `cpu_uso` y `mem_uso` para almacenar los datos 
de uso de CPU y memoria, respectivamente.

#### - Iniciar el Proceso: 
Utiliza `subprocess.Popen(ejecutable)` para iniciar el proceso ejecutable.

#### - Monitoreo del Proceso:
- Utiliza un bucle `for` para monitorear el uso de CPU y memoria
cada segundo durante 60 segundos.
- `psutil.cpu_percent(interval=1)` obtiene el porcentaje de uso
de CPU durante el intervalo de 1 segundo.
- `psutil.virtual_memory().percent` obtiene el porcentaje de uso
de memoria RAM.

#### - Almacenamiento de Datos: 
Los valores de uso de CPU y memoria se almacenan en las listas 
`cpu_uso` y `mem_uso` respectivamente.

#### - Esperar a que el Proceso Finalice: 
Utiliza `proceso.wait()` para esperar a que el proceso ejecutable
finalice su ejecución.

#### - Graficar los Datos:

- Utiliza `matplotlib.pyplot` para crear una gráfica.
- `plt.plot(cpu_uso, label='Uso de CPU (%)')` y
`plt.plot(mem_uso, label='Uso de memoria (%)')` trazan las líneas
de uso de CPU y memoria, respectivamente.
- `plt.xlabel`, `plt.ylabel` y `plt.title` configuran las etiquetas
 y el título del gráfico.
- `plt.legend()` agrega una leyenda.
- `plt.grid(True)` agrega una cuadrícula al gráfico.
- `plt.show()` muestra la gráfica.


El código verifica si el script está siendo ejecutado 
directamente (no importado como un módulo). 
Verifica si se proporciona el argumento correcto 
desde la línea de comandos (`sys.argv`). En caso contrario,
muestra un mensaje de uso.

### Línea de comandos
Para realizar el script por medio de la línea de comandos se 
hace lo siguiente: `python script.py /ruta/al/ejecutable`

### Resultados obtenidos
La salida esperada será una gráfica generada por `matplotlib` que 
mostrará dos líneas: una representando el uso de CPU (%) y otra 
representando el uso de memoria (%) a lo largo del tiempo, durante 
los 60 segundos de monitoreo. Esta gráfica proporcionará una 
representación visual del comportamiento del proceso en términos 
de utilización de recursos del sistema.
