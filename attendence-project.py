import face_recognition
import os
import cv2
import numpy as np
from datetime import datetime

path = "project"
images = []
classnames = []
mylist = os.listdir(path)
print(mylist)
for c1 in mylist:
    curImg = cv2.imread(f'{path}/{c1}')
    images.append(curImg)
    classnames.append(os.path.splitext(c1)[0])

print(classnames)

def findEncoding(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return

def markattendence(name):
    with open('attendence.csv',"r+") as f:
        mydatalist = f.readlines()
        NameList = []
        for line in mydatalist:
            entry = line.split(',')
            NameList.append(entry[0])
        if name not in NameList:
            now = datetime.now()
            dtstring = now.strftime('%H:%M,%S')
            f.writelines(f'\n{name},{dtstring}')

markattendence('elon1')




encodelistknown = findEncoding(images)
print('Encoding Complete')


cap = cv2.VideoCapture(1)

while True:
    success, img = cap.read()
    imgs = cv2.resize(img,(0,0),None,0.25,0.25)
    imgs = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    facescurframe = face_recognition.face_locations(imgs)
    encodecurframe = face_recognition.face_encodings(imgs, facescurframe)

    for encodeface, faceloc in zip(encodecurframe,facescurframe):
        matches = face_recognition.compare_faces(encodelistknown, encodeface)
        print(matches)
        facedis = face_recognition.face_distance(encodelistknown, encodeface)
        print(facedis)

        matchindex = np.argmin(facedis)

        if matches[matchindex]:
            name = classnames[matchindex].upper()
            y1,x2,y2,x1 =  faceloc
            y1, x2, y2, x1 =  y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,25),2)
            markattendence(name)
            print(name)
        else:
            print("no image found")

    cv2.imshow("image",imgs)
    if cv2.waitKey(25)& 0xff == ord('q'):
            break
#
cap.release()
cv2.destroyAllWindows()