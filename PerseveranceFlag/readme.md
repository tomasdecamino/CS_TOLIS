# Código del paracídas del Perseverance de la NASA

No intenta reproducir exactamente el paracaídas, sino mostrar como se construye el código de colores...  escondido está el texto "DARE MIGHTY THINGS". Pueden ver el artículo en [TIME magazine que explica](https://time.com/5942177/perseverance-rover-parachute-message/)

El código está escrito en Python, pero utilizando [processing.py](https://py.processing.org/). Se puede mejorar muchísimo, pues la intención es más explicar el algoritmo que generara una replica exacta.

![Flag](https://github.com/tomasdecamino/CS_TOLIS/blob/main/PerseveranceFlag/perseverance.jpg)

Es simplemente el código binario del caracter ascii. Eso si cambian el bit más sifnificativo (de 7) a 0...  el código dice "DARE MIGHTY THINGS".  No reproduje el último anillo, ese se los dejo como reto, pues hay números también

## Retos
- Crear el último anillo del paracaídas (tiene unos números y letras)
- Hacer una interfáz (input box) para poder poner cualquier mensaje en el paracaídas
- Colocar el mensaje en forma de bandera en lugar de paracaídas
