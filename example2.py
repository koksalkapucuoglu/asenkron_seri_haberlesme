import serial
import time

from pyA20.gpio import gpio
from pyA20.gpio import port


gpio.init()

led = port.PD14

gpio.setcfg(led,gpio.OUTPUT)

ser=serial.Serial('/dev/ttyS1',9600)
ser.flushInput()
ser.write(b'\n2 kategorimiz var.Bunlardan birini seciniz\n1-)1 sn araliklarla led yakma\n2-)flash led yakma')
print ("Seri Haberlesme basliyor\n")

while 1:
        ser.flushInput()
        ser.write(b'\n\nLutfen bir kategori secin: ')
        secenek=ser.read().decode()

        if secenek == '1':
                ser.write(b"\nLed 1 saniye araliklarla yaniyor\n")
                for counter in range(10):
                        gpio.output(led,1)
                        time.sleep(1)
                        gpio.output(led,0)
                        time.sleep(1)
                ser.write(b"\nLed sondu\n")
        elif secenek == '2':
                ser.write(b"\nLed 0.1 saniye araliklarla yaniyor\n")
                for counter in range (50):
                        gpio.output(led,1)
                        time.sleep(0.1)
                        gpio.output(led,0)
                        time.sleep(0.1)
                ser.write(b"\nLed sondu\n")
        else:

                ser.write(b'\nBoyle bir kategori bulunamamistir.\n1-)1 sn araliklarla led yakma \n2-)flash led yakma\n')

