import cv2 as cv
import os
import pickle

import face_recognition

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL' : "https://project-796b3-default-rtdb.firebaseio.com/",
    'storageBucket' : "project-796b3.appspot.com",
})

folderPath = "Images"
pathList = os.listdir(folderPath)
imgList = []
studentId = []
for path in pathList:
    imgList.append(cv.imread(os.path.join(folderPath, path)))
    studentId.append(os.path.splitext(path)[0])
    filename = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(filename)
    blob.upload_from_filename(filename)

# print(len(imgList))
# print(studentId)

def FindEncodes(imageList):
    encodeList = []
    for img in imageList:
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        encodeList.append(face_recognition.face_encodings(img)[0])
    return encodeList

encodedList = FindEncodes(imgList)
encodedListWithId = [encodedList, studentId]

file = open("EncodeFile.p",'wb')
pickle.dump(encodedListWithId, file)
file.close()