from board import Board
#from display import Display
from ewh_net import Network
from machine import Pin
#import time

network = Network()
network.connect()
print(network.ip)
print(network.mac)

board = Board()

board.init_ssd1306i2c(
    reset_pin=board.init_pin(21, "Display Reset", Pin.OUT),
    scl_pin=board.init_pin(18, "Display SCL"),
    sda_pin=board.init_pin(17, "Display SDA"),
)

board.display.text("Moin", 1)