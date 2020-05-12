from collections import namedtuple

from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)

Message = namedtuple('Message', 'text tag')
messages = []


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')


@app.route('/vprs1', methods=['GET'])
def vprs1():
    return render_template('vprs1.html', messages=messages)

@app.route('/vprs2', methods=['GET'])
def vprs2():
    return render_template('vprs2.html', messages=messages)

@app.route('/vprs3', methods=['GET'])
def vprs3():
    return render_template('vprs3.html', messages=messages)

@app.route('/vprs4', methods=['GET'])
def vprs4():
    return render_template('vprs4.html', messages=messages)

@app.route('/vprs5', methods=['GET'])
def vprs5():
    return render_template('vprs5.html', messages=messages)

@app.route('/vprs6', methods=['GET'])
def vprs6():
    return render_template('vprs6.html', messages=messages)

@app.route('/vprs7', methods=['GET'])
def vprs7():
    return render_template('vprs7.html', messages=messages)

@app.route('/vprs8', methods=['GET'])
def vprs8():
    return render_template('vprs8.html', messages=messages)

@app.route('/vprs9', methods=['GET'])
def vprs9():
    return render_template('vprs9.html', messages=messages)

@app.route('/vprs10', methods=['GET'])
def vprs10():
    return render_template('vprs10.html', messages=messages)

@app.route('/tvt', methods=['GET'])
def tvt():
    return render_template('tvt.html', messages=messages)

@app.route('/vprs0', methods=['GET'])
def vprs0():
    return render_template('vprs0.html', messages=messages)



@app.route('/add_message', methods=['POST'])
def add_message():
    text = request.form['text']
    tag = request.form['tag']

    messages.append(Message(text, tag))

    return redirect(url_for('main'))

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
