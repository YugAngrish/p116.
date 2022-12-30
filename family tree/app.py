from flask import Flask, render_template
app = Flask(__name__)
#in the function return render_template(‘index.html’)
@app.route("/index")
def me():
    #Create a variable
    myname = 'Flask1'
    myage = '16'
    return render_template('index.html', name = myname , age = myage)
@app.route("/mother")
def mother():
    #Create a variable
    myname = 'Flask2'
    myage = '36'
    return render_template('mother.html', name = myname , age = myage)   
app.run(debug=True)
@app.route("/friend")
def friend():
    #Create a variable
    myname = 'Flask3'
    myage = '16'
    return render_template('friend.html', name = myname , age = myage)   
app.run(debug=True)
@app.route("/father")
def father():
    #Create a variable
    myname = 'Flask4'
    myage = '38'
    return render_template('father.html', name = myname , age = myage)   
app.run(debug=True)

