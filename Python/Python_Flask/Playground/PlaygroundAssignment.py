from flask import Flask, render_template
app = Flask(__name__)
@app.route('/play/<number>')
def play1(number):
    return render_template("PlaygroundAssignment.html",num=int(number),bgcolor="lightblue")

@app.route('/play')
def play2():
    return render_template("PlaygroundAssignment.html",num=int(3),bgcolor="lightblue")

@app.route('/play/<number>/<color>')
def play3(number,color):
    return render_template("PlaygroundAssignment.html",num=int(number),bgcolor=color)

if __name__=="__main__":
    app.run(debug=True)