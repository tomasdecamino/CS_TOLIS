# Leer datos de puerto serial de un Micro:Bit

## Introducción
Este código sencillo muestra como obtener datos del puerto serial, enviado por un [Micro:Bit](https://microbit.org/). El ejemplo es lo más sencillo posible para demostrar el uso, y que a partir de acá, se pueden hacer muchas aplicaciones con lectura de sensores en el Micro:Bit para desplegar visualmente en [Processing.py](https://py.processing.org/).

Esta cambinación es ideal para la enseñanza de un solo lenguaje de programación (Python) que se utiliza en ambas plataformas, y hace los proyectos mucho más escalables.

Se incluye el código de processing.py y el de micropython para el Micro:Bit.

En el código de processing.py, las líneas

```python
    println(Serial.list())
    myPort = Serial(this,Serial.list()[5], 115200)
```
Para determinar en cual puerto serial se muestran la lista de conexiones seriales, de allñí el ususario debe indicar en posición de la lista, está el microbit. Así por ejemplo en MacOSX y Linux es algo como "/dev/tty.usbmodem142402", en PC sería el COM.

## ¿Qué hace el código?
A partir del acelerómetro del microbit, se pasa la infromación del eje x por serial, el cual es usado en processig.py para mover un círculo.  La intención del código es mostrar el uso de lectura de puerto serial de la forma más sencilla posible.

##  Retos
- Hacer un video juego tipo "pong"
- Usar el eje y del microbit junto con el eje x (debe mandar dos datos separado por coma y al recibirlos se deben separar o "split")
- Usar colores u otras formas o imagenes
