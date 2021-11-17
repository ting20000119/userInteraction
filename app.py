from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from functools import wraps
import requests
import json
import time
import datetime
import requests
from requests.structures import CaseInsensitiveDict

app = Flask(__name__)


@app.route('/')
def index():
    input_file = open('lessnewdeal.json')
    json_array = json.load(input_file)
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
    print(arr)
    input_file.close()
    return render_template('homepage.html', arr=arr)


if __name__ == '__main__':
    app.run(debug=True)
