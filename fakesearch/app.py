from flask import Flask,render_template
import flask
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sendmsg')
def sendmsg():
    key = "628829631:AAFpHO-RChiJqxOeudFf8XYj77cYpQDqzVE"
    url = "https://api.hphk.io/telegram/bot%s/"%(key)
    your_id = "235391244"
    msg = flask.request.args.get("msg")
    chat_url = url + "sendMessage?chat_id=%s&text=%s"%(your_id,msg)
    print(requests.get(chat_url))
    return render_template('sendmsg.html',msg=msg)
    
app.run()