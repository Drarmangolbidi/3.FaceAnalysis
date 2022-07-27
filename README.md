# 3.FaceAnalysis
<br>

## :blush:Step One :( Find Landmarks of face ):blush:</b>

<br>

If you want to detect  the Landmarks you should download the "7.Arman.jpg" and "1.Face Landmarks.py" . 

<br>

![a](https://user-images.githubusercontent.com/109248678/181346710-cb7fb4c8-dfab-43d6-9e9e-eec58b57af6b.jpg)

<br>

Code is :👇

<br>

```python
import face_recognition
from PIL import Image , ImageDraw

face_image = face_recognition.load_image_file('7.Arman.jpg')

face_landmarks_list = face_recognition.face_landmarks(face_image)

print(face_landmarks_list)

for face_landmarks in face_landmarks_list:
    pil_image = Image.fromarray(face_image)
    d = ImageDraw.Draw(pil_image)
    d.line(face_landmarks['chin'] , fill=(255,255,255) ,width=1)
    d.line(face_landmarks['left_eyebrow'] , fill=(255,255,255) ,width=1)
    d.line(face_landmarks['right_eyebrow'] , fill=(255,255,255) ,width=1)
    d.line(face_landmarks['nose_bridge'] , fill=(255,255,255) ,width=1)
    d.line(face_landmarks['nose_tip'] , fill=(255,255,255) ,width=1)
    d.line(face_landmarks['left_eye'] , fill=(255,255,255) ,width=1)
    d.line(face_landmarks['right_eye'] , fill=(255,255,255) ,width=1)
    d.line(face_landmarks['top_lip'] , fill=(255,255,255) ,width=1)
    d.line(face_landmarks['bottom_lip'] , fill=(255,255,255) ,width=1)
pil_image.show()    
```
#### EX1_Leve :
- [ ] Simple! 
- [ ] Intermediate!
- [x] Hard!


<br>

## :blush:Step Two :( Multi-Face Landmarks ):blush:</b>

<br>

![b](https://user-images.githubusercontent.com/109248678/181349433-bacf292b-d695-4dfc-9536-60de4e5f0a11.jpg)

<br>

Code is :👇

<br>

```python
import face_recognition
from PIL import Image , ImageDraw
face_image = face_recognition.load_image_file('8.threeWoman.webp')
face_landmarks_list = face_recognition.face_landmarks(face_image)
print(face_landmarks_list)

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
```
#### EX2_Leve :
- [ ] Simple! 
- [ ] Intermediate!
- [x] Hard!


<br>

<br>

## :blush:Step three :( Multi-Face Landmarks for video ):blush:</b>

<br>

download "3.Video Multi-Face Landmarks.py" .

<br>
Code is :👇

<br>

```python
import face_recognition
from PIL import Image, ImageDraw
import numpy as np
import cv2

webcam_video_stream = cv2.VideoCapture(0)
all_face_locations = []
while True:   
    ret,current_frame = webcam_video_stream.read()
    
    face_landmarks_list =  face_recognition.face_landmarks(current_frame)
    
    pil_image = Image.fromarray(current_frame)
    
    d = ImageDraw.Draw(pil_image)    
    index=0
    while index < len(face_landmarks_list):
        
        for face_landmarks in face_landmarks_list:
          
            d.line(face_landmarks['chin'],fill=(255,255,255), width=1)
            d.line(face_landmarks['left_eyebrow'],fill=(255,255,255), width=1)
            d.line(face_landmarks['right_eyebrow'],fill=(255,255,255), width=1)
            d.line(face_landmarks['nose_bridge'],fill=(255,255,255), width=1)
            d.line(face_landmarks['nose_tip'],fill=(255,255,255), width=1)
            d.line(face_landmarks['left_eye'],fill=(255,255,255), width=1)
            d.line(face_landmarks['right_eye'],fill=(255,255,255), width=1)
            d.line(face_landmarks['top_lip'],fill=(255,255,255), width=1)
            d.line(face_landmarks['bottom_lip'],fill=(255,255,255), width=1)
    
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
```
#### EX3_Leve :
- [ ] Simple! 
- [ ] Intermediate!
- [x] Hard!
<br>

## :blush:Step Four :( 4.Face Makeup.py ):blush:</b>

<br>

![ArmanMackup](https://user-images.githubusercontent.com/109248678/181355930-01ad020e-7655-417b-9f17-c723e3c2b294.jpg)

<br>

before makeup

<br>

![Arman](https://user-images.githubusercontent.com/109248678/181355774-ba3799cb-f2d6-4de1-9ea0-65f9e1aa1634.jpg)
<br>



download "4.Face Makeup.py" and "Arman.jpg".

<br>

Code is :👇

<br>

```python
import face_recognition
from PIL import Image, ImageDraw

face_image = face_recognition.load_image_file('Arman.jpg')

face_landmarks_list =  face_recognition.face_landmarks(face_image)

print(face_landmarks_list)

for face_landmarks in face_landmarks_list:
    
    pil_image = Image.fromarray(face_image)
    d = ImageDraw.Draw(pil_image,"RGBA")
    
    d.polygon(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 128))
    d.polygon(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 128))
    d.line(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 150), width=5)
    d.line(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 150), width=5)


    d.polygon(face_landmarks['top_lip'], fill=(150, 0, 0, 128))
    d.polygon(face_landmarks['bottom_lip'], fill=(150, 0, 0, 128))
    d.line(face_landmarks['top_lip'], fill=(150, 0, 0, 64), width=8)
    d.line(face_landmarks['bottom_lip'], fill=(150, 0, 0, 64), width=8)

    d.line(face_landmarks['left_eye'] + [face_landmarks['left_eye'][0]], fill=(0, 0, 0, 110), width=6)
    d.line(face_landmarks['right_eye'] + [face_landmarks['right_eye'][0]], fill=(0, 0, 0, 110), width=6)

pil_image.show()

pil_image.save("makeup.jpg")

```
#### EX4_Leve :
- [ ] Simple! 
- [ ] Intermediate!
- [x] Hard!

<br>

## :blush:Step Five :( 5.Realtime and Video Face Makeup ):blush:</b>

<br>

download "" . amd turn on your webcam .

<br>

https://user-images.githubusercontent.com/109248678/181360101-5d00bd2d-8d17-4fb9-8690-26ab4c40346f.mp4

<br>

Code is :👇

<br>

```python
import face_recognition
from PIL import Image, ImageDraw
import numpy as np
import cv2

webcam_video_stream = cv2.VideoCapture(0)
#webcam_video_stream = cv2.VideoCapture('video.mp4')

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

```
#### EX5_Leve :
- [ ] Simple! 
- [ ] Intermediate!
- [x] Hard!
