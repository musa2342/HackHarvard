from flask import Flask, request, render_template, url_for, redirect
import logging
from terra.base_client import Terra

logging.basicConfig(level=logging.INFO)
_LOGGER = logging.getLogger("app")

terra = Terra(api_key='API-KEY', dev_id='DEV-ID', secret="SIGNING-SECRET")

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

@app.route("/connectionSuccess")
def connectionSuccess():
    return redirect(url_for('index'))


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
    


if __name__=='__main__':
    app.run(host="localhost", port=8080)

