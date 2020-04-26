from gpiozero import MCP3008
import time

moisture = MCP3008(channel=0)

while True:
    time.sleep(1)
    print(moisture.value)