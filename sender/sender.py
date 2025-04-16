import csv
import time
import json
import requests
import os

# Get the absolute path to the CSV file relative to the script location
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR, 'ip_addresses.csv')

# URL to the Flask server (using the container name “server” in docker-compose)
SERVER_URL = 'http://server:5000/receive'

def send_packages():
    with open(CSV_FILE, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        prev_timestamp = None
        for row in reader:
            current_timestamp = int(row['Timestamp'])
            if prev_timestamp is not None:
                sleep_duration = current_timestamp - prev_timestamp
                if sleep_duration > 0:
                    time.sleep(sleep_duration)
            prev_timestamp = current_timestamp

            payload = {
                'ip': row['ip address'],
                'latitude': float(row['Latitude']),
                'longitude': float(row['Longitude']),
                'timestamp': current_timestamp,
                'suspicious': float(row['suspicious'])
            }
            try:
                response = requests.get(SERVER_URL, params={'data': json.dumps(payload)})
                print(f"Sent package: {payload} | Server responded with: {response.status_code}")
            except Exception as e:
                print(f"Error sending package: {e}")

if __name__ == '__main__':
    send_packages()
