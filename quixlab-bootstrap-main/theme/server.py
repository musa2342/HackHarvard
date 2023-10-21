from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def serve_home():
    return render_template('index.html')


@app.route('/api/data')
def return_all():
    return # return health data

if __name__=='__main__':
    app.run(host="0.0.0.0",port=8000)

