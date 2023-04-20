# Project 149 code from ChatGPT
import machine
import utime

led = machine.Pin(25, machine.Pin.OUT)  # Set Pin 25 as output

while True:
    led.value(1)  # Turn on the LED
    utime.sleep(0.5)  # Wait for 500ms
    led.value(0)  # Turn off the LED
    utime.sleep(0.5)  # Wait for 500ms


