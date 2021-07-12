from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/result')
def result():
    return render_template('result.html', name=session["name"], form1=session["form1"], form2=session["form2"], animal=session["animal"], comments=session["comments"])


@app.route('/processing', methods=["POST"])
def proc():
    print(request.form)
    session["name"] = request.form['name']
    session["form1"] = request.form['form1']
    session["form2"] = request.form['form2']
    session["comments"] = request.form["bigText"]
    return redirect('/result')


if __name__ == "__main__":
    app.secret_key = "he's here! the phantom of the opera!"
    app.run(debug=True)
