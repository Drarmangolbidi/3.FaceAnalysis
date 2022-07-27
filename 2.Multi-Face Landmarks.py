#!/usr/bin/env python
# coding: utf-8

# In[1]:


import face_recognition
from PIL import Image , ImageDraw


# In[2]:


face_image = face_recognition.load_image_file('picture2.jpg')


# In[3]:


face_landmarks_list = face_recognition.face_landmarks(face_image)

print(face_landmarks_list)


# In[4]:


pil_image = Image.fromarray(face_image)
d = ImageDraw.Draw(pil_image)

index=0
while index < len(face_landmarks_list):    
    for face_landmarks in face_landmarks_list:
        d.line(face_landmarks['chin'] , fill=(255,255,255) ,width=1)
        d.line(face_landmarks['left_eyebrow'] , fill=(255,255,255) ,width=1)
        d.line(face_landmarks['right_eyebrow'] , fill=(255,255,255) ,width=1)
        d.line(face_landmarks['nose_bridge'] , fill=(255,255,255) ,width=1)
        d.line(face_landmarks['nose_tip'] , fill=(255,255,255) ,width=1)
        d.line(face_landmarks['left_eye'] , fill=(255,255,255) ,width=1)
        d.line(face_landmarks['right_eye'] , fill=(255,255,255) ,width=1)
        d.line(face_landmarks['top_lip'] , fill=(255,255,255) ,width=1)
        d.line(face_landmarks['bottom_lip'] , fill=(255,255,255) ,width=1)
    index+=1
    
pil_image.show()  
pil_image.save('multiface_landmarks.jpg')


# In[ ]:




