from flask import Flask, render_template, url_for, request
app = Flask(__name__)
print(__name__)

@app.route('/')
def home_page():
    return render_template('./templates/index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

app.run(host='127.0.0.1', threaded=True)

