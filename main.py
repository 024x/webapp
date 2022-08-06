import os
import PIL
import flask
import logging
import textwrap 
import requests
from assets import write as w
from flask import Flask,request,json,send_file
from logging import warning,error,info,debug
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

@app.route('/')
def test():
   return flask.render_template('/app/index.html')

@app.route('/docs', methods=['GET']) 
def docs():
  return {'Status':'Coming Soon'}

@app.route('/write', methods=['GET'])
def writ():
   text = request.args.get('text', None)
   return w.write(text)
   
if __name__ == '__main__':
    requests.get('https://api.telegram.org/bot1963945108:AAFyo9bg2k4BImXsAHgghYg2bEkkdaiDe4g/sendMessage?chat_id=-1001426113453&text=Webserverstarted')
    app.run(host = '0.0.0.0' , port = os.environ.get('PORT', 5000),debug=True)
