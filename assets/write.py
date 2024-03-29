import os
import PIL
import logging
import requests
import textwrap 
from flask import Flask,request,json,send_file
from logging import warning,error,info,debug
from PIL import Image, ImageDraw, ImageFont

def write(text):
   value = text
   wrapper = textwrap.TextWrapper(width=65)
   word_list = wrapper.wrap(text=value)
   s = []
   for element in word_list:
       s.append(element)
   hmm = "\n"
   txt = (hmm.join(s))
   warning(txt)
   s1 = textwrap.indent(txt, prefix=' ')
   img = Image.open("nordwood-themes-R53t-Tg6J4c-unsplash.jpg")
   d1 = ImageDraw.Draw(img)
   myFont = ImageFont.truetype("ds.otf", 130)
   d1.text((65, 10), s1, fill =(0, 0, 0),font=myFont)
   img.save("result.jpg")
   filename = "result.jpg"
   return send_file(filename, mimetype='image/jpeg')
