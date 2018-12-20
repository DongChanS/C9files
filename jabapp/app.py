from flask import Flask,send_file,render_template
from random import sample
from bs4 import BeautifulSoup
import requests
import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
 
@app.route("/name")
# 비슷하게 써주는게 관례?
def name():
    return "Dong Chan"

@app.route("/hello/<name>")
def hi(name):
    return "hello " + name + "!"

@app.route("/cube/<int:number>")
def cube(number):
    return str(number**3)

@app.route("/reverse/<string>")
def reverse(string):
    return string[::-1]
    
@app.route("/palindrome/<string>")
def palindrome(string):
    return "True" if string == string[::-1] else "False"

@app.route("/profile")
def profile():
    return send_file("profile.html")

# @app.route("/lotto")
# def lotto():
#     result = str(sorted(sample(range(1,46),6)))
#     return result

@app.route("/lotto/<name>")
def lotto(name):
    result = str(sorted(sample(range(1,46),6)))
    return render_template('lotto.html',result=result, name=name)


@app.route("/kospi")
def kospi():
    # https://finance.naver.com/sise/에서 코스피가격 스크래핑해서 가져오기
    url = "https://finance.naver.com/sise/"
    doc = BeautifulSoup(requests.get(url).text,'html.parser')
    sise = doc.select_one('#KOSPI_now').text
    return render_template('kospi.html',sise=sise)


@app.route("/isitfirstday")
def isitfirstday():
    now = datetime.datetime.now()
    day = now.day
    month = now.month
    remain = (datetime.datetime(2019,1,1) - now).days
    return render_template('newyear.html',day=day,month=month,remain=remain)
    
app.run()