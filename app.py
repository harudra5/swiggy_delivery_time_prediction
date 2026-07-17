import streamlit as st
import pandas as pd
import pickle

with open("swiggy_delivery_time_prediction.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Swiggy Delivery Time Prediction")

age = st.number_input("Age", 18, 60, 25)
ratings = st.number_input("Ratings", 1.0, 5.0, 4.5)
weather = st.selectbox("Weather", ["sunny","cloudy","fog","stormy","sandstorms","windy"])
traffic = st.selectbox("Traffic", ["low","medium","high","jam"])
vehicle_condition = st.selectbox("Vehicle Condition",[0,1,2])
type_of_order = st.selectbox("Type of Order",["Snack","Meal","Drinks","Buffet"])
type_of_vehicle = st.selectbox("Vehicle",["motorcycle","scooter","electric_scooter"])
multiple_deliveries = st.selectbox("Multiple Deliveries",[0,1,2,3])
festival = st.selectbox("Festival",["yes","no"])
city_type = st.selectbox("City Type",["Urban","Semi-Urban","Metropolitan"])
city_name = st.text_input("City Name")
order_day = st.number_input("Order Day",1,31)
order_month = st.number_input("Order Month",1,12)
order_day_of_week = st.selectbox("Day of Week",["monday","tuesday","wednesday","thursday","friday","saturday","sunday"])
is_weekend = st.selectbox("Weekend",[0,1])
pickup_time_minutes = st.number_input("Pickup Time (Minutes)",0,60)
order_time_hour = st.number_input("Order Hour",0,23)
order_time_of_day = st.selectbox("Order Time",["Morning","Afternoon","Evening","Night"])
distance = st.number_input("Distance (km)",0.0)

if st.button("Predict Delivery Time"):

    data = pd.DataFrame({
        "age":[age],
        "ratings":[ratings],
        "weather":[weather],
        "traffic":[traffic],
        "vehicle_condition":[vehicle_condition],
        "type_of_order":[type_of_order],
        "type_of_vehicle":[type_of_vehicle],
        "multiple_deliveries":[multiple_deliveries],
        "festival":[festival],
        "city_type":[city_type],
        "city_name":[city_name],
        "order_day":[order_day],
        "order_month":[order_month],
        "order_day_of_week":[order_day_of_week],
        "is_weekend":[is_weekend],
        "pickup_time_minutes":[pickup_time_minutes],
        "order_time_hour":[order_time_hour],
        "order_time_of_day":[order_time_of_day],
        "distance":[distance]
    })

    prediction = model.predict(data)

    st.success(f"Estimated Delivery Time: {prediction[0]:.2f} minutes")