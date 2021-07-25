# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 16:32:25 2021

@author: vipvi
"""
#import opencv
import cv2

#using xml files from openCV git
cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")

#capture the instance the video starts

video = cv2.VideoCapture(0)

while True:
    #captue return and frame when video is read
    ret, frame = video.read()
    #convert to gray
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #get rectangle with coordinates x,y,w,h
    face = cascade.detectMultiScale(gray,1.1,4)
    #use a for loop for the rectangle
    for (x,y,w,h) in face:
        #create green rectangle using openCV (BGR)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    #create fonts
    font = cv2.FONT_HERSHEY_COMPLEX
    #put text (video,text,origin,font,font thickness, color)
    cv2.putText(frame,'Vivek Ponnala',(5,400),font,2,(0,0,255))
    #draw line (video,start position, end position, color,thickness)
    cv2.line(frame,(50,20),(500,20),(255,0,0),2)
    cv2.line(frame,(75,30),(475,30),(255,0,0),2)
    #draw rectangle (video,start, end, color, thickness)
    cv2.rectangle(frame,(85,50),(450,300),(0,255,0),2)
    #show video with face detection
    cv2.imshow('Video',frame)
    if(cv2.waitKey(10) & 0XFF == ord('q')):
        break
#closes the video file
video.release()
#destroys all windows
cv2.destroyAllWindows()



    