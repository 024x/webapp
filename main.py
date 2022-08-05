import os
import PIL
import logging
import requests 
from flask import Flask,request,json,send_file
from logging import warning,error,info,debug
from PIL import Image, ImageDraw, ImageFont
import textwrap

app = Flask(__name__)

@app.route('/')
def test():
  return {'working':True}

@app.route('/write', methods=['GET'])
def write():
   text = request.args.get('text', None)
   value = text
   wrapper = textwrap.TextWrapper(width=65)
   word_list = wrapper.wrap(text=value)
   s = []
   for element in word_list:
       s.append(element)
   hmm = "\n"
   txt = (hmm.join(s))
   warning(txt)
   img = Image.open("nordwood-themes-R53t-Tg6J4c-unsplash.jpg")
   d1 = ImageDraw.Draw(img)
   myFont = ImageFont.truetype("ds.otf", 130)
   d1.text((65, 10), txt, fill =(0, 0, 0),font=myFont)
   img.save("result.jpg")
   filename = "result.jpg"
   return send_file(filename, mimetype='image/jpeg')

    
if __name__ == '__main__':
    app.run(host = '0.0.0.0' , port = os.environ.get('PORT', 5000),debug=True)
