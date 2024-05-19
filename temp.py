import serial
import serial.tools.list_ports
import requests

def find_serial_port():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        if 'Arduino' in port.description:
            return port.device
    return None

port = find_serial_port()
if port is None:
    print("No suitable serial port found.")
else:
    ser = serial.Serial(port, 9600)

    url = 'https://test.jujuking.fr/temp.php'

    while True:
        if ser.in_waiting > 0:
            ligne = ser.readline().decode('utf-8').strip()
            print(ligne)
            
            if "Température" in ligne:
                temperature = ligne.split(':')[1].strip().replace(' °C', '')
                data = {'temperature': temperature}
                try:
                    response = requests.post(url, data=data)
                    print('Temperature sent successfully', response.status_code)
                except requests.exceptions.RequestException as e:
                    print('Error:', e)
            
            elif "Humidity" in ligne:
                humidity = ligne.split(':')[1].strip().replace(' %', '')
                data = {'humidity': humidity}
                try:
                    response = requests.post(url, data=data)
                    print('Humidity sent successfully', response.status_code)
                except requests.exceptions.RequestException as e:
                    print('Error:', e)
