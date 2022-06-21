from flask import Flask,render_template
app = Flask(__name__,static_folder='D:\\bai tap python\\python_nangcao\learn-py\\Lab6\\thuchanh\\bt10\\templates\static')
@app.route('/')
def index():
    languages = [ {'STT':1, 'ten': "Python"}, {'STT':2, 'ten': "Java"} , {'STT':3, 'ten': "C++"}]
    languages.append({'STT':4, 'ten': ".NET" })
    languages.append({'STT':5, 'ten': "Matlab" })
    return render_template('abc.html', ngon_ngu = languages)
if __name__ == '__main__':
    app.run(port=5050)