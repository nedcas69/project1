
import face_recognition
import cv2
import numpy as np
import speech_recognition as recognizer
from sklearn.tree import DecisionTreeRegressor
#cam = cv2.VideoCapture('rtsp://92193:Bb123456@167.124.20.3:554/ISAPI/Streaming/Channels/101')
cam = cv2.VideoCapture(0)

# cam.set(3, 640) # set video widht
# cam.set(4, 480) # set video height

cam.set(3, 1280) # set video widht
cam.set(4, 720) # set video height

state = True

is_start = open("/home/oo7/project1/project1/twty/1.jpg")
state_for_start = is_start.readline()
if state_for_start == "0":
    state = True
    print("Запускаем скрипт")
else:
    state = False
    print("отредактируйте state.log")
is_start.close()

while state:

    is_start = open("/home/oo7/project1/project1/twty/1.jpg")
    state_for_start = is_start.readline()
    if state_for_start == "0":
        state = True
#         print("Запускаем скрипт")
    else:
        state = False
        print("отредактируйте state.log")
    is_start.close()


    ret, img =cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5, # origin
        minSize = (100, 100) # not origin
       )

    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
 
        if (confidence < 100):
            id = font.names[id]
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))
            # ---> можно тыкнуть функцию сюда
        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)

#              Самообучение
# ------------------------------------------------------------------------------------------------
       # if True:
         #   if id not in enterings:
           ##     enterings.append(id)
#
            #if id not in names:
            #    face_id=len(names)
            #    count += 1
            #    cv2.imwrite(path+"/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
            #    if count > count_of_shots:
            #        restudying()
            #        names.append("User."+str(face_id))
            #        recognizer.read(projectpath+'/trainer/trainer.yml')
            #        f = open(projectpath+"/enterings.log", "a")
            #        count=0
            #        f.write(str(face_id)+" User"+str(face_id)+"\n")                    
            #        f.close
#
            #        with open(projectpath+"/names.log", "w") as file:
            #            for name in names:
            #                file.write(name + '\n')

    cv2.imshow('camera',img) 
    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
cam.release()
cv2.destroyAllWindows()