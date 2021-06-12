from flask import Flask,render_template,Response,request

from camera import Camera


app = Flask(__name__)





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
    return render_template('index.html')




if __name__ == "__main__":
    app.run(debug = True,host = '0.0.0.0',port=5000)