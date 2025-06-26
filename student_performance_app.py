import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
lda = joblib.load("lda.pkl")
feature_columns = joblib.load("feature_columns.pkl")


st.title("Nelson's Academic Perfomance Evaluator for University Students")
st.header("This app predicts a University student's performance category based on their habits and other details. Enter the required information to see if the student is likely to achieve Distinction, Good, Average, or another grade category. Powered by machine learning")
age = st.number_input("Please input your age: ")
study_hours_per_day = st.number_input("On a scale of (0-12), How long do you study daily?: ")
attendance_percentage = st.number_input("On a scale of (40-100), What was your attendance percentage last semester?: ")
sleep_hours = st.number_input("On a scale of (4-12), How many Hours of Sleep do you get daily?: ")
exercise_frequency = st.number_input("On a scale of (0-7), How frequent do you exercise?: ")
stress_level = st.number_input("If you were to pick from 1- 10 how would you say you get stressed? ")
time_management_score = st.number_input("On a scale of (1-10), How well do you manage time? ")
exam_anxiety_score = st.number_input("On a scale of (5-10), How would you rate your anxiety when you sit for exams?: ")
motivation_level = st.number_input("On a scale of (1-10), How motivated do you feel when performing academic activities?: ") 
screen_time = st.number_input("On a scale of (0-24), How many hours do you spend on screens in a day?: ")
previous_gpa = st.number_input("What was your gpa last semester?:")

gender = st.selectbox("Please Select your gender", ["Male","Female"])
st.write(f"You chose {gender}")
internet_quality = st.selectbox("What is the Quality of the Internet in your area", ["Low", "Medium", "High"])
st.write(f"You chose {internet_quality}")
access_to_tutoring = st.selectbox("Do you have access to tutoring", ["Yes", "No"])
st.write(f"You chose {access_to_tutoring}")

input_df = pd.DataFrame([{
    "age": age,
    "study_hours_per_day": study_hours_per_day,
    "attendance_percentage": attendance_percentage,
    "sleep_hours": sleep_hours,
    "exercise_frequency": exercise_frequency,
    "stress_level": stress_level,
    "time_management_score": time_management_score,
    "exam_anxiety_score": exam_anxiety_score,
    "motivation_level": motivation_level,
    "screen_time": screen_time,
    "previous_gpa": previous_gpa,
    "gender": gender,
    "internet_quality": internet_quality,
    "access_to_tutoring": access_to_tutoring
}])
input_encoded = pd.get_dummies(input_df)
input_encoded = input_encoded.reindex(columns=feature_columns, fill_value=0)

if st.button("Predict Performance"):
    X_scaled = scaler.transform(input_encoded)
    X_lda = lda.transform(X_scaled)
    prediction = model.predict(X_lda)
    st.success(f"The predicted performance category is: {prediction[0]}")

