# Author: Daniel Raymond
# Version: 1.0
# Date: 2023-01-01

# DHT Sensor install reference: https://pypi.org/project/Adafruit-DHT/
# sudo apt-get update sudo apt-get install python3-pip sudo python3 -m pip install --upgrade pip setuptools wheel
# sudo pip3 install Adafruit_DHT
# download library source code: https://github.com/adafruit/Adafruit_Python_DHT/releases
# Then: cd Adafruit_Python_DHT sudo python3 setup.py install

# DHT Sensor Code reference: https://pimylifeup.com/raspberry-pi-humidity-sensor-dht22/
# MariaDB connector installation info: https://mariadb.com/docs/server/connect/programming-languages/python/install/
# MariaDB connector install file: mariadb-connector-python-1.0.11.tar.gz


import datetime
import Adafruit_DHT
import os
import db_connect

from time import sleep
con = db_connect.con
cur = con.cursor(prepared=True) # Get Cursor

DHT_SENSOR = Adafruit_DHT.DHT22
count = 1
DHT_PIN = 4
os.system('clear')


while True:
    if count >= 10:
        os.system('clear') # Clearing the Screen
        count = 1
    now = datetime.datetime.now()
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Current Temperature = {0:0.1f}*C - Humidity level = {1:0.1f}%"
              .format(temperature, humidity) + "  @ " + now.strftime("%Y-%m-%d %H:%M:%S"))
        cur.execute("INSERT INTO temp_reading (crtemp, crhumidity, damper1, damper2, fan, extemp)"
                    "VALUES (%s, %s, 0, 0, 0, 0.0)",(temperature,humidity))
        con.commit()
    else:
        print("Failed to retrieve data from humidity sensor")
    sleep(1800)
    count += 1

con.close()


