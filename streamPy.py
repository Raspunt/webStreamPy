
import cv2 
import numpy as np
from threading import Thread
import time


class Stream:



    def __init__(self):

        self.camera =  cv2.VideoCapture(0)
        self.thread = Thread(target=self.update,args=())
        self.thread.daemon = True
        self.thread.start()

        



    def update(self):


        while True:
            self.ret ,self.frame =  self.camera.read()

            if self.frame is not None:
                cv2.imwrite("frame.png",self.frame)






    def get_frame(self):
        return self.frame 



    def get_ByteFrames(self):

        while True:
            try:
                frame = cv2.imread("frame.png")
                if frame  is not None:                
                    ret, buffer = cv2.imencode('.jpg', frame)
                    frame = buffer.tobytes()



                    yield (b'--frame\r\n'
                        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

            except Exception as e:
                print(e)


    def testStream(self,name_window):

        while True:

            try:
                # print(name_window) 

                cv2.imshow(f"{name_window}",self.frame)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    cv2.destroyAllWindows()
                    break

                
                
            except AttributeError as e:
                print(f"Нету картинки {e}" )

       






