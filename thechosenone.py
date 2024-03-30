import network
import socket
import urequests as requests
from time import sleep
import ssl
import time
import utime
from machine import Pin, ADC
# set up email server details
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'aayanghosh76@gmail.com'
smtp_password = 'N@N11/1/1/1/'
wifi_ssid = 'RPS-guest'
#wifi_password = 'Welcome$123'
motion_detected = False
# set up recipient's phone number
url = "https://hooks.zapier.com/hooks/catch/18295376/3x2extj/"
# set up sensor pin and threshold
sensor_pin = 34
motion_threshold = 500
i = 0 
# set up buzzer
buzzer_pin = 25
buzzer = Pin(buzzer_pin, Pin.OUT)


def buzz(sec):
    current_time = utime.time()
    while current_time < current_time + sec:
        #buzzer loop
        buzzer.on()
        time.sleep(0.0001)
        buzzer.off()
        i = 0
        break


# set up ADC
adc = ADC(Pin(sensor_pin))

#connects to wifi

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

if sta_if.isconnected() == False:
    sta_if.connect(wifi_ssid)

    while sta_if.isconnected() == False:
        sleep(1)
        print(".", end = "")
while True:
    # read sensor value
    sensor_value = adc.read()
    print(sensor_value)
    if sensor_value > motion_threshold:  
            try:
                if i == 0:
                    print("MOTION DETECTED")
                    r = requests.get(url)
                    print(r.text)
                    i = 1                
                while i == 1:
                    buzz(4)            
            except Exception as e:
                print(e, "error")