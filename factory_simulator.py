import requests
import time
import random
import uuid


INFLUX_URL = "http://localhost:8086/api/v2/write?org=manufacturing-iot&bucket=signals&precision=ns"
INFLUX_TOKEN = "my-super-token-secret"  

headers = {
    "Authorization": f"Token {INFLUX_TOKEN}",
    "Content-Type": "text/plain; charset=utf-8"
}

print("🏭 Factory Simulator Started... Press Ctrl+C to stop.")

try:
    while True:
    
        temperature_value = round(20.0 + random.random() * 5, 2)  
        correlation_id = str(uuid.uuid4()) 
        tags = "signals,site=dk-plant1,area=packaging,line=line3,asset=filler1,signal=temperature,unit=C,quality=GOOD"
        fields = f'value_numeric={temperature_value},correlationId="{correlation_id}"'
        payload = f"{tags} {fields} {time.time_ns()}"
        response = requests.post(INFLUX_URL, headers=headers, data=payload)
        
        if response.status_code == 204:
            print(f"✅ Sent: {temperature_value}°C | ID: {correlation_id[:5]}...")
        else:
            print(f"❌ Error {response.status_code}: {response.text}")

        time.sleep(1) 

except KeyboardInterrupt:
    print("\n🛑 Simulator stopped.")