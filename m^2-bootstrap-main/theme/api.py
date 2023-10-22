# Importing the API and instantiating the client using your keys
from terra.base_client import Terra
# Datetime objects required as input to some API calls
from datetime import datetime
# import requests

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

print(auth_resp)

# widget_response = terra.generate_widget_session(
#     reference_id="Sharon",
#     providers=["GARMIN","WITHINGS","FITBIT","GOOGLE","OURA","WAHOO","PELOTON","ZWIFT","TRAININGPEAKS","FREESTYLELIBRE","DEXCOM","COROS","HUAWEI","OMRON","RENPHO","POLAR","SUUNTO","EIGHT","APPLE","CONCEPT2","WHOOP","IFIT","TEMPO","CRONOMETER","FATSECRET","NUTRACHECK","UNDERARMOUR"],
#     auth_success_redirect_url="http://localhost:8080/",
#     auth_failure_redirect_url="http://localhost:8080/page-login",
#     language="en"
# ).get_parsed_response()
# print(widget_response)

# import urllib.parse

# deeplink = urllib.parse.urljoin('http://localhost:8080/')
# print(deeplink.path())

# import requests

# url = "https://api.tryterra.co/v2/auth/generateAuthToken"

# headers = {
#     "accept": "application/json",
#     "dev-id": "earlham-testing-DoaYyfwkHC",
#     "x-api-key": "iwqBZa7s6pln7v8h8zRF1l3OWbTLyzsW"
# }

# response = requests.post(url, headers=headers)
# print(response.json()['token'])

# import requests

# url = "https://api.tryterra.co/v2/auth/authenticateUser?resource=GARMIN"

# payload = {
#     "reference_id": response.json()['token'],
#     "auth_success_redirect_url": "http://localhost:8080/",
#     "auth_failure_redirect_url": "http://localhost:8080/page-login"
# }
# headers = {
#     "accept": "application/json",
#     "dev-id": "earlham-testing-DoaYyfwkHC",
#     "content-type": "application/json",
#     "x-api-key": "iwqBZa7s6pln7v8h8zRF1l3OWbTLyzsW"
# }

# response = requests.post(url, json=payload, headers=headers)

# print(response.json()['auth_url'])

# Create a user object
# USER_ID = "e036976a-027d-4eb2-8b9f-22ae3afbb382"
# terra_user = terra.from_user_id(USER_ID)

# Get the nutrition data from start date to current time
# nutrition_resp = terra_user.get_nutrition(start_date=datetime.strptime('2023-03-29','%Y-%m-%d'), end_date=datetime.now(), to_webhook = False )
# nutrition_resp_json = nutrition_resp.get_json()



