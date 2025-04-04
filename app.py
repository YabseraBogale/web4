from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask import Flask,jsonify,request,render_template,url_for,send_from_directory
from Database.HEEE import heee 


app=Flask(__name__)
limiter=Limiter(
    get_remote_address,
    app=app,
)

exit_exam=heee()

@app.errorhandler(429)
def ratelimit_handler(e):
    return render_template("err429.html",err=e)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/resume")
def resume():
    directory="static/files"
    filename="resume.pdf"
    return send_from_directory(directory,filename,as_attachment=True)


@app.route("/test")
@limiter.limit("1 per day")
def test():
    return render_template("test.html")

@app.route("/exit_exam_question_answer_api")
@limiter.limit("1 per day")
def exit_exam_question_answer_api():
    result=exit_exam.get_random_100_question_heee()
    if type(result)==type([]):
        return jsonify(result)
    return jsonify([])

@app.route("/blog/<name>")
def blog(name):
    return render_template(name)

@app.route("/balance_sheet")
def balance_sheet():
    return render_template("balance_sheet.html")

@app.route("/dictionary_for_software")
def random_software_fact():
    facts=exit_exam.random_software_fact()
    return render_template("dictionary_for_software.html",Facts=facts)

if __name__=="__main__":
    app.run(debug=True)
