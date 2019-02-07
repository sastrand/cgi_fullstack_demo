from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def greeter():
    return render_template("greeter.html")

@app.route('/', methods=['POST'])
def greeter_post():
    text = request.form['text']
    return render_template('hello.html', name=text)

if __name__=="__main__":
    app.debug = True
    app.run()

