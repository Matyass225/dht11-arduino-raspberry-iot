import smbus2
import time
import requests

# --- BEÁLLÍTÁSOK ---
I2C_ADDR = 0x08
API_KEY = "QNC42K1EEN75OMFG"
URL = "https://api.thingspeak.com/update"

bus = smbus2.SMBus(1)

def get_arduino_data():
    # 2 bájtot kérünk az Arduinótól (temp, hum)
    try:
        data = bus.read_i2c_block_data(I2C_ADDR, 0, 2)
        return data[0], data[1]
    except Exception as e:
        print(f"I2C hiba: {e}")
        return None, None

print("Adatküldés indítása... (Ctrl+C-vel leállítható)")

while True:
    temp, hum = get_arduino_data()
    
    if temp is not None:
        # Adatküldés a ThingSpeak-nek
        params = {
            'api_key': API_KEY,
            'field1': temp,
            'field2': hum
        }
        
        try:
            r = requests.get(URL, params=params)
            if r.status_code == 200:
                print(f"Siker! Temp: {temp}C, Hum: {hum}% | ThingSpeak ID: {r.text}")
            else:
                print(f"Hiba a küldésnél: {r.status_code}")
        except Exception as e:
            print(f"Hálózati hiba: {e}")

    # A ThingSpeak ingyenes verziója 15 másodpercenként fogad adatot
    time.sleep(20)
