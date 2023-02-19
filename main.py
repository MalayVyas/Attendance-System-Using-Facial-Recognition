import datetime
import cv2 as cv
import cvzone
import face_recognition
import pickle
import re
import firebase_admin
import numpy as np
from firebase_admin import db, credentials

# Database
cred = credentials.Certificate("Resources/ServiceAccountKey.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://attendance-database-b5042-default-rtdb.firebaseio.com/"
})

detectedTime = [0]*10
cap = cv.VideoCapture(0)
backImg = cv.imread("Resources/background.png", 1)

file = open("EncodeFile.p", 'rb')
encodedListWithId = pickle.load(file)
file.close()
encodeList, studentId = encodedListWithId

while cap.isOpened():

    # Reading Image and Resizing it
    ret, img = cap.read()
    imgSmall = cv.resize(img, (0,0), None, 0.25, 0.25)
    imgSmall = cv.cvtColor(imgSmall, cv.COLOR_BGR2RGB)

    # Fetching FaceLocation and Encoding
    faceCurFrame = face_recognition.face_locations(imgSmall)
    encodeCurFrame = face_recognition.face_encodings(imgSmall, faceCurFrame)

    counter = 0
    matchIndex = -1
    flag = False
    for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
        matches = face_recognition.compare_faces(encodeList, encodeFace)
        faceDis = face_recognition.face_distance(encodeList, encodeFace)
        matchIndex = np.argmin(faceDis)
        flag = False
        if matches[matchIndex] and faceDis[matchIndex]<0.4:
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            box = x1, y1, x2-x1, y2-y1
            img = cvzone.cornerRect(img, box, rt=0)
            flag = True
            if counter == 0:
                counter = 1
        else:
            flag = False

    if matchIndex != -1 and flag:
        path = studentId[matchIndex]
        imgPath = str(f'Images/{path}.jpg')
        detectedImg = cv.imread(imgPath, 1)
        backImg[58:58+400, 1462:1462+400] = detectedImg
        time = datetime.datetime.now()
        detectedTime[matchIndex] = time

    attendanceInfo = 0
    if matchIndex != -1 and flag:
        attendanceInfo = db.reference(f'AttendanceDatabase/{studentId[matchIndex]}').get()
        timeString = attendanceInfo.get("LastAttendanceTime")
        timelist = list(re.split(r":|-| ", timeString))
        # print(timelist)
        timelist[5] = timelist[5][:2]
        attendedLecDB = attendanceInfo["AttendedLectures"]
        timeDatetime = datetime.datetime(int(timelist[0]), int(timelist[1]), int(timelist[2]), int(timelist[3]), int(timelist[4]), int(timelist[5]))
        if (detectedTime[matchIndex] - timeDatetime).total_seconds() > 3600:
            key = attendanceInfo.get("RollNo")
            attendanceInfo["LastAttendanceTime"] = str(detectedTime[matchIndex])
            attendanceInfo["AttendedLectures"] += 1
            ref = db.reference('AttendanceDatabase')
            ref.child(key).set(attendanceInfo)
        else:

            backImg = cv.rectangle(backImg, (1461, 500), (1920, 1080), (161, 237, 175), -1)
            name = attendanceInfo["Name"]
            rollno = attendanceInfo["RollNo"]
            attendedLec = attendanceInfo["AttendedLectures"]
            cv.putText(backImg, str('Welcome, '), (1461, 540), cv.FONT_HERSHEY_COMPLEX, 1.5, (0, 0, 0), 2)
            cv.putText(backImg, str(f'{rollno}'), (1700, 540), cv.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
            cv.putText(backImg, str(f'Lectures Attended: {attendedLec}'), (1461, 680), cv.FONT_HERSHEY_COMPLEX, 1,
                       (0, 0, 0), 2)


    showFull = img
    showFull = cv.resize(img, (1280, 720), None)
    backImg[211:720+211,56:1280+56] = showFull
    cv.imshow("Attendance System", backImg)

    if cv.waitKey(27) & 0xFF == 27:
        break

cap.release()
cv.destroyAllWindows()