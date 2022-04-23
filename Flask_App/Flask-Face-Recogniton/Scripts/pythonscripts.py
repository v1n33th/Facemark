import cv2
import numpy as np
import requests
from datetime import datetime
from Employee.employee import employee_table

def recognize_face(img, model):
    label = np.argmax(model.predict(img))
    return label

def preprocess_image(img):
    print(len(img))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (250,250))
    img = np.asarray([img/255])
    return img

def call_api(label, punch_type):
    
    emp = employee_table[label]
    emp_id = emp["user_id"]
    emp_name = emp["name"]
    
    dt_now = datetime.now()
    time = dt_now.strftime("%Y-%m-%d %H:%M:%S")
    query = {"time_log": str(time)}

    if punch_type == "punch_in":
        action_id = "1"
        action = "punched in"
    else:
        action_id = "2"
        action = "punched out"

    headers = {"charset": "utf-8", "Content-Type": "application/json"}
    response = requests.post("http://192.168.2.172:8000/users/" + emp_id + "/in_out/" + action_id, json=query, headers=headers)
    if response.status_code == 200:
        return 1, label, time, emp_name, action
    else:
        return 0, label, None, emp_name, action

    