# DHT11 IoT Projekt - Matyass225
📋 Vizsga Projekt: Okos Meteorológiai Állomás
Rendszer: DHT11 -> Arduino (Slave) -> Raspberry Pi Zero W (Master) -> ThingSpeak (Cloud)

1. Hardveres felépítés (A bekötés magyarázata)
Szenzor: DHT11 digitális szenzor az Arduino D2 lábára kötve.

Kommunikáció: I2C protokoll (SDA és SCL vonalak).

Biztonság: Logic Level Shifter használata kötelező! Az Arduino 5V-os jeleit 3.3V-ra fordítja a Pi számára.

Címzés: Az Arduino I2C címe a kódban fixálva: 0x08.

2. Legfontosabb Linux parancsok (Cheat Sheet)
Hardver ellenőrzése
i2cdetect -y 1 – Megmutatja az I2C buszon lévő eszközöket. Ha látsz egy 08-at, a kapcsolat él.

Python környezet kezelése
cd ~ – Belépés a felhasználói mappába.

source dht_projekt/bin/activate – A virtuális környezet (venv) bekapcsolása.

deactivate – Kilépés a virtuális környezetből.

A program futtatása és ellenőrzése
python3 thingspeak_push.py – A script manuális elindítása.

ps aux | grep thingspeak_push.py – Megmutatja, hogy fut-e a program a háttérben.

kill [PID_szám] – Leállítja a futó folyamatot (a PID számot a fenti ps parancsból tudod kiolvasni).

Automatizálás és Naplózás
crontab -e – Az automatikus indítás (boot) beállításainak szerkesztése.

cat ~/log.txt – Megnézheted a program által mentett hibaüzeneteket vagy státuszokat.

Rendszer parancsok
hostname -I – Kilistázza a Raspberry Pi IP címét (fontos az SSH-hoz).

sudo shutdown -h now – A Raspberry Pi biztonságos leállítása (hogy ne sérüljön az SD kártya).

3. Hogyan magyarázd el a működést? (Vizsga válaszok)
Miért kell az Arduino és a Pi közé szinteltoló?
Az Arduino 5V-os logikai szinteket használ, a Raspberry Pi viszont csak 3.3V-ot bír el a GPIO lábain. Enélkül a Pi processzora maradandó károsodást szenvedne.

Miért jó a ThingSpeak?
Ez egy ingyenes IoT platform, amely HTTP protokollon keresztül fogadja az adatokat, automatikusan tárolja és grafikonon jeleníti meg azokat, így bárhonnan követhető a mérés.

Mi az az I2C?
Egy kétvezetékes (SDA - adat, SCL - órajel) soros kommunikációs busz, ahol egy "Mester" (Pi) több "Szolga" (Arduino) eszközt is tud vezérelni egyedi címek alapján.


Vizsga projekt leírás - DHT11 I2C RPi
Projekt Összefoglaló: DHT11 - Arduino - RPi Zero W - ThingSpeak

1.  Hardver Felépítés

  - Szenzor: DHT11 (Arduino D2 pin).
  - Vezérlő: Arduino Uno (I2C Slave, cím: 0x08).
  - Átjáró: Raspberry Pi Zero W (I2C Master).
  - Szinteltoló (Logic Level Shifter): Kötelező az Arduino (5V) és a Pi (3.3V) közé!
      - Arduino A4 (SDA) -> HV1 | LV1 -> Pi Pin 3 (SDA)
      - Arduino A5 (SCL) -> HV2 | LV2 -> Pi Pin 5 (SCL)

2.  Szoftveres Működés

  - Az Arduino beolvassa a hőmérsékletet és páratartalmat, majd I2C-n várakozik.
  - A Raspberry Pi egy Python script segítségével 20 másodpercenként lekéri az adatokat.
  - A Pi a beépített Wi-Fi-n keresztül küldi az értékeket a ThingSpeak felhőbe.

3.  Hasznos Parancsok

  - I2C eszköz keresése: i2cdetect -y 1
  - Manuális indítás: source dht_projekt/bin/activate majd python3 thingspeak_push.py
  - Log ellenőrzése: cat /home/matyi/log.txt

4.  Vizsga Tippek

  - Hangsúlyozd a közös földelés (GND) fontosságát.
  - Említsd meg a virtuális környezet (venv) használatát a rendszerstabilitás miatt.


Hozz létre egy projekt mappát (ha még nincs):
mkdir -p ~/vizsga_anyagok

Hozd létre a leírást:
nano ~/vizsga_anyagok/projekt_leiras.txt

Másold bele az alábbi rövidített emlékeztetőt:

PROJEKT ÖSSZEFOGLALÓ (EMLÉKEZTETŐ)
1. Kapcsolat:

Arduino Uno (5V) <—> Logic Level Shifter <—> RPi Zero W (3.3V)

Protokoll: I2C (Arduino Slave 0x08).

DHT11 az Arduinóra kötve (Pin D2).

2. Teendők indítás után:

Ellenőrizd az I2C-t: i2cdetect -y 1 (A 08-as címnek látszania kell).

A Python script automatikusan indul (Crontab beállítva).

ThingSpeak felületén figyeld a grafikon frissülését (20mp-enként).

3. Fontos vizsga-kulcsszavak:

I2C Master/Slave architektúra.

Feszültségszint eltolás (3.3V vs 5V).

Felhő alapú adatmegjelenítés (IoT).
