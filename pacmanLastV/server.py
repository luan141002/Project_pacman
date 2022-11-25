import os
from flask import Flask
from app_class import *
app = Flask(__name__)
port = int(os.environ.get('PORT', 3000))
#@app.route('/')
def hello():
    return "Hello World!"
if __name__ == '__main__':
    app = App()
    #app.run()
    app.run(host='0.0.0.0', port=port)