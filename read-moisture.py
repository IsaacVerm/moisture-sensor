from gpiozero import MCP3008, Button
from signal import pause

moisture = MCP3008(channel=0)
button = Button(2)

def print_moisture_value():
    print(moisture.value)

button.when_pressed = print_moisture_value

pause()    
