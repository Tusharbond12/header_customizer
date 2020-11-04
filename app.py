
from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime
import pymongo
from html5print import HTMLBeautifier
import json
from flask_cors import CORS,cross_origin
import pymongo

app=Flask(__name__)
CORS(app)

@app.route('/',methods=['POST','GET'])
@cross_origin()
def homepage_signup():
    return render_template("index.html")
@app.route('/history',methods=['GET','POST'])
@cross_origin()
def history():
    try:

        import pymongo
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        dataBase = client['header_visualiser']
        COLLECTION_NAME = "req_res"
        collection = dataBase[COLLECTION_NAME]
        query = collection.find()
        data = []
        for record in query:
            dict = {}
            dict['date'] = record['date']
            dict['request'] = json.dumps(record['request'], indent=4)
            dict['response'] = json.dumps(record['response'], indent=4)
            data.append(dict)
        return render_template('history.html', data=data)
    except Exception:
        return render_template('index.html', query="Some server error has occured while fetching history")







@app.route('/result',methods=['POST'])
@cross_origin()
def result():
    try:
        url = request.form['url']
        meth = request.form['method']
        print(meth)
        if(url[0:4] != 'http' or url[0:5] != "https"):
            url = "http://" + url
        attr=request.form.to_dict()
        attr.pop('url')
        attr.pop('method')
        headers=attr
        req=requests.get(url,headers=headers)

        if(meth=="Post"):
            req=requests.post(url,headers=headers)
        elif(meth=="Delete"):
            req=requests.delete(url,headers=headers)
        elif(meth=="Head"):
            req=requests.head(url,headers=headers)
        elif(meth=="Put"):
            req=requests.put(url,headers=headers)











        res_headers = req.headers
<<<<<<< HEAD
        
        
        client = pymongo.MongoClient("mongodb+srv://admin:123@cluster0.jc3ai.mongodb.net/header_visualiser?retryWrites=true&w=majority")
        dataBase = client['header_visualiser']
        COLLECTION_NAME = "req_res"
        collection = dataBase[COLLECTION_NAME]
        dt=datetime.now()
        record={'date':dt,'request':req.request.headers,'response':res_headers}
        collection.insert_one(record)
=======
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        dataBase = client['header_visualiser']
        COLLECTION_NAME = "req_res"
        collection = dataBase[COLLECTION_NAME]
        dt=datetime.now()
        record={'date':dt,'request':req.request.headers,'response':res_headers}
        collection.insert_one(record)
        text=HTMLBeautifier.beautify(req.text, 4)
>>>>>>> a0d877e925298b52d6506ccdd1f63437a087da53


        content = {"res_headers":res_headers,"r_url":req.url,'req':req,'text':text }
        return render_template('result.html',**content)
    except Exception:
        return render_template('index.html',query="No such url exist!")
if __name__ == "__main__":
    app.run(port=8080,debug=True)