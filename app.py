from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users')
def users():
    return {
        "Name": "Park Mun Hun",
        "Age": 23,
        "Addr": "Busan"
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80')