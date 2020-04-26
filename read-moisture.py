from gpiozero import MCP3008, Button, LED
from signal import pause
from time import sleep

moisture = MCP3008(channel=0)
button = Button(2)
red_led= LED(15)
green_led = LED(18)

moisture_threshold = 0.1

def get_moisture_value():
    return(moisture.value)

def light_led():
    moisture_value = get_moisture_value()
    print(moisture_value)

    if moisture_value > moisture_threshold:
        green_led.on()
    else:
        red_led.on()

def lights_off():
    # small delay so it's clear the led was on
    sleep(1)
    green_led.off()
    red_led.off()

button.when_pressed = light_led 
button.when_released = lights_off

pause()    
