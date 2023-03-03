import streamlit as st
import cv2
from datetime import datetime
import time
# commit: display overlay date on cam video Sec36

st.title('Motion Detector')
start_button=st.button('Start Camera')

if start_button:
    streamlit_image=st.image([])
    
    camera=cv2.VideoCapture(0)
    time.sleep(1)

    while True:
        now=datetime.now()

        check,frame=camera.read()
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

        cv2.putText(img=frame,text=now.strftime('%A'),org=(50,50),
                    fontFace=cv2.FONT_HERSHEY_PLAIN,fontScale=2,color=(255,255,255),
                    thickness=2,lineType=cv2.LINE_AA)
        cv2.putText(img=frame,text=now.strftime('%H:%M:%S'),org=(50,90),
                    fontFace=cv2.FONT_HERSHEY_PLAIN,fontScale=2,color=(255,10,40),
                    thickness=2,lineType=cv2.LINE_AA)
        
        streamlit_image.image(frame)
    camera.release()
    
    print('done')



