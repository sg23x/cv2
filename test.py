#
#
import cv2
model = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyemod = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
img = cv2.imread('notsmiling.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = model.detectMultiScale(gray, 1.1, 4)
for (x, y, w, h) in faces:
    eye_img = img[y:y+h, x:x+w]
    eye_gray = gray[y:y+h, x:x+w]
    cv2.rectangle(img, (x, y), (x+w, y+h), (178, 209, 67), 2)
    cv2.putText(img, 'face', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
    eyes = eyemod.detectMultiScale(eye_gray, 1.1, 4)
    for (xe, ye, we, he) in eyes:
        cv2.rectangle(eye_img, (xe, ye), (xe + we, ye + he), (0,0,255), 2)
        cv2.putText(eye_img, 'eye', (xe, ye-10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,255,255), 1)
cv2.imshow('face detected', img)
cv2.waitKey()

#import cv2
#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#cap = cv2.VideoCapture('why.mp4')
#while True:
#    x, img = cap.read()
#    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
#    for (x, y, w, h) in faces:
#        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
#    cv2.imshow('img', img)
#    k = cv2.waitKey(30) & 0xff
#    if k==27:
#        break
#cap.release()

#import cv2
#model = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#model = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
#img = cv2.imread('no.jpg')
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#faces = model.detectMultiScale(gray, 1.1, 4)
#for (x, y, w, h) in faces:
#    cv2.rectangle(img, (x, y), (x+w, y+h), (178, 209, 67), 2)
#    cv2.putText(img, 'face', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
#cv2.imshow('face detected', img)
#cv2.waitKey()