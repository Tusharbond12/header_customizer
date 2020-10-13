
from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime
import pymongo

app=Flask(__name__)
@app.route('/register', methods=['GET','POST'])
def register():
    return render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/',methods=['POST','GET'])
def homepage_signup():
    rule = request.url_rule
    print("HELLO"+rule.rule)
    return render_template("index.html")

@app.route('/letsee',methods=['GET','POST'])
def check_up():
    fromm=request.form['tus']
    wh=request.form['pus']
    print('This is ', fromm )
    print('This is ',wh)
    return render_template('result.html')

@app.route('/result',methods=['POST'])
def result():
    try:
        url = request.form['url']
        if(url[0:4] != 'http' or url[0:5] != "https"):
            url = "http://" + url
        print(url)
        attr=dict(request.form)
        print(attr)
        attr.pop('url')
        headers=attr
        #dt=datetime.now()
        req=requests.get(url,headers=headers)
        #headers['dt']=dt

        res_headers = req.headers
        #res_headers['dt']=dt
        #DB_NAME = 'CN_LAB'
        #client = pymongo.MongoClient('mongodb://localhost:27017/')
        #database = client[DB_NAME]
        #collection1 = database['Requests']
        #collection = database['Responses']
        #collection.insert_one(res_headers)
        #collection1.insert_one(headers)
        #res_headers.pop('dt')
        content = {"res_headers":res_headers,"r_url":req.url,'req':req}
        return render_template('result.html',**content)
    except Exception:
        return render_template('index.html',query="No such url exist!")
if __name__ == "__main__":
    app.run(port=8080,debug=True)