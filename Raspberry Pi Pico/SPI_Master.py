from machine import Pin, SPI

# Guía de Conexiones
"""
Raspberry Pi Pico (Maestro)          Dispositivo Esclavo
--------------------------------     -------------------
SCK (Pin 2) -----------------------> SCK
MOSI (Pin 3) ----------------------> MOSI
MISO (Pin 4) <---------------------- MISO
CS (Pin 5) ------------------------> CS
GND -------------------------------- GND
"""

# Nota: Aunque la Raspberry Pi Pico tiene capacidad UART,
# en este programa, la comunicación se realiza utilizando
# la consola de Thonny, no a través de UART.

"""
Parece que para poder hacer una conexión desde terminal
hacia la rasp necesito hacer una conexión usando los pines
propiamente de UART, y no se puede hacer directamente
por USB.
Parece que para esto tal vez necesitaría tener un debugger
"""

# Configuración de SPI
spi = SPI(0, baudrate=1000000, polarity=0, phase=0, bits=8, firstbit=SPI.MSB,#
          sck=Pin(2), mosi=Pin(3), miso=Pin(4))

# Configuración del pin Chip Select (CS)
cs = Pin(5, mode=Pin.OUT)

def send_spi_data(data):
    cs.value(0)  # Baja el pin CS para seleccionar el dispositivo SPI
    spi.write(data)  # Envía el dato por SPI
    cs.value(1)  # Sube el pin CS para deseleccionar el dispositivo SPI

while True:
    data = input("Escribe un dato: ")  # Lee el dato desde la consola de Thonny
    print("Dato recibido desde terminal:", data)  # Imprime el dato en la consola
    send_spi_data(data.encode('utf-8'))  # Envía el dato convertido a bytes por SPI
    print("Dato enviado:", data)
    