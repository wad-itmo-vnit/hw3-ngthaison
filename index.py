from flask import Flask, render_template, send_file, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')
   
app.run(host="localhost", port=5000)