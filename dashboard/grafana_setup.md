# Setup Grafana

1. Instal Grafana:
```sh
sudo apt install -y grafana
sudo systemctl start grafana-server
sudo systemctl enable grafana-server
```

2. Akses `http://<IP_RASPBERRY>:3000`
Login: **admin/admin**

3. Tambah Data Source:
- Pilih MySQL
- Host: `localhost:3306`
- Database: `sensor_db`
- User: `root`, Password: `password`

4. Buat Dashboard dengan Query:
```sql
SELECT time, temperature, humidity, soil_moisture FROM sensor_data
```
