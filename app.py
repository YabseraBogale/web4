
from flask import Flask,jsonify,request,render_template,url_for,send_from_directory

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/resume")
def resume():
    directory="static/files"
    filename="resume.pdf"
    return send_from_directory(directory,filename,as_attachment=True)

@app.route("/blog/<name>")
def blog(name):

    return render_template(name)

@app.route("/news",methods=['POST','GET'])
def newletter():
    if request.method=='POST':
        print(request.form['email'])
        return jsonify({'ok':200})
    return render_template("base.html")

if __name__=="__main__":
    app.run(debug=True)
