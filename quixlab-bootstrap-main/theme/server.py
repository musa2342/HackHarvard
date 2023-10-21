from flask import Flask, request, render_template, url_for, redirect
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
    

@app.route("/home")
def home():
    return redirect(url_for('index'))

@app.route("/app-profile")
def app_profile():
    return render_template('app-profile.html')

@app.route("/page-login")
def page_login():
    return render_template('page-login.html')

@app.route("/page-register")
def page_register():
    return render_template('page-register.html')

@app.route("/app-calender")
def app_calender():
    return render_template('app-calender.html')



@app.route('/api/data')
def return_all():
    return # return health data

if __name__=='__main__':
    app.run(debug=True)

