from flask import Flask,request,json
import os
app = Flask(__name__)
import logging
from logging import warning,error,info,debug
import requests
@app.route('/')
def hello():
    return {'working':True}

 
if __name__ == '__main__':
    app.run(host = '0.0.0.0' , port = os.environ.get('PORT', 5000),debug=True)
