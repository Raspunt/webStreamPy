from flask import Flask,render_template,Response,request

from time import *
from  motors import MotorMood

from camera import Camera


app = Flask(__name__)
mm = MotorMood()



@app.route('/video_feed')
def VideoStream():
    cam = Camera()
    return Response(cam.startCamera(),mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def Startpage():
    return render_template('index.html')


comArray = []

@app.route('/',methods = ["POST"])
def activateMotors():
    print(request.form)
    com = request.form['comand']
    comArray.append(com)
    while (len(comArray) == 1):
        if com == "up":
            mm.motorV()
            print("едет в вперед")
        if com == "down":
            mm.motorD()
            print("едет в назад")

        if com == "left":
            mm.motorL()
            print("едет в лево")

        if com == "right":
            mm.motorR()
            print("едет в право")

        if com == "stop":
            mm.motorS()
            print("Stop")
    else :
        comArray.clear()
        print(len(comArray))



#    if com == 'down':
#       mot1.backward()
#        mot2.backward()
#        print('вниз')


    return render_template('index.html')




if __name__ == "__main__":
    app.run(debug = True,host = '0.0.0.0',port=5000)
