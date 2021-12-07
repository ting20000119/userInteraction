from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from functools import wraps
import requests
import json
import time
import datetime
import requests
from requests.structures import CaseInsensitiveDict
import treemaker

app = Flask(__name__)


@app.route('/')
def index():
    input = open('graphFile.json')
    jjson = json.load(input)
    # print(jjson)
    input.close()
    return render_template('d3.html', json=jjson)


@app.route('/submissiontree')
def sub_tree():
    sub_id = request.args.get('id', default='j3ygfd', type=str)
    print(sub_id)

    input_file = open('less.json')
    jjson = json.load(input_file)
    input_file = open('less.json')
    json_array = json.load(input_file)
    # print(json_array)
    json_array = treemaker.getpairlist(sub_id)
    arr = []
    json_obj = {}
    json_obj['marker'] = {"radius": 13}
    json_obj['dataLabels'] = {
        "enabled": True,
        "linkFormat": "",
        "allowOverlap": True,
        "style": {"textOutline": False}
    }
    pairArr = []
    for obj in json_array:
        json_pair = []
        for key in obj.keys():
            json_pair.append(key)
            json_pair.append(obj[key]['parentAuthor'])
            break
            # print(key)
            # print(obj[key]['parentAuthor'])
        pairArr.append(json_pair)
    json_obj['data'] = pairArr
    nodeArr = []
    colorDict = {}
    colorDict['dem'] = "#0000ff"
    colorDict['rep'] = "#E8544E"
    colorDict['error'] = "#808080"
    for obj in json_array:
        nodeDictKid = {}
        nodeDictParent = {}
        for key in obj.keys():
            nodeDictKid['id'] = key
            nodeDictParent['id'] = obj[key]['parentAuthor']
            nodeDictKid['marker'] = {"radius": 20}
            nodeDictParent['marker'] = {"radius": 20}
            nodeDictKid['color'] = colorDict[obj[key]['childLeaning']]
            nodeDictParent['color'] = colorDict[obj[key]['parentLeaning']]
            break
        nodeArr.append(nodeDictKid)
        nodeArr.append(nodeDictParent)
    json_obj['nodes'] = nodeArr
    arr.append(json_obj)
    # print(arr)
    input_file.close()
    #print(json.dumps(arr,indent = 2, separators=(',', ': ')))
    #print(json.dumps(jjson,indent = 2, separators=(',', ': ')))
    return render_template('homepage.html', arr=arr, jjson=None)


if __name__ == '__main__':
    app.run(debug=True)
