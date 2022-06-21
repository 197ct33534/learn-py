from flask import Flask
ungdung = Flask(__name__)
@ungdung.route('/')
def hello():
    return ('xin chào!')
if __name__ == "__main__": 
    ungdung.run()