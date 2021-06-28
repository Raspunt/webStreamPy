from flask import Flask,render_template,Response,request
import gpiozero as gz
from time import *
from  motors import MotorMood

from camera import Camera


app = Flask(__name__)

mot1 = gz.Motor(16,19)
mot2 = gz.Motor(17,27)
mm = MotorMood()
isRun = False



@app.route('/video_feed')
def VideoStream():
    cam = Camera()
    return Response(cam.startCamera(),mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def Startpage():
    return render_template('index.html')


@app.route('/',methods = ["POST"])
def activateMotors():
    print(request.form)
    com = request.form['comand']
    if com == "up":
        for i in range(10000):
            mm.motorV()
    if com == "down":
        for i in range(10000):
            mm.motorD()

    if com == "left":
        for i in range(10000):
            mm.motorL()

    if com == "right":
        for i in range(10000):
            mm.motorR()



#    if com == 'down':
#       mot1.backward()
#        mot2.backward()
#        print('вниз')


    return render_template('index.html')




if __name__ == "__main__":
    app.run(debug = True,host = '0.0.0.0',port=5000)
