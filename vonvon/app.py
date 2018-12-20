from flask import Flask,render_template,request
import requests
from faker import Faker
import random
import pickle

app = Flask(__name__)
name_job_dict = dict()
fake = Faker('ko_KR')

@app.route('/')
def landing():
    return render_template('index.html')

@app.route('/match')
def matching():
    try:
        with open('fish.txt','rb+') as f:
            fish = pickle.load(f)
    except:
        fish = {}
        
    me = request.args.get('me')
    you = request.args.get('you')
    if (me,you) in fish.keys() or (you,me) in fish.keys():
        try:
            num = fish[(me,you)]
        except:
            num = fish[(you,me)]
    else:
        num = str(random.randint(50,100))
        fish[(me,you)] = num
        with open('fish.txt','wb') as f:
            pickle.dump(fish,f)
            
    return render_template('match.html',me=me,you=you,num=num)

@app.route('/admin')
def admin():
    # 낚인 사람들의 명단을 보여줄것임.
    with open('fish.txt','rb') as f:
        fish = pickle.load(f)
    return render_template('admin.html',fish=fish.keys())


# 1. 루트에서 사용자의 이름을 입력 받습니다.
# 2. '/pastlife' : 랜덤으로 생성된 전생직업을 보여준다.
# 3. 조금 더 업그레이드 시켜서,, 검색한 이력이 있다면 처음 매칭된 직업을 보여줄것이고
# 4. 아니면 새로 생성된 이름을 보여줄것이다(딕셔너리)
@app.route('/junsaeng')
def index():
    return render_template('junsaeng.html')

@app.route('/pastlife')
def pastlife():
    name = request.args.get("name")
    if name not in list(name_job_dict.keys()):
        job = fake.job()
        name_job_dict[name] = job
    else:
        job = name_job_dict[name]
    return render_template('pastlife.html',name=name,job=job)