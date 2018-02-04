from flask import Flask, render_template, flash, redirect, request, session, abort
from flask_socketio import SocketIO, emit
import os
import JSON

# https://flask-socketio.readthedocs.io/en/latest/
# https://github.com/socketio/socket.io-client

app = Flask(__name__)

app.config['SECRET_KEY'] = 'jsbcfsbfjefebw237u3gdbdc'
socketio = SocketIO(app)


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
            return render_template('./ChatApp.html')
       
 
@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return redirect('/')
 
@app.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect('/')


def messageReceived():
    print('message was received!!!')


@socketio.on('my event')
def handle_my_custom_event(json):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)


if __name__ == '__main__':
    socketio.run(app, debug=True)
