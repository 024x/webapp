from flask import Flask,request,json
import os
app = Flask(__name__)
import logging
from logging import warning,error,info,debug
from pyrogram import Client
import requests
bot =  Client(
	    "my_Bot",
	    api_hash="fd7acd07303760c52dcc0ed8b2f73086",
	    api_id=2171111,
	    bot_token="1840298314:AAFUMtMNiJpyBBt4tyGfuq_yO3ZXl88jxwk",
	)
@app.route('/')
def hello():
    return 'Webhooks with Python'

@app.route('/githubIssue',methods=['POST','GET'])
def githubIssue():
    data = request.json
    print(data)
    warning(data)
    with open('json.txt','w') as f:
        f.write(str(data))
    try:
        with bot:
            bot.send_document('s4tyendra','json.txt')
    except:
        bot.send_document('s4tyendra','json.txt')
    warning(data)
    return data
 
if __name__ == '__main__':
    app.run(host = '0.0.0.0' , port = os.environ.get('PORT', 5000),debug=True)