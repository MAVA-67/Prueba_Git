# Mi laboratorio de Terminal y Git
Autor: MAVA

MatIA: recuento de pinzas con datos sinteticos.
Ejecucion: python src/recuento_matIA.py
IA: Ayuda para resolver dudas de sintaxis y autocompletado de codigo.

## Comprobacion
He probado los casos coincide, faltan y sobran pinzas.

«Comandos y análisis»

Qué diferencia hay entre > y >>.
Respuesta: >(Sobrescribir) si el archivo existe, vacía su contenido por completo y escribe la nueva salida, si no existe, lo crea
           >>(Añadir o Append) al contrario que > si converva el contenido existente y añade la nueva salida al final del archivo igual que > si no existe, lo crea

Qué hace la tubería |.
Respuesta: La tubería conecta la salida estándar (stdout) de un programa directamente con la entrada estándar (stdin) de otro, sin necesidad de guardar resultados intermedios en el disco.
Tambien nos permite encadenar herramientas modulares ejemplo :cat archivo.txt | grep "error" | wc -l, la salida del primer comando alimenta al segundo, y el resultado de este alimenta al tercero en tiempo real a través de memoria.

Por qué una tijera no aumenta el contador.
Respuesta: El elemento "tijera" no aumenta el contador debido a la condición que hay dentro del bucle del codigo de python for en las líneas 8 y 9:
Primera iteración: instrumento vale "pinza". La condición instrumento == "pinza" es verdadera (True), por lo que observadas pasa de 0 a 1.   Segunda iteración: instrumento vale "tijera". La condición "tijera" == "pinza" es falsa (False), por lo que Python ignora la línea 9 y pasa directamente al siguiente elemento sin sumar nada.   Tercera iteración: instrumento vuelve a ser "pinza". La condición es verdadera y observadas pasa de 1 a 2. 

Qué indican las tres líneas del informe.
Respuesta:   Pinzas esperadas: 2 -> se esperaban 2 pinzas el programa predice la cantidad
             Pinzas observadas: 2 -> se observan 2 pinzas el programa observa la cantidad
             Resultado: coincide -> como las pinzas esperadas y observadas coinciden se cumple y es verídico True

Qué diferencia hay entre guardar un archivo, git add, git commit y git push. 
Respuesta: git add: Pasa las modificaciones seleccionadas al Staging Area (área de preparación). Le indica a Git qué cambios específicos formarán parte de la próxima captura.

git commit: Empaqueta permanentemente los cambios del Staging Area dentro del historial del repositorio local con un identificador único (hash) y un mensaje descriptivo. El cambio ya queda registrado en el historial, pero solo en tu máquina.

git push: Sube los commits locales al servidor o repositorio remoto (como GitHub, GitLab o Azure DevOps) para sincronizar tu trabajo con el resto del equipo o respaldarlo en la nube.
