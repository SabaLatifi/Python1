from machine import Pin
import time

led = Pin(15, Pin.OUT)
button = Pin(13, Pin.IN, Pin.PULLUP)

try:
 def send_sos(num_of_sos):
    while True:
        for  in range(numof_sos):
            for  in range(3):
                led.value(1)
                time.sleep(0.5)

            for  in range(3):
                led.value(1)
                time.sleep(1.5)

            for  in range(3):
                led.value(1)
                time.sleep(0.5)
            time.sleep(3)
        break
except:
    pass
