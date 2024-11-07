import mysql.connector
import json
import os
with open("./config.json") as f:
    global_config = json.load(f)
current_directory = os.path.dirname(os.path.abspath(__file__))
import base64
import tempfile

# Decode and save each certificate to a temporary file
def decode_and_save_to_tempfile(encoded_content, suffix):
    # Decode the Base64 content
    decoded_content = base64.b64decode(encoded_content)
    
    # Create a temporary file and write the decoded content
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
    temp_file.write(decoded_content)
    temp_file.close()
    
    return temp_file.name

# Get environment variables
ssl_ca_encoded = os.environ['SERVER_CA']
ssl_cert_encoded = os.environ['CLIENT_CERT']
ssl_key_encoded = os.environ['CLIENT_KEY']

# Decode each certificate and save it to a temporary file
ssl_ca_file = decode_and_save_to_tempfile(ssl_ca_encoded, ".pem")
ssl_cert_file = decode_and_save_to_tempfile(ssl_cert_encoded, ".pem")
ssl_key_file = decode_and_save_to_tempfile(ssl_key_encoded, ".pem")
config = {
    'user': global_config["user"],
    'password': global_config["password"],
    'host': global_config["host"],
    'port': global_config["port"],
    'database': global_config["database"],
    'ssl_ca': ssl_ca_file,
    'ssl_cert': ssl_cert_file,
    'ssl_key': ssl_key_file 
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
