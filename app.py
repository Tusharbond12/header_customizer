
from flask import Flask, render_template, request, jsonify
import requests
import pymongo

app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def homepage_signup():
    return render_template("index.html")

@app.route('/result',methods=['POST'])
def result():
    try:
        url = request.form['url']
        if(url[0:4] != 'http' or url[0:5] != "https"):
            url = "http://" + url
        print(url)
        attr=request.form.to_dict()
        print(attr)
        print(type(attr['url']))
        attr.pop('url')
        headers=attr
        req=requests.get(url,headers=headers)
        res_headers = req.headers
        #DEFAULT_CONNECTION_URL = "mongodb://localhost:27017/"
        #DB_NAME = "MultipleDatabase"


        # Establish a connection with mongoDB
        #client = pymongo.MongoClient(DEFAULT_CONNECTION_URL)

        # Create a DB
        #dataBase = client[DB_NAME]
        #collection_name = "Test_collection"
        #collection = dataBase[collection_name]
        #record={'request':headers,'response':res_headers}
        #collection.insert_one(record)

        content = {"res_headers":res_headers,"r_url":req.url,'req':req}
        return render_template('result.html',**content)
    except Exception:
        return render_template('index.html',query="No such url exist!")
if __name__ == "__main__":
    app.run(port=8080,debug=True)