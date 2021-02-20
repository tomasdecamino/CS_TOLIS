# Ejemplo de verificación de error en mensaje con ParityCheck

Un ejemplo sencillo de parity check para enviar mensajes y que el receptor detecte si hay un error en el mensaje.  Se requieren 2 MicroBits, uno ejecuta el código de sender.py, y el otro de receiver.py.  En el "sender" se presiona el botón A para enviar el mensaje, antes de enviarlo lo prepara haciendo "Parity", es decir, si hay un número impar de '1', agrega un '1' al final, y si ya hay un número par de '1', entonces agrega un '0'. El mensaje es recibido por el "receiver", que verifica la paridad, es decir, siempre deben venir un número par de 'bits'

![Sender-Receiver](https://github.com/tomasdecamino/CS_TOLIS/blob/main/ParityMicroBit/microbit%20parity1.png)

Si se presiona el botón B al mismo tiempo que el A, agrega un bit de error.  El receiver si el mensaje con cumple con un número par de 1, determina que el mensaje está corrupto y vuelve a pedir el mensaje al "sender".

![Sender-Receiver-Error](https://github.com/tomasdecamino/CS_TOLIS/blob/main/ParityMicroBit/microbit%20parity2.png)

Acá hay un [video](https://youtu.be/2qlANkPDRks) que muestra como funciona

## Retos

- Enviar mensajes más largos
- Enviar textos como "Hello World"

## Recursos adicionales

Para entender mejor la corrección de errores, recomiendo ver este video de [Computerphile](https://youtu.be/-15nx57tbfc)


