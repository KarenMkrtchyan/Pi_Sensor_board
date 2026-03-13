import time
import board
import digitalio
import mcp3008

PIN = board.D4

print("hello blinky!")

led = digitalio.DigitalInOut(PIN)
led.direction = digitalio.Direction.OUTPUT
adc = mcp3008.MCP3008()

while True:
    # LED test
    for i in range(5):
        led.value = True
        time.sleep(0.5)
        led.value = False
        time.sleep(0.5)

    # Light sensor test
    for i in range(50):
        print(adc.read([mcp3008.CH0]))
        time.sleep(.1)

    for i in range(4):
        led.value = True
        time.sleep(0.2)
        led.value = False
        time.sleep(0.2)
    # Sound sensor test
    for i in range(50):
        print(adc.read([mcp3008.CH1]))
        time.sleep(.1)

    for i in range(4):
        led.value = True
        time.sleep(0.1)
        led.value = False
        time.sleep(0.1)