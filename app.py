from flask import Flask,render_template,url_for,send_from_directory


app=Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/resume")
def resume():
    directory="static/files"
    filename="resume.pdf"
    return send_from_directory(directory,filename,as_attachment=True)



if __name__=="__main__":
    app.run(debug=True)
