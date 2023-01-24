# Author: Daniel Raymond
# Version: 1.0
# Date: 2023-01-01


import mariadb
import sys


try:
    con = mariadb.connect(
        user="coder",
        password="#Coding!Spree#",
        host="localhost",
        port=3306,
        database="tempdata"
    )
except mariadb.Error as ex:
    print(f"An error occurred while connecting to MariaDB: {ex}")
    sys.exit(1)
