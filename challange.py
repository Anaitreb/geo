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
    """Geocode the DataFrame using the Address column"""
    pass

def download_csv(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}">Download CSV File</a> (right-click and save as &lt;some_name&gt;.csv)'
    return href

def main():
    """ Manage Application interface""" 
    pass