
from base_camera import BaseCamera
import cv2
import base64 

# In[]

class Camera(BaseCamera):
    
    @staticmethod
    def frames():
        
        while True:
        
            # cam = cv2.VideoCapture("video.MOV")
            cam = cv2.VideoCapture(0)
            
            assert cam.isOpened(), "Can not open video file."
            
            while True:
                ret, img = cam.read()

                
                if ret:
                    # resize the frame to 0.5x
                    buffer = cv2.imencode('.jpg', img)[1]
                    jpg_as_text = base64.b64encode(buffer).decode('utf-8', 'ignore')
                    
                    
                    
                    # 
                    
                    # encode as a jpeg image and return it
                    yield jpg_as_text
                else:
                    break
            
