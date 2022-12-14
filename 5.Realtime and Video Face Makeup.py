#!/usr/bin/env python
# coding: utf-8

# In[1]:


import face_recognition
from PIL import Image, ImageDraw
import numpy as np
import cv2


# In[3]:


# webcam_video_stream = cv2.VideoCapture(0)
webcam_video_stream = cv2.VideoCapture('video.mp4')

all_face_locations = []


while True:
    
    ret,current_frame = webcam_video_stream.read()

    face_landmarks_list =  face_recognition.face_landmarks(current_frame)
    
    pil_image = Image.fromarray(current_frame)
    
    d = ImageDraw.Draw(pil_image)
    
    index=0
    while index < len(face_landmarks_list):
        
        for face_landmarks in face_landmarks_list:
          
            
            d.polygon(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 128))
            d.polygon(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 128))
            d.line(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 150), width=5)
            d.line(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 150), width=5)
        
        
            d.polygon(face_landmarks['top_lip'], fill=(0, 0, 200, 100))
            d.polygon(face_landmarks['bottom_lip'], fill=(0, 0, 200, 100))
            d.line(face_landmarks['top_lip'], fill=(150, 150, 150, 64), width=2)
            d.line(face_landmarks['bottom_lip'], fill=(150, 150, 150, 64), width=2)
        
        
            d.line(face_landmarks['left_eye'] + [face_landmarks['left_eye'][0]], fill=(0, 0, 0, 110), width=1)
            d.line(face_landmarks['right_eye'] + [face_landmarks['right_eye'][0]], fill=(0, 0, 0, 110), width=1)

    
        index +=1
    
     
    rgb_image = pil_image.convert('RGB') 
    rgb_open_cv_image = np.array(pil_image)
    
    bgr_open_cv_image = cv2.cvtColor(rgb_open_cv_image, cv2.COLOR_RGB2BGR)
    bgr_open_cv_image = bgr_open_cv_image[:, :, ::-1].copy()

    cv2.imshow("Webcam Video",bgr_open_cv_image)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam_video_stream.release()
cv2.destroyAllWindows()       


# In[ ]:




