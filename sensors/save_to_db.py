import mysql.connector
from sensors.read_sensors import read_sensors
from config import DB_HOST, DB_USER, DB_PASS, DB_NAME

def save_to_db():
    data = read_sensors()
    conn = mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME)
    cursor = conn.cursor()
    sql = "INSERT INTO sensor_data (temperature, humidity, soil_moisture) VALUES (%s, %s, %s)"
    cursor.execute(sql, (data["temperature"], data["humidity"], data["soil_moisture"]))
    conn.commit()
    cursor.close()
    conn.close()
    print("Data berhasil disimpan ke database.")

if __name__ == "__main__":
    save_to_db()
