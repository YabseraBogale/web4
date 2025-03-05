
from flask import Flask,jsonify,request,render_template,url_for,send_from_directory
from Database.HEEE import heee 

app=Flask(__name__)
exit_exam=heee()


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/resume")
def resume():
    directory="static/files"
    filename="resume.pdf"
    return send_from_directory(directory,filename,as_attachment=True)

@app.route("/exit_exam_question_answer_api")
def exit_exam_question_answer_api():
    result=exit_exam.get_random_100_question_heee()
    if type(result)==type([]):
        return jsonify()
    return jsonify([])

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
