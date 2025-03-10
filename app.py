import os
from flask import Flask,jsonify,request,render_template,url_for,send_from_directory
from Database.HEEE import heee 
from Database.NEWLETTER import newletter

app=Flask(__name__)
app.config["UPLOAD_FOLDER"]="Upload/"
exit_exam=heee()
news_letter=newletter()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/resume")
def resume():
    directory="static/files"
    filename="resume.pdf"
    return send_from_directory(directory,filename,as_attachment=True)


@app.route("/come",methods=["GET","POST"])
def come():
    if request.method=="POST":
        if "video" not in request.files:
            return "no video uploaded"
        video = request.files["video"]
        if video.filename=="":
            return "no video"
        else:
            video_path=os.path.join(app.config["UPLOAD_FOLDER"],video.filename)
            video.save(video_path)
            return "ok"
    return render_template("come.html")

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

@app.route("/news",methods=['POST','GET'])
def newletter():
    if request.method=='POST':
        print(request.form['email'])
        return jsonify({'ok':200})
    return render_template("base.html")

if __name__=="__main__":
    app.run(debug=True)
