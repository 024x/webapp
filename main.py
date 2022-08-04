import os
import PIL
import logging
import textwrap 
import requests 
from urllib.parse import quote as q
from flask import Flask,request,json,send_file
from logging import warning,error,info,debug
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

def wrap(value):
  wrapper = textwrap.TextWrapper(width=65)
  word_list = wrapper.wrap(text=value)
  s = []
  for element in word_list:
      s.append(element)
  hmm = "\n"
  x = q(hmm.join(s))
  return x

@app.route('/')
def test():
  return {
    'Owner': Naveen,
    'Telegram': Naveen_xD,
    'GitHub': Naveen-xd2580
  }

@app.route('/write', methods=['GET'])
def write():
   txxt = request.args.get('text', None)
   txt = wrap(txxt)
   img = Image.open("nordwood-themes-R53t-Tg6J4c-unsplash.jpg")
   d1 = ImageDraw.Draw(img)
   myFont = ImageFont.truetype("ds.otf", 120)
   d1.text((65, 10), txt, fill =(0, 0, 0),font=myFont)
   img.save("result.jpg")
   filename = "result.jpg"
   return send_file(filename, mimetype='image/jpeg')
    
    
if __name__ == '__main__':
    app.run(host = '0.0.0.0' , port = os.environ.get('PORT', 5000),debug=True)
