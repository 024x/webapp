from flask import Flask,request,json
import os
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Webhooks with Python'

@app.route('/githubIssue',methods=['POST','GET'])
def githubIssue():
    data = request.json
    print(data)
    return data
 
if __name__ == '__main__':
    app.run(host = '0.0.0.0' , port = os.environ.get('PORT', 5000),debug=True)