import numpy as np 
import cv2



class Camera:


    def startCamera(self):

        cap = cv2.VideoCapture(0)


        
        while True:
            ret,frame = cap.read()
            


            ret, buffer = cv2.imencode('.jpg', frame)

            frame = buffer.tobytes()

            yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

            
        
        cap.release()
        cv2.destroyAllWindows()





