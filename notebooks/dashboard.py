import streamlit as st
import pandas as pd
import psycopg2
import plotly.express as px

# ---------- CONFIG ----------
st.set_page_config(page_title="Taxi Dashboard", layout="wide")

# ---------- CONNECTION ----------
@st.cache_data
def load_data():
    conn = psycopg2.connect(
        host="localhost",
        database="nyc_taxi_db",
        user="postgres",
        password=""
    )

    query = """
    SELECT *
    FROM fact_trips
    LIMIT 500000
    """

    df = pd.read_sql(query, conn)
    conn.close()
    return df

df = load_data()

# ---------- KPIs ----------
st.title("🚖 Taxi Data Dashboard")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Trips", len(df))
col2.metric("Avg Fare", round(df["fare_amount"].mean(), 2))
col3.metric("Avg Distance", round(df["trip_distance"].mean(), 2))
col4.metric("Avg Duration", round(df["trip_duration"].mean(), 2))

# ---------- DEMAND OVER TIME ----------
st.subheader("Demand Over Time")

df["pickup_datetime"] = pd.to_datetime(df["pickup_datetime"])
demand = df.groupby(df["pickup_datetime"].dt.date).size().reset_index(name="trips")

fig1 = px.line(demand, x="pickup_datetime", y="trips")
st.plotly_chart(fig1, use_container_width=True)

# ---------- TOP ZONES ----------
st.subheader("Top Zones")

top_zones = df.groupby("pickup_location_id").size().reset_index(name="trips").sort_values(by="trips", ascending=False).head(10)

fig2 = px.bar(top_zones, x="pickup_location_id", y="trips")
st.plotly_chart(fig2, use_container_width=True)

# ---------- FARE VS DISTANCE ----------
st.subheader("Fare vs Distance")

fig3 = px.scatter(df.sample(10000), x="trip_distance", y="fare_amount", opacity=0.5)
st.plotly_chart(fig3, use_container_width=True)

# ---------- ML: PREDICTED VS ACTUAL ----------
if "prediction" in df.columns:
    st.subheader("Predicted vs Actual Fare")

    fig4 = px.scatter(df.sample(10000), x="fare_amount", y="prediction")
    st.plotly_chart(fig4, use_container_width=True)

# ---------- CLUSTERS ----------
if "cluster" in df.columns:
    st.subheader("Cluster Distribution")

    fig5 = px.histogram(df, x="cluster")
    st.plotly_chart(fig5, use_container_width=True)