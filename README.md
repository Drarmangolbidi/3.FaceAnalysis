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


