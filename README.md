# **🌱 Smart Irrigation System - IoT-Based Automatic Plant Watering System**  

## **📌 Deskripsi Proyek**  
Proyek ini adalah sistem penyiraman tanaman otomatis berbasis IoT menggunakan **Python** dan **Raspberry Pi**. Sistem ini mengontrol penyiraman tanaman berdasarkan data dari berbagai sensor dan dapat dimonitor serta dikendalikan melalui **Grafana** atau **Node-RED**.  

🚀 **Fitur utama:**  
✅ Mode **Manual & Otomatis** untuk penyiraman tanaman  
✅ Sensor **kelembaban tanah, suhu, kelembaban udara, cahaya, pH, dan hujan**  
✅ **Notifikasi ke Telegram** jika kelembaban tanah rendah  
✅ **Data tersimpan ke MySQL/Firebase** untuk analisis jangka panjang  
✅ **Live monitoring dengan kamera** (Opsional: Modul kamera Raspberry Pi)  
✅ **AI untuk prediksi penyiraman** menggunakan Machine Learning  
✅ **Grafana & Node-RED** untuk visualisasi data real-time  
✅ **Daya hemat energi** dengan panel surya  

---

## **🛠️ 1. Teknologi yang Digunakan**  
| Teknologi | Deskripsi |
|-----------|-----------|
| **Python** | Bahasa utama untuk membaca sensor & mengontrol pompa |
| **Raspberry Pi** | Hardware utama untuk menjalankan sistem |
| **MySQL / Firebase** | Penyimpanan data sensor |
| **Grafana** | Visualisasi data sensor dalam bentuk grafik |
| **Node-RED** | Dashboard interaktif untuk monitoring & kontrol |
| **Telegram API** | Mengirim notifikasi otomatis ke pengguna |
| **Scikit-learn / TensorFlow** | Prediksi waktu penyiraman dengan AI |
| **Docker** | Menjalankan MySQL, Grafana, dan layanan lain dalam container |

---

## **🛠️ 2. Instalasi & Setup**  
### **2.1 Hardware yang Dibutuhkan**
- **Raspberry Pi 3/4** (atau perangkat IoT lainnya)
- **Sensor kelembaban tanah** (YL-69/Capacitive Moisture Sensor)
- **Sensor suhu & kelembaban udara** (DHT11/DHT22)
- **Sensor cahaya** (LDR)
- **Sensor hujan** (Rain Sensor)
- **pH meter** (untuk mengukur keasaman tanah)
- **Relay module** (untuk mengontrol pompa air)
- **Pompa air & solenoid valve** (untuk penyiraman otomatis)
- **Panel surya + Battery (Opsional)**

### **2.2 Instalasi Software**  
#### **🌀 Raspberry Pi Setup**
1. Update Raspberry Pi:  
   ```sh
   sudo apt update && sudo apt upgrade -y
   ```
2. Install Python dan library yang dibutuhkan:  
   ```sh
   sudo apt install python3-pip -y
   pip3 install -r requirements.txt
   ```
3. Setup **MySQL Server** (jika menggunakan MySQL):  
   ```sh
   sudo apt install mysql-server -y
   ```

#### **🖥️ Setup Grafana untuk Visualisasi**
1. **Instal Grafana:**  
   ```sh
   sudo apt install grafana -y
   sudo systemctl start grafana-server
   sudo systemctl enable grafana-server
   ```
2. Akses **Grafana** melalui `http://RaspberryPi_IP:3000`

#### **🌎 Setup Node-RED untuk Dashboard**
1. **Instal Node-RED:**  
   ```sh
   sudo npm install -g --unsafe-perm node-red
   ```
2. Jalankan Node-RED:  
   ```sh
   node-red-start
   ```
3. Akses melalui `http://RaspberryPi_IP:1880`

#### **📦 Menjalankan dengan Docker (Opsional)**
Jika ingin menjalankan MySQL & Grafana di Docker:  
```sh
docker-compose up -d
```

---

## **🔗 3. Struktur Proyek**
```
smart_irrigation_system/
│── sensors/
│   ├── read_sensors.py    # Membaca data dari sensor
│   ├── save_to_db.py      # Menyimpan data ke MySQL/Firebase
│── control/
│   ├── pump_control.py    # Mengontrol pompa air berdasarkan kelembaban tanah
│── notifications/
│   ├── telegram_alert.py  # Mengirim notifikasi jika tanah kering
│── dashboard/
│   ├── grafana_setup.md   # Panduan setup Grafana
│   ├── node_red_setup.md  # Panduan setup Node-RED
│── docker/
│   ├── Dockerfile         # Container untuk MySQL/Grafana
│── README.md              # Dokumentasi proyek
│── requirements.txt       # Library Python yang dibutuhkan
│── config.py              # Konfigurasi API, database, dll.
```

---

## **🚀 4. Cara Menjalankan Proyek**
1. **Jalankan pembacaan sensor:**  
   ```sh
   python3 sensors/read_sensors.py
   ```
2. **Aktifkan sistem penyiraman otomatis:**  
   ```sh
   python3 control/pump_control.py
   ```
3. **Menjalankan notifikasi Telegram:**  
   ```sh
   python3 notifications/telegram_alert.py
   ```
4. **Lihat data di Grafana:**  
   Buka `http://RaspberryPi_IP:3000`  
5. **Kontrol penyiraman dari Node-RED:**  
   Buka `http://RaspberryPi_IP:1880`

---

## **🔧 5. Konfigurasi Telegram Notifikasi**
Untuk mendapatkan notifikasi jika tanah terlalu kering:  
1. Buat bot Telegram dengan `@BotFather`  
2. Simpan `TOKEN` dari bot yang dibuat  
3. Dapatkan chat ID dengan menjalankan:  
   ```sh
   curl https://api.telegram.org/botTOKEN/getUpdates
   ```
4. Masukkan `TOKEN` & `chat ID` ke **config.py**:  
   ```python
   TELEGRAM_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
   TELEGRAM_CHAT_ID = "YOUR_CHAT_ID"
   ```

---

## **📈 6. Menggunakan Machine Learning untuk Prediksi Penyiraman**
Sistem ini dapat menggunakan **Scikit-learn** untuk memprediksi kapan penyiraman harus dilakukan.  
Contoh model sederhana dengan **Naive Bayes**:  
```python
from sklearn.naive_bayes import GaussianNB

# Data latihan (kelembaban tanah, suhu, kelembaban udara) → hasil penyiraman (1=Ya, 0=Tidak)
X_train = [[30, 25, 60], [40, 28, 65], [25, 22, 55]]
y_train = [1, 1, 0]

model = GaussianNB()
model.fit(X_train, y_train)

# Prediksi penyiraman untuk kelembaban 35%, suhu 27°C, kelembaban udara 63%
prediksi = model.predict([[35, 27, 63]])
print("Perlu menyiram?" , "Ya" if prediksi[0] == 1 else "Tidak")
```

---

## **🎯 7. Kontribusi**
Kami membuka kontribusi dari komunitas untuk:  
✅ Menambahkan sensor lain (misalnya **sensor kelembaban daun**)  
✅ Mengoptimalkan model **Machine Learning**  
✅ Memperbaiki & meningkatkan **antarmuka Grafana/Node-RED**  
✅ Menyediakan fitur kontrol tambahan via **mobile app**  

Silakan **fork, pull request, atau diskusi** di **GitHub Issues**. 🚀  

---

## **📜 8. Lisensi**
Proyek ini menggunakan **MIT License**.  

**💡 Ingin berkontribusi? Yuk, gabung ke komunitas kami!** 🚀🚀🚀