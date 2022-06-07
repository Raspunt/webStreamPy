
from flask import Flask,render_template,Response,request
from cameraStreamer import CameraStream

app = Flask(__name__)

cap = CameraStream()


@app.route('/video_feed')
def VideoStream():
    return Response(cap.getFrames(),mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug = True,host = '0.0.0.0',port=5000)


