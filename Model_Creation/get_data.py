from cProfile import label
import cv2
import numpy as np
import uuid
import os

def preprocess_image(img):
    print(len(img))
    img = cv2.resize(img, (250,250))
    return img

def main():

    person = input("Enter the name of the person")
    font = cv2.FONT_HERSHEY_SIMPLEX
    path = os.path.join("Data", person)
    if not os.path.isdir(path):
        os.makedirs(path)

    org = (50, 50)
    fontScale = 1
    color = (255, 0, 0)
    thickness = 2
    
    classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    
    cam = cv2.VideoCapture(0)
    fe = False
    count = 0
    while True:
        ret_val, img = cam.read()
        bboxes = classifier.detectMultiScale(img)
        for box in bboxes:
            x, y, w, h = box
            face = img[y:y + h, x:x + w] 
            if len(face)<150:
                print(len(face))
                break
            else:
                face = preprocess_image(face)
                unique_filename = str(uuid.uuid4())
                img_name = os.path.join(path, person + unique_filename +".jpg")
                cv2.imwrite(img_name, face)
                count += 1
                img = cv2.putText(img, str(count), org, font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.rectangle(img, (x, y), (x + w, y +h), (0,0,255), 1)

        cv2.imshow('my webcam', img)

        if cv2.waitKey(1) == 27 or count >= 500: 
            break 
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
