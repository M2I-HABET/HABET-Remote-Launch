# HABET Remote Launch Hotwire System Activator Payload CircuitPython Script
# Recieves GPS data and transmits it via LoRa radio module
# Utilizes Adafruit Feather M4 Express, Ultimate GPS FeatherWing, RFM95W 433 MHz FeatherWing
# Last updated 9/2/2020 by Austin Trask

import time
import board
import busio
import digitalio
import analogio
import adafruit_rfm9x

CS = digitalio.DigitalInOut(board.D10)
RESET = digitalio.DigitalInOut(board.D11)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
RADIO_FREQ_MHZ = 433.0
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)
rfm9x.tx_power = 23

button0 = digitalio.DigitalInOut(board.A0)
button0.direction = digitalio.Direction.INPUT
button0.pull = digitalio.Pull.DOWN

while True:

    if button0.value:
        try:
            rfm9x.send("ActivateLaunch")
        except:
            print("Failed to send")
    
    time.sleep(.5)
