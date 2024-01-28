# Author: Daniel Raymond
# Version: 1.0
# Date: 2023-01-01


import datetime
import Adafruit_DHT
import RPi.GPIO as GPIO
# GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
import os
import db_connect
# import requests
from time import sleep

con = db_connect.con
cur = con.cursor(prepared=True)  # Get Cursor

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4  # from old code - to be removed
damper_1 = (4, 17, 27, 22)  # -> Physical pins (7, 11, 13, 15)
damper_2 = (6, 13, 19, 26)  # -> Physical pins (31, 33, 35, 37)
damper_3 = (12, 16, 20, 21)  # -> Physical pins (32, 36, 38, 40)

temp_sensor_1 = 5   # Physical pin 29
temp_sensor_2 = 18  # Physical pin 12
temp_sensor_3 = 23  # Physical pin 16

water_sensor_mechanic = 24  # Physical pin 18
water_sensor_bedroom = 25  # Physical pin 22

damper_limit_1 = 10  # Physical pin 19
damper_limit_2 = 9  # Physical pin 21
damper_limit_3 = 11  # Physical pin 23


count = 3
os.system('clear')


while count >= 0:
    damper_1_position = 0
    damper_2_position = 0
    damper_3_position = 0

    if GPIO.input(damper_limit_1) != 1:
        GPIO.output(damper_1[count], GPIO.LOW)  # Turn of
        damper_1_position += 1

    if GPIO.input(damper_limit_2) != 1:
        GPIO.output(damper_2[count], GPIO.LOW)  # Turn of
        damper_2_position += 1

    if GPIO.input(damper_limit_3) != 1:
        GPIO.output(damper_3[count], GPIO.LOW)  # Turn of
        damper_3_position += 1

    count -= 1
    sleep(0.02)
    # GPIO.output(damper_1_1[0], GPIO.HIGH)  # Turn off
    # arrayPosition += 1
    # if arrayPosition > 3: arrayPosition = 0
'''
decrease damper location of the three damper until limit is reached while counting the amount of steps ans store 
position in variables.
Set damper back to position based on captured values
'''

while True:
    if count >= 10:
        os.system('clear')  # Clearing the Screen
        count = 1
    now = datetime.datetime.now()
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Current Temperature = {0:0.1f}*C - Humidity level = {1:0.1f}%"
              .format(temperature, humidity) + "  @ " + now.strftime("%Y-%m-%d %H:%M:%S"))
        cur.execute("INSERT INTO temp_reading (crtemp, crhumidity, damper1, damper2, fan, extemp)"
                    "VALUES (%s, %s, 0, 0, 0, 0.0)", (temperature, humidity))
        con.commit()
    else:
        print("Failed to retrieve data from humidity sensor")
    sleep(1800)  # 30 minutes delay
    count += 1

con.close()


def damperRotation(damperName, damperLimit):
    global arrayPosition
    previousPinStatus = None


    while damperLimit > 0:
        if previousPinStatus is not None:
            GPIO.output(damper_1_1[0], GPIO.LOW)  # Turn off

        GPIO.output(damper_1_1[0], GPIO.HIGH)  # Turn off
        arrayPosition += 1
        if arrayPosition > 3: arrayPosition = 0
