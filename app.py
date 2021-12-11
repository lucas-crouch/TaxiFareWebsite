import streamlit as st
import datetime as dt
import requests

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')
'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''
'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''

url = 'https://taxifare.lewagon.ai/predict'

pickup_datetime = dt.datetime.now()

if url == 'https://taxifare.lewagon.ai/predict':

    pickup_longitude = st.text_input("pickup longitude")
    pickup_latitude = st.text_input("pickup_latitude")
    dropoff_longitude = st.text_input("dropoff_longitude")
    dropoff_latitude = st.text_input("dropoff_latitude")
    passenger_count = st.text_input("passenger_count")

    params = {
        "pickup_datetime": pickup_datetime,
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count
    }

if pickup_longitude and pickup_latitude and dropoff_longitude and dropoff_latitude and passenger_count:
    """
    response = requests.get(
        f'https://taxifare.lewagon.ai/predict?pickup_datetime={time}&pickup_longitude=40.7614327&pickup_latitude=-73.9798156&dropoff_longitude=40.6513111&dropoff_latitude=-73.8803331&passenger_count=2')
    """

    response = requests.get(url, params)
    price = round(response.json()["prediction"], 2)
    st.markdown(f"This trip will cost you {price}$")
