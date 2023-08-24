import requests
from datetime import datetime


current_time = int(datetime.now().timestamp()*1000) # timestamp_ms

resp = requests.get(
    url='http://127.0.0.1:8080/api/httptest',
    params={'timestamp': current_time}
)
print( '%sms' % resp.text)