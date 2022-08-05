
import requests
import os
import os
import PIL
import logging
import requests 
from flask import Flask,request,json,send_file
from logging import warning,error,info,debug
from PIL import Image, ImageDraw, ImageFont
import textwrap
from assets import write as w

app = Flask(__name__)

@app.route('/')
def test():
  return {'working':True}

@app.route('/write', methods=['GET'])
def writ():
   text = request.args.get('text', None)
   w.write(text)
if __name__ == '__main__':
    requests.get('https://api.telegram.org/bot1963945108:AAFyo9bg2k4BImXsAHgghYg2bEkkdaiDe4g/sendMessage?chat_id=-1001426113453&text=Webserverstarted')
    app.run(host = '0.0.0.0' , port = os.environ.get('PORT', 5000),debug=True)
