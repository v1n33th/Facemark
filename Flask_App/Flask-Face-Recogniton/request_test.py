from dataclasses import dataclass
from urllib import response
import requests
from datetime import datetime

dt_now = datetime.now()
time = dt_now.strftime("%Y-%m-%d %H:%M:%S")
query = {"time_log": str(time)}

headers = {"charset": "utf-8", "Content-Type": "application/json"}
response = requests.post("http://192.168.2.172:8000/users/4/in_out/1", json=query, headers=headers)
print(response.status_code)
