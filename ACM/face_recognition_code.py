# # import cv2
# # import numpy as np
# # import  face_recognition
# #
# # imgElon = face_recognition.load_image_file('Elon_Musk.jpg')
# # imgElon = cv2Color(imgElon,cv2.COLOR_BGR2RGB)
# #
# # imgTest  = face_recognition.load_image_file('Elon_Musk_test.jpg')
# # imgTest = cv2Color(imgElon,cv2.COLOR_BGR2RGB)
# #
# # cv2.imshow('Elon Musk',imgElon)
# # cv2.imshow('Elon Test',imgElon)
# # cv2.waitKey(0)
# import cv2
# import numpy as np
# import face_recognition
# import os
# from datetime import datetime
# import time
# import pandas as  pd
# import csv
#
# path = 'attendenceimages'
# # f = open("attendance.csv","r+")
# # f.truncate()
# data = pd.read_csv('Attendance.csv')
# images = []
# classnames = []
# fields = ['Name', 'Time']
# with open('Attendance.csv', 'r+') as f:
#     csvwriter = csv.writer(f)
#     csvwriter.writerow(fields)
#
# mylst = os.listdir(path)
# print(mylst)
#
# for img in mylst:
#     cur_img = cv2.imread(f'{path}/{img}')
#     images.append(cur_img)
#     classnames.append(os.path.splitext(img)[0])
# print(classnames)
#
#
# def find_encodings(images):
#     encodelist = []
#     for cl in images:
#         cl = cv2.cvtColor(cl, cv2.COLOR_BGR2RGB)
#         encode = face_recognition.face_encodings(cl)[0]
#         encodelist.append(encode)
#     return encodelist
#
#
# def markattendence(name):
#     with open('Attendance.csv', 'r+') as f:
#         mydatalist = f.readlines()
#         namelist = []
#         print(mydatalist)
#         for line in mydatalist:
#             entry = line.split(',')
#             namelist.append(entry[0])
#         if name not in namelist:
#             now = datetime.now()
#             dt_string = now.strftime('%H:%M:%S')
#             f.write(f"\n{name},{dt_string}")
#
#
# known_encodings = find_encodings(images)
# print('encoding completed')
#
# t0 = time.time()
# cap = cv2.VideoCapture(0)
#
# while True:
#     ret, img = cap.read()
#     imag_re = cv2.resize(img, (0, 0), None, 0.25, 0.25)
#     imag_re = cv2.cvtColor(imag_re, cv2.COLOR_BGR2RGB)
#
#     faces_cur_frame = face_recognition.face_locations(imag_re)
#     encodes_cur_frame = face_recognition.face_encodings(imag_re, faces_cur_frame)
#
#     for encodeface, faceloc in zip(encodes_cur_frame, faces_cur_frame):
#         matches = face_recognition.compare_faces(known_encodings, encodeface)
#         facedis = face_recognition.face_distance(known_encodings, encodeface)
#         # print(facedis)
#         matchindex = np.argmin(facedis)
#
#         if matches[matchindex]:
#             name = classnames[matchindex].upper()
#             # print(name)
#             y1, x2, y2, x1 = faceloc
#             y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
#             cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
#             cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
#             cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
#             markattendence(name)
#
#     cv2.imshow('webcam', img)
#     t1 = time.time()
#     if cv2.waitKey(1) & int(t1 - t0) > 60:
#         break
#
# df_csv = pd.read_csv('Attendance.csv')
# df_excel = pd.ExcelWriter('Attendance.xlsx')
# df_csv.to_excel(df_excel, index=False)
#
# df_excel.save()
#
# file_loc1 = 'Attendance.xlsx'
# file_loc2 = 'class_sheet.xlsx'
# df2 = pd.read_excel(file_loc1)
# df1 = pd.read_excel(file_loc2)
#
# name_df1 = df1['Name']
# name_df2 = df2['Name']
#
# print(name_df2)
# abs_df = df1.set_index('Name').drop(df2['Name'], errors='ignore').reset_index(drop=False)
# print(abs_df)
#
# abs_excel = pd.ExcelWriter('Absentees.xlsx')
# abs_df.to_excel(abs_excel, index=False)
#
# abs_excel.save()
#



# New program

import cv2
import numpy as np
import face_recognition
import os
from datetime import  datetime

path = 'commuter_images'
images = []
names = []
mylist = os.listdir(path)
print(mylist)
for cls in mylist:
    curImg = cv2.imread(f'{path}/{cls}')
    images.append(curImg)
    names.append(os.path.splitext(cls)[0])

print(names)

def findEncodings(images):
    encodelist = []
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode =  face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist

def markattendence(name):
    with open('commuters.csv', 'r+') as f:
        mydatalist = f.readlines()
        namelist = []
        print(mydatalist)
        for line in mydatalist:
            entry = line.split(',')
            namelist.append(entry[0])
        if name not in namelist:
            now = datetime.now()
            dt_string = now.strftime('%H:%M:%S')
            f.write(f"\n{name},{dt_string}")


encodeListKnown = findEncodings(images)
print(len(encodeListKnown))
print('Encoding completed')

cap = cv2.VideoCapture(0)

while True:
    success,img = cap.read()
    imgS = cv2.resize(img,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    faces_curr_frame = face_recognition.face_locations(imgS)
    encodes_curr_frame = face_recognition.face_encodings(imgS,faces_curr_frame)

    for encodeFace,faceLoc in zip(encodes_curr_frame,faces_curr_frame):
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDistance = face_recognition.face_distance(encodeListKnown,encodeFace)
        print(faceDistance)
        matchIndex = np.argmin(faceDistance)

        if matches[matchIndex]:
            name = names[matchIndex].upper()
            print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            markattendence(name)

    cv2.imshow('Webcam',img)
    cv2.waitKey(1)