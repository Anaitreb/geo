import time
import base64

import streamlit as st
import pandas as pd

import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

import matplotlib.pyplot as plt

st.title("Geocoding Application in Python")
st.image("images/geocoding.jpg")

file = st.sidebar.file_uploader("Upload a file", type=["csv"])


def geocode(df, col):
    "Geocode the DataFrame using the Address column"
    locator = Nominatim(user_agent="myGeocoder")
    geocode = RateLimiter(locator.geocode, min_delay_seconds=1)
    df['location'] = df[col].apply(geocode)

    df['point'] = df['location'].apply(
        lambda loc: tuple(loc.point) if loc else None)

    df[['lat', 'lon', 'alt']] = pd.DataFrame(
        df['point'].tolist(), index=df.index)

    return df


def download_csv(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}">Download CSV File</a> (right-click and save as &lt;some_name&gt;.csv)'
    return href


def main():
    if file is not None:
        # Read and Display the Dataframe
        df = pd.read_csv(file)
        st.write(df.head())
        st.write(df.shape)

        # Create Select Box with the Dataframe Columns
        options = df.columns.tolist()
        selection = st.sidebar.selectbox("Select the Address Column", options)
        st.write("Your current sellection is: ", selection)

        # Geocode
        if st.sidebar.checkbox("Start Geocoding"):
            with st.spinner('Geocoding Hold tight...'):
                time.sleep(5)
            df = geocode(df, selection)

            st.success('Geocoding finished successfully!')
            st.write(df.head())

        # Download the csv File
        st.markdown(download_csv(df), unsafe_allow_html=True)


if __name__ == "__main__":
    main()
