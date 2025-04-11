from flask import Flask, render_template, request, jsonify
from api.pump_control import siram
from api.save_to_db import save_sensor_data
from api.read_sensors import get_sensor_data
from api.telegram_alert import send_telegram_alert

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/sensor-data')
def sensor_data():
    data = get_sensor_data()
    return jsonify(data)

@app.route('/api/siram', methods=['POST'])
def siram_tanaman():
    siram()
    send_telegram_alert("Penyiraman dimulai otomatis/manual.")
    return jsonify({"message": "Penyiraman dimulai"})

@app.route('/api/set-jadwal', methods=['POST'])
def set_jadwal():
    waktu = request.json.get("waktu")
    print(f"Jadwal penyiraman otomatis diatur ke: {waktu}")
    # Simpan ke file/jadwal
    return jsonify({"message": "Jadwal disimpan"})

if __name__ == '__main__':
    app.run(debug=True)
