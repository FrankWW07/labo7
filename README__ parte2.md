# laboratorio 7
### Estudiante: Frank Wang Wu
### Carné: B57946

## Parte II
En este ejercicio, se quiere crear una herramienta para monitorear un proceso, visualizando el estado de un proceso, usando el módulo `os`.

### paquetes usados
#### 1. `os`: 
Proporciona una interfaz para trabajar con funcionalidades dependientes del sistema operativo, permitiendo operaciones de bajo nivel relacionadas con archivos, procesos, etc.

#### 2. `subprocess`: 
Permite generar procesos, conectar tuberías de entrada/salida/error, y obtener sus códigos de salida.

#### 3. `sys`: 
Proporciona acceso a variables y funciones específicas del intérprete de Python y al sistema.

#### 4. `time`: 
Proporciona funciones relacionadas con el tiempo, como pausar la ejecución del programa (`sleep`).

### Funciones del Script
`revisar_proceso(nombre_proceso, ruta_ejecutable)`:
Esta función realiza la verificación continua del estado del proceso especificado. 

#### - Bucle While Infinito: 
Permite que la función se ejecute continuamente para verificar el estado del proceso.

#### - Revisión del Proceso: 
Utiliza `os.popen('ps aux').readlines()` para obtener la lista de procesos en ejecución y busca si el proceso especificado (`nombre_proceso`) está activo.

Si el proceso no se encuentra en la lista de procesos activos, se establece la variable `proceso_encontrado` como `False`.

#### - Volver a Iniciar el Proceso: 
Si no se encuentra el proceso, se muestra un mensaje indicando que el proceso se ha cerrado y se utiliza `subprocess.Popen(['xdg-open', ruta_ejecutable])` para reiniciar el proceso especificado mediante `xdg-open` (asumiendo que `ruta_ejecutable` es la ruta al archivo ejecutable).


El código verifica si el script está siendo ejecutado directamente (no importado como un módulo). Verifica si se proporcionan los argumentos correctos desde la línea de comandos (`sys.argv`). En caso contrario, muestra un mensaje de uso.

### Línea de comandos 
Para realizar el scripting en bash se debe usar el siguiente comando:
`python mi_script.py mi_proceso "python mi_script.py"`

### Resultados 
Los resultados obtenidos al ejecutar el presente script dependiendo del estado del proceso presentará lo siguente:

#### 1. Si el proceso especificado está en ejecución:

- El script monitoreará el proceso continuamente cada minuto (según el intervalo definido).
- No mostrará ninguna salida en la consola, ya que el proceso está en ejecución y no se detectará ningún cierre del mismo.

#### 2. Si el proceso especificado no está en ejecución:

- Cuando el script detecta que el proceso no está en la lista de procesos en ejecución, mostrará el mensaje: "El proceso '{nombre_proceso}' se ha cerrado. Volviendo a levantarlo..."
- Luego, intentará reiniciar el proceso utilizando el comando `subprocess.Popen(['xdg-open', ruta_ejecutable])`. La ruta al ejecutable se debe proporcionar como argumento al script.
- Si el proceso puede reiniciarse correctamente usando `xdg-open`, no se mostrará más información en la consola. Si hay algún problema para reiniciar el proceso, podría mostrar un mensaje de error correspondiente.
