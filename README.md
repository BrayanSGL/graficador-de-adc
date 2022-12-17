# Graficador de ADC en python

Este proyecto consiste en la comunicación entre una tarjeta Nucleo L476RG y una computadora a través del puerto serie. La tarjeta Nucleo envía continuamente la lectura del potenciómetro y la computadora muestra un gráfico de la señal en tiempo real. Además, la computadora puede enviar comandos a la tarjeta Nucleo para encender o apagar los LEDs verde y rojo.

## Requisitos
Para poder ejecutar este proyecto es necesario tener:

- Una tarjeta Nucleo L476RG
- Una computadora con puerto serie y conexión USB
- Un potenciómetro
- Dos LEDs (verde y rojo)
- Una resistencia de 220 Ohmios para cada LED
- Cables para conectar los componentes

## Cómo ejecutar el proyecto
1. Conecte la tarjeta Nucleo a la computadora a través del cable USB.
2. Abra el archivo main.cpp en el IDE de su elección y cargue el código en la tarjeta Nucleo.
3. Conecte el potenciómetro a los pines A5 y GND de la tarjeta Nucleo.
4. Conecte los LEDs a los pines D6 y D7 de la tarjeta Nucleo, utilizando las resistencias de 220 Ohmios como limitadores de corriente.
5. Abra el archivo main.py en un entorno de Python y ejecútelo.
6. Ajuste los límites superior e inferior del gráfico con las barras deslizantes y observe cómo los LEDs se encienden o apagan según el valor del potenciómetro.

## Código
El código de la tarjeta Nucleo se encuentra en el archivo `main.cpp`. Se utiliza la librería mbed para manejar la comunicación serie y controlar los LEDs. La lectura del potenciómetro se realiza a través del pin A5 y se convierte a un valor en el rango de -250 a 250 antes de enviarlo a través del puerto serie.

El código para la computadora se encuentra en el archivo `main.py`. Se utiliza la librería serial para leer y escribir en el puerto serie, y la librería tkinter para crear la interfaz gráfica de usuario (GUI). Se utiliza un hilo (thread) para actualizar la lectura del potenciómetro y el gráfico en tiempo real.

## Licencia
Este proyecto está licenciado bajo la licencia MIT.
