# Author: Daniel Raymond
# Version: 1.0
# Date: 2023-01-01


import mysql.connector
import sys


try:
    con = mysql.connector.connect(
        user="coder",
        password="(#Coding!Spree#)",
        host="192.168.0.21",
        port=3306,
        # database="tempdata"
        database="tempdata"
    )
except mysql.connector.Error as ex:
    print(f"An error occurred while connecting to MariaDB: {ex}")
    sys.exit(1)
