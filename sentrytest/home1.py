from flask import Flask, Response
app = Flask(__name__)

from raven.contrib.flask import Sentry
sentry = Sentry(app, dsn='http://7fe4ca23adb74d4d92f5d17167e66919:8fce1ff465b445ea94c1210d1c5e91d7@devmeter:9000/2')




@app.route('/')
def hello_world():
    print('hey')
    try:
        paca = paca79*2
    except NameError:
        sentry.captureException()
    return Response(status=200)

if __name__ == "__main__":
    app.run(port=5000, host='192.168.0.100')