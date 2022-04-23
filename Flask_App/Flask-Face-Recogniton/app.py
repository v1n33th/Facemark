from flask import Flask,render_template,Response, redirect
from cProfile import label
import cv2
import tensorflow as tf
import numpy as np
import Scripts.pythonscripts as ps
import cv2
import time
from flask_sse import sse
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

app=Flask(__name__)
app.config["REDIS_URL"] = "redis://localhost"
app.register_blueprint(sse, url_prefix='/stream')

cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX

org = (50, 50)
fontScale = 1
color = (255, 0, 0)
thickness = 2
model = tf.keras.models.load_model('Models/face_rec.h5')

def generate_frames(camtype):

    print(camtype)
    prev_label = None
    detected_label_count = {
        'label': None,
        'count': None
    }

    while True:
        success, img = cam.read()
        if not success:
            break
        else:
            classifier = cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')
            bboxes = classifier.detectMultiScale(img, 1.1, 7)
            for box in bboxes:
                x, y, w, h = box
                face = img[y:y + h, x:x + w] 
                if len(face)<150:
                    break
                else:
                    face = ps.preprocess_image(face)
                    label = ps.recognize_face(face, model)
                    if label != prev_label:
                        if detected_label_count['label'] == label:
                            if detected_label_count['count'] > 10:
                                prev_label = label
                                
                                status_code, label, time, emp_name, action = ps.call_api(label, camtype)
                                if status_code == 1:
                                    msg = emp_name + " " +  action + " at " + str(time)
                                else:
                                    msg = "There has been a issue while punching you in"

                                with app.app_context():
                                    sse.publish({"message":  msg, "status_code": status_code }, type='publish')
                            else:
                                detected_label_count['count'] += 1
                        else:
                            detected_label_count['label'] = label
                            detected_label_count['count'] = 1

                    cv2.rectangle(img, (x, y), (x + w, y +h), (0,255,0), 1)

            ret, buffer=cv2.imencode('.jpg',img)
            frame = buffer.tobytes()

        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return redirect("/punchin")

@app.route('/punchin')
def punchin():
    return render_template('index.html')

@app.route('/punchout')
def punchout():
    return render_template('indexOut.html')

@app.route('/videoin')
def videoin():
    return Response(generate_frames("punch_in"), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/videoout')
def videoout():
    return Response(generate_frames("punch_out"), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run(debug=True)

