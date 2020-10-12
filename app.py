
from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime
import pymongo

app=Flask(__name__)
@app.route('/', methods=['GET','POST'])
def register():
    return render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/homepage_sign_up',methods=['POST','GET'])
def homepage_signup():

    return render_template("index.html")


@app.route('/homepage_signin',methods=['POST'])
def homepage_signin():


    return render_template("index.html")


@app.route('/result',methods=['POST'])
def result():
    url = request.form['url']
    fromm = request.form['from']
    host = request.form['host']
    headers={'From':fromm , 'Host': host}
    dt=datetime.now()
    req=requests.get("https://www.youtube.com/",headers=headers)
    headers['dt']=dt

    res_headers = req.headers
    res_headers['dt']=dt
    DB_NAME = 'CN_LAB'
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    database = client[DB_NAME]
    collection1 = database['Requests']
    collection = database['Responses']
    collection.insert_one(res_headers)
    collection1.insert_one(headers)
    res_headers.pop('dt')
    return render_template('result.html', res_headers=res_headers)

if __name__ == "__main__":
    app.run(port=8080,debug=True)