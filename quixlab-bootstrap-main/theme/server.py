from flask import Flask, request, render_template, url_for, redirect
import logging
import flask
from terra.base_client import Terra
from datetime import datetime
import requests

logging.basicConfig(level=logging.INFO)
_LOGGER = logging.getLogger("app")

API_KEY = "iwqBZa7s6pln7v8h8zRF1l3OWbTLyzsW"
DEV_ID = "earlham-testing-DoaYyfwkHC"
SECRET = "iwqBZa7s6pln7v8h8zRF1l3OWbTLyzsW"

terra = Terra(API_KEY, DEV_ID, SECRET)

auth_resp = terra.generate_authentication_url(
    reference_id="Sharon",
    resource="GARMIN",
    auth_success_redirect_url="http://localhost:8080/",
    auth_failure_redirect_url="http://localhost:8080/page-login",
).get_parsed_response()

auth_url= auth_resp.auth_url
user_id=auth_resp.user_id



# terra = Terra(api_key='API-KEY', dev_id='DEV-ID', secret="SIGNING-SECRET")

app = flask.Flask(__name__)

@app.route("/consumeTerraWebhook", methods=["POST"])
def consume_terra_webhook() -> flask.Response:
    # body_str = str(request.get_data(), 'utf-8')
    body = request.get_json()
    _LOGGER.info(
        "Received webhook for user %s of type %s",
        body.get("user", {}).get("user_id"),
        body["type"])
    verified = terra.check_terra_signature(request.get_data().decode("utf-8"), request.headers['terra-signature'])
    if verified:
      return flask.Response(status=200)
    else:
      return flask.Response(status=403)
    
# app = Flask(__name__)

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


@app.route("/page-login-terra")
def page_login_terra():
    return redirect(auth_url)

# @app.route('/user/Sharon')
# def user():
#     return render_template('http://localhost:8080/index/')


@app.route("/page-register")
def page_register():
    return render_template('page-register.html')

@app.route("/app-calender")
def app_calender():
    return render_template('app-calender.html')

@app.route("/connectionSuccess")
def connectionSuccess():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host="localhost", port=8080)
