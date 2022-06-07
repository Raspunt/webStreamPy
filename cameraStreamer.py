
import cv2
from threading import Thread
import time


class CameraFramesCreator(Thread):

    streamFrame = None


    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(CameraFramesCreator, cls).__new__(cls)
        
        return cls.instance

        
    def run(self):
        self.StartStream()



    def StartStream(self):
        camera = cv2.VideoCapture(0)
        while True:
            ret,frame = camera.read()
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            self.streamFrame = frame

            cv2.waitKey(0)


            # yield (b'--frame\r\n'
            #    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


class CameraStream:


    def getFrames(self):

        cap = CameraFramesCreator()
        cap.start()


        while True:
    
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + cap.streamFrame + b'\r\n\r\n')




