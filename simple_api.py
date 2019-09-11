from flask import Flask
from flask import request
from manipulation import Manipulation

app = Flask(__name__)
manipulation = Manipulation()

@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/averages', methods = ['GET'])
def averages():
    return manipulation.average_by_dept()

@app.route('/headcount_over_time', methods = ['GET'])
def headcount_over_time():
    dept = request.args.get('department')
    return manipulation.headcount_over_time(dept)

if __name__ == '__main__':
    app.run()