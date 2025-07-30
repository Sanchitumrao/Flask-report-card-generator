from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/success/<float:score>/<float:s>/<float:m>/<float:e>")
def success(score,s,m,e):
    return render_template("results.html",result="PASS",score=score,science=s,maths=m,english=e)

@app.route("/fail/<float:score>/<float:s>/<float:m>/<float:e>")
def fail(score,s,m,e):
    return render_template("results.html",result="FAIL",score=score,science=s,maths=m,english=e)

@app.route("/submit",methods=["POST","GET"])
def submit():
    totalscore=0
    if request.method == "POST":
        science =float(request.form["science"])
        maths = float(request.form["maths"])
        english =float( request.form["english"])
        totalscore =float (((science + maths + english)/3).__round__(3))

        if totalscore>=50:
           return redirect(url_for("success",score=totalscore,s=science,m=maths,e=english))
        else:
           return redirect(url_for("fail",score=totalscore,s=science,m=maths,e=english))

if __name__ == "__main__":
    app.run(debug=True)