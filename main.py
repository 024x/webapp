import os
import PIL
import logging
import requests 
from flask import Flask,request,json,send_file
from logging import warning,error,info,debug
from PIL import Image, ImageDraw, ImageFont


app = Flask(__name__)

@app.route('/')
def test():
  return {'working':True}

@app.route('/hi/<text>',methods=['GET'])
def hello():
  txt = "Hello"
  img = Image.open("nordwood-themes-R53t-Tg6J4c-unsplash.jpg")
  d1 = ImageDraw.Draw(img)
  myFont = ImageFont.truetype("ds.otf", 50)
  d1.text((65, 10), txt, fill =(0, 0, 0),font=myFont)
  img.save("result.jpg")
  filename = "result.jpg"
  return send_file(filename, mimetype='image/jpeg')

@app.route('/write', methods=['GET'])
def write():
   txt = request.args.get('text', None)
   img = Image.open("nordwood-themes-R53t-Tg6J4c-unsplash.jpg")
   d1 = ImageDraw.Draw(img)
   myFont = ImageFont.truetype("ds.otf", 50)
   d1.text((65, 10), txt, fill =(0, 0, 0),font=myFont)
   img.save("result.jpg")
   filename = "result.jpg"
   return send_file(filename, mimetype='image/jpeg')
    
    
if __name__ == '__main__':
    app.run(host = '0.0.0.0' , port = os.environ.get('PORT', 5000),debug=True)
