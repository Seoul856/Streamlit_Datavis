import streamlit as st
import pandas as pd
import plotly.express as px
import json
import random
import mysql.connector

# Connect to the MySQL database
db_connection = mysql.connector.connect(
    host="localhost",
    user="username",
    database="Groundwater"
)

# Load data from MySQL database
query = "SELECT * FROM water_data5"
df = pd.read_sql(query, con=db_connection)

# Load GeoJSON data
with open('karnataka.json', 'r') as f:
    geojson = json.load(f)

# ... (rest of your code remains unchanged)
