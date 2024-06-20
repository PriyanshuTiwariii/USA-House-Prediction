import streamlit as st
import numpy as np
import pickle 

pickle_out=open("classifier.pkl","rb")

model=pickle.load(pickle_out)

st.title('USA Housing Price Prediction')

st.write("Enter the following details to predict the house price:")

# Define input fields
avg_area_income = st.number_input('Avg. Area Income', min_value=0)
avg_area_house_age = st.number_input('Avg. Area House Age', min_value=0)
avg_area_number_of_rooms = st.number_input('Avg. Area Number of Rooms', min_value=0)
avg_area_number_of_bedrooms = st.number_input('Avg. Area Number of Bedrooms', min_value=0)
area_population = st.number_input('Area Population', min_value=0)

# Prediction
if st.button('Predict'):
    input_data = np.array([[avg_area_income, avg_area_house_age, avg_area_number_of_rooms, avg_area_number_of_bedrooms, area_population]])
    prediction = model.predict(input_data)
    
    st.write(f'The predicted house price is ${prediction[0]:,.2f}')
