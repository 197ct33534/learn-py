from flask import abort,redirect,url_for,Flask,request
app = Flask(__name__)
@app.route('/')
def index():
    return redirect(url_for('login'))
@app.route('/login')
def login():
    abort(401)
@app.route('/upload',method=['POST','GET'])
def upload_file():
    if(request.method == 'POST'):
        f = request.files['the_files']
        f.save('/save/www/uploads/upload_file.txt')
if __name__ == '__main__':
    app.run(port=5050)