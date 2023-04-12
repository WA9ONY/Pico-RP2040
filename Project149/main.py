from machine import Pin
from utime import sleep

led = Pin(25, Pin.OUT)

while True:
    led.toggle()
    sleep(5)
