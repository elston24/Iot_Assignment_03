import time
import random
import urequests
import network

# WiFi settings
ssid = 'Wokwi-GUEST'
password = ''  # No password for Wokwi simulated WiFi

# ThingSpeak settings
write_api_key = 'HXEF36DWFIM3YGJ0'
channel_id = '2488446'
base_url = 'http://api.thingspeak.com/update'

def connect_to_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Connecting to WiFi...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print('Connected to WiFi')

def generate_sensor_data():
    temperature = random.uniform(-50, 50)
    humidity = random.uniform(0, 100)
    co2 = random.uniform(300, 2000)
    return temperature, humidity, co2

def send_data(temperature, humidity, co2):
    url = f'{base_url}?api_key={write_api_key}&field1={temperature}&field2={humidity}&field3={co2}'
    try:
        response = urequests.get(url)
        if response.status_code == 200:
            print(f"Data sent successfully: Temperature={temperature}, Humidity={humidity}, CO2={co2}")
        else:
            print(f"Failed to send data: {response.text}")
        response.close()
    except Exception as e:
        print(f"Error occurred: {e}")

connect_to_wifi(ssid, password)

try:
    while True:
        temperature, humidity, co2 = generate_sensor_data()
        send_data(temperature, humidity, co2)
        time.sleep(15)  # Publish every 15 seconds
except KeyboardInterrupt:
    print('Script stopped')
