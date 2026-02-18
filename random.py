import smbus2
import time
import requests
import random  # Szükséges a véletlenszámhoz

# --- BEÁLLÍTÁSOK ---
I2C_ADDR = 0x08
API_KEY = "QNC42K1EEN75OMFG"
URL = "https://api.thingspeak.com/update"

bus = smbus2.SMBus(1)

def get_arduino_data():
    try:
        # Megpróbáljuk kiolvasni az adatot az I2C-ről (hogy a kapcsolat éljen)
        data = bus.read_i2c_block_data(I2C_ADDR, 0, 2)
        
        # --- MÓDOSÍTÁS: Felülírjuk a kiolvasott adatot randommal ---
        # A random.uniform(22.1, 23.0) generálja a számot
        # A round(..., 1) pedig 1 tizedesjegyre kerekíti
        temp = round(random.uniform(22.1, 23.0), 1)
        hum = data[1] # A páratartalmat meghagyhatjuk az eredetinek, vagy ezt is randomizálhatjuk
        
        return temp, hum
    except Exception as e:
        print(f"I2C hiba (de generálok adatot): {e}")
        # Ha nincs rákötve az Arduino, akkor is adjon vissza valamit, hogy ne álljon le
        temp = round(random.uniform(22.1, 23.0), 1)
        return temp, 50 # 50% alapértelmezett páratartalom hiba esetén

print("Adatküldés indítása (I2C + Random)...")

while True:
    temp, hum = get_arduino_data()
    
    if temp is not None:
        params = {
            'api_key': API_KEY,
            'field1': temp,
            'field2': hum
        }
        
        try:
            r = requests.get(URL, params=params)
            if r.status_code == 200:
                print(f"Siker! Küldött (Random) Temp: {temp}C, Hum: {hum}%")
            else:
                print(f"Hiba a küldésnél: {r.status_code}")
        except Exception as e:
            print(f"Hálózati hiba: {e}")

    time.sleep(20)