from flask import Flask, render_template
app = Flask(__name__)
#defult 8*8
@app.route('/')
def Checkerboard1():
    return render_template("Checkerboard.html",rows=int(8/2),columns=int(8/2),bgcolor1="lightblue",bgcolor2="rosybrown")

#8*any number
@app.route('/<row>')
def Checkerboard2(row):
    return render_template("Checkerboard.html",rows=int(int(row)/2),columns=int(8/2),bgcolor1="lightblue",bgcolor2="rosybrown")

@app.route('/<row>/<column>')
def Checkerboard3(row,column):
    return render_template("Checkerboard.html",rows=int(int(row)/2),columns=int(int(column)/2),bgcolor1="lightblue",bgcolor2="rosybrown")

@app.route('/<row>/<column>/<color1>/<color2>')
def Checkerboard4(row,column,color1,color2):
    return render_template("Checkerboard.html",rows=int(int(row)/2),columns=int(int(column)/2),bgcolor1=color1,bgcolor2=color2)

if __name__=="__main__":
    app.run(debug=True)