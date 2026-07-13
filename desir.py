import requests
import json

URL = "http://127.0.0.1:8000/aicreate/"

data = {
    'teacher_name': 'John Doe',
    'course': 'Deep Learning',
    'course_duration': 3,
    'seat': 30,
}

json_data = json.dumps(data)
r = requests.post(url=URL, data=json_data)
data = r.json()
print(data)