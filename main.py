import json
from flask import Flask,request
from pprint import pprint


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def login():
    data=None
    with open('data.json') as file:
        tmp= json.loads(file.read())
        data = tmp
    if(data is None):
        data=[]
    if request.method=='GET':
        return data
    if request.method == 'POST':
        print(request.data)


        with open('data.json','w') as file:
            data.append(request.json)
            file.write(json.dumps(data,indent=2))
            return data
