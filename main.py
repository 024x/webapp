from server import app
if __name__ == '__main__':
    requests.get('https://api.telegram.org/bot1963945108:AAFyo9bg2k4BImXsAHgghYg2bEkkdaiDe4g/sendMessage?chat_id=-1001426113453&text=Webserverstarted')
    app.run(host = '0.0.0.0' , port = os.environ.get('PORT', 5000),debug=True)
