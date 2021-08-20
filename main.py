from flask import Flask,render_template,Response,request
import cv2
from streamPy import  Stream



app = Flask(__name__)

stream = Stream()




@app.route('/video_feed')
def VideoStream():
    return Response(stream.get_ByteFrames(),mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def Startpage():
    return render_template('index.html')


@app.route('/',methods = ["POST"])
def activateMotors():
    print(request.form)
    return render_template('index.html')




if __name__ == "__main__":
    app.run(debug = True,host = '0.0.0.0',port=5000)