import mysql.connector
import json
import os
with open("./config.json") as f:
    global_config = json.load(f)
current_directory = os.path.dirname(os.path.abspath(__file__))
config = {
    'user': global_config["user"],
    'password': global_config["password"],
    'host': global_config["host"],
    'port': global_config["port"],
    'database': global_config["database"],
    'ssl_ca': os.path.join(current_directory,'server-ca-2.pem'),
    'ssl_cert': os.path.join(current_directory,'client-cert.pem'),
    'ssl_key': os.path.join(current_directory,'client-key.pem') 
}

try:
    connection = mysql.connector.connect(**config)
    print("Connected to MySQL database")

    cursor = connection.cursor()
    cursor.execute("SHOW TABLES")
    for table in cursor.fetchall():
        print(table)

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed")
