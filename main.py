from machine import Pin

led = Pin(2, Pin.OUT) # Led integrato del ESP32
sensore = Pin(21, Pin.IN) # Sensore collegato al PIN 21

NERO = 0

while True:
    stato = sensore.value()
    if stato == NERO:
        led.value(0)
        print("Led spento")
    else:
        led.value(1)
        print("Led acceso")