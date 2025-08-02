from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/home")
def home():
    return "home page"
if __name__=="__main__":
    app.run(host='0.0.0.0',port=10000)