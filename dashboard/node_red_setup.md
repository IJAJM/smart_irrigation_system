# Setup Node-RED

1. Instal Node-RED:
```sh
sudo npm install -g --unsafe-perm node-red
```

2. Jalankan Node-RED:
```sh
node-red
```
Akses `http://<IP_RASPBERRY>:1880`

3. Instal Dashboard UI:
```sh
cd ~/.node-red
npm install node-red-dashboard
```

4. Buat Flow:
- **Input:** Inject Node  
- **Switch:** soil_moisture < threshold  
- **Output:** GPIO untuk pompa  
- **Dashboard UI:** Grafik data sensor

Simpan dan deploy.
