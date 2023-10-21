# Importing the API and instantiating the client using your keys
from terra.base_client import Terra
# Datetime objects required as input to some API calls
from datetime import datetime

API_KEY = "iwqBZa7s6pln7v8h8zRF1l3OWbTLyzsW"
DEV_ID = "earlham-testing-DoaYyfwkHC"
SECRET = "iwqBZa7s6pln7v8h8zRF1l3OWbTLyzsW"

terra = Terra(API_KEY, DEV_ID, SECRET)

widget_response = terra.generate_widget_session(
    reference_id="USER ID IN YOUR APP",
    providers=["CRONOMETER", "OURA"],
    auth_success_redirect_url="http://localhost:8080/connectionSuccess",
    auth_failure_redirect_url="https://failure.url",
    language="en"
).get_parsed_response()

print(widget_response)


# Create a user object
USER_ID = "e036976a-027d-4eb2-8b9f-22ae3afbb382"
terra_user = terra.from_user_id(USER_ID)

# Get the nutrition data from start date to current time
nutrition_resp = terra_user.get_nutrition(start_date=datetime.strptime('2023-03-29','%Y-%m-%d'), end_date=datetime.now(), to_webhook = False )
nutrition_resp_json = nutrition_resp.get_json()



