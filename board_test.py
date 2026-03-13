import time
import board
import digitalio
import mcp3008

PIN = board.D4

print("hello blinky!")

led = digitalio.DigitalInOut(PIN)
led.direction = digitalio.Direction.OUTPUT
adc = mcp3008.MCP3008()

DARK_THRESH = 400
LOUD_THRESH = 400

for i in range(2):
    print("--- LED TEST ---")
    for i in range(5):
        led.value = True
        time.sleep(0.5)
        led.value = False
        time.sleep(0.5)

    print("--- LIGHT SENSOR TEST ---")
    for i in range(50):
        v = adc.read([mcp3008.CH0])[0]
        print(str(v) + ": Bright" if v > DARK_THRESH else ": Dark")
        time.sleep(.1)

    for i in range(4):
        led.value = True
        time.sleep(0.2)
        led.value = False
        time.sleep(0.2)

    print("--- SOUND SENSOR TEST ---")
    for i in range(50):
        led.value = False
        v = adc.read([mcp3008.CH1])[0]
        if v < LOUD_THRESH:
             led.value = True
        print(v)
        time.sleep(.1)

    for i in range(4):
        led.value = True
        time.sleep(0.1)
        led.value = False
        time.sleep(0.1)