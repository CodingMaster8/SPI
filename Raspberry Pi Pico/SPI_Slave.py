from machine import Pin, SPI

# Guía de Conexiones
"""
Dispositivo Maestro     Dispositivo Esclavo
-------------------     -------------------
SCK ------------------> SCK (Pin 2)
MOSI  ----------------> MISO (Pin 4)
MISO  <---------------- MOSI (Pin 3)
CS -------------------> CS (Pin 5)
GND ------------------- GND
"""

# Configuración de SPI para el esclavo
spi = SPI(0, baudrate=1000000, polarity=0, phase=0, bits=8, firstbit=SPI.MSB,
          sck=Pin(2), mosi=Pin(3), miso=Pin(4))

# Configuración del pin Chip Select (CS) como entrada
cs = Pin(5, mode=Pin.IN)

def read_spi_data():
    # El esclavo no tiene un pin CS activo, se usa la función read() para leer datos.
    # Parece que con esto, todos los esclavos leen el dato
    if not cs.value():  # Verifica si el pin CS está bajo (activo)
        data = spi.read(255)  # Lee hasta 255 bytes de SPI (ajustar si es necesario)
        return data
    return None

while True:
    data = read_spi_data()
    if data:
        print("Dato recibido por SPI:", data.decode('utf-8'))  # Imprime el dato recibido en la consola