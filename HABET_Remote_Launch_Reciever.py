# HABET Remote Launch Hotwire System Payload CircuitPython Script
# Recieves GPS data and transmits it via LoRa radio module
# Utilizes Adafruit Feather M4 Express, Ultimate GPS FeatherWing, RFM95W 433 MHz FeatherWing
# Last updated 8/25/2020 by Austin Trask

import time
import board
import busio
import digitalio
import analogio
import adafruit_rfm9x

# Initiate the command for activating the hotwire
hotwire = digitalio.DigitalInOut(board.A5)
hotwire.direction = digitalio.Direction.OUTPUT

CS = digitalio.DigitalInOut(board.D10)
RESET = digitalio.DigitalInOut(board.D11)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
RADIO_FREQ_MHZ = 433.0
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)
rfm9x.tx_power = 23

burn = False

while True:
    packet = rfm9x.receive(timeout=.1)
    if packet is None:
        print("No Packet Yet")
    else:
        try:
            if('ActivateLaunch' in packet):
                hotwire.value = True
                print("We Launching")
                time.sleep(10)
                hotwire.value = False
        except:
            print("Ope")
    time.sleep(.5)
