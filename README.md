# OrangePi-temp
Control de la temperatura de una Orange Pi con Python, haciendo que un ventilador se encienda automáticamente cuando el microprocesador llegue a una determinada temperatura.

## Requerimientos
Necesitamos tener instalada la librería <a href="https://github.com/duxingkei33/orangepi_PC_gpio_pyH3">orangepi_PC_gpio_pyH3</a>.

Conectamos un relé a los pines 2 y 6 para alimentación y el activador al pin 7 (PA6). Un ventilador que enfríe el micro en la salida normalmente cerrado del relé para que en caso de fallo en la detección o fallo del programa, el ventilador esté activado. De esta manera la Orange Pi no se sobrecalentará, siempre será mejor opción en caso de fallo.

He configurado la temperatura de corte en 45 grados, pero se puede cambiar con la variable temperaturamaxima.

Añade este archivo al arranque.