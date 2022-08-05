import os
import PIL
import logging
import requests 
from flask import Flask,request,json,send_file
from logging import warning,error,info,debug
from PIL import Image, ImageDraw, ImageFont
import textwrap
from assets import write

app = Flask(__name__)

@app.route('/')
def test():
  return {'working':True}

@app.route('/write', methods=['GET'])
def write():
   text = request.args.get('text', None)
   write.write(text)
