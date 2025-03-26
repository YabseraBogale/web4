from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
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


@app.route("/test")
def test():
    return render_template("test.html")

@app.route("/exit_exam_question_answer_api")
def exit_exam_question_answer_api():
    result=exit_exam.get_random_100_question_heee()
    if type(result)==type([]):
        return jsonify(result)
    return jsonify([])

@app.route("/blog/<name>")
def blog(name):
    return render_template(name)


@app.route("/dictionary_for_software")
def random_software_fact():
    facts=exit_exam.random_software_fact()
    return render_template("dictionary_for_software.html",Facts=facts)

if __name__=="__main__":
    app.run(debug=True)
