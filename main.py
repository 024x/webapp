from flask import Flask,request,json
import os
import PIL
from PIL import Image, ImageDraw, ImageFont
app = Flask(__name__)
import logging
from logging import warning,error,info,debug
import requests
from flask import send_file
@app.route('/')
def hello():
    return {'working':True}

@app.route('/hi')
def he():
    txt = "Hello"
    img = Image.open("white.jpg")
    d1 = ImageDraw.Draw(img)
    myFont = ImageFont.truetype("ds.otf", 50)
    d1.text((65, 10), txt, fill =(0, 0, 0),font=myFont)
    img.save("result.jpg")
    filename = "result.jpg"
    return send_file(filename, mimetype='image/jpeg')
if __name__ == '__main__':
    app.run(host = '0.0.0.0' , port = os.environ.get('PORT', 5000),debug=True)
