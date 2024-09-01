import streamlit as st
import pickle
import pandas as pd
import numpy as np
import xgboost
from xgboost import XGBRegressor

def run_score_predictor_page():
    pipe = pickle.load(open('models/score_predictor.pkl', 'rb'))

    teams = ['Sunrisers Hyderabad',
            'Mumbai Indians',
            'Royal Challengers Bengaluru',
            'Kolkata Knight Riders',
            'Punjab Kings',
            'Chennai Super Kings',
            'Rajasthan Royals',
            'Delhi Capitals',
            'Lucknow Super Giants',
            'Gujarat Titans']

    cities = ['Chandigarh', 'Delhi', 'Mumbai', 'Kolkata', 'Jaipur',
            'Hyderabad', 'Chennai', 'Durban', 'Centurion', 'Ahmedabad',
            'Dharamsala', 'Indore', 'Visakhapatnam', 'Pune', 'Abu Dhabi',
            'Sharjah', 'Dubai', 'Rajkot', 'Bengaluru', 'Navi Mumbai',
            'Lucknow']
    wicket = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    over = [3,4,5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

    st.title('IPL Score Predictor')

    col1, col2 = st.columns(2)

    with col1:
        batting_team = st.selectbox('Select batting team', sorted(teams))
    with col2:
        bowling_team = st.selectbox('Select bowling team', sorted(teams))

    city = st.selectbox('Select city', sorted(cities))

    col3, col4, col5 = st.columns(3)

    with col3:
        current_score = st.number_input('Current Score')
    with col4:
        overs = st.selectbox('Overs', sorted(over))
    with col5:
        wickets = st.selectbox('Wicket', sorted(wicket))

    last_three_run = st.number_input('Runs scored in last 3 overs')
    last_three_wickets = st.number_input('Wickets in last 3 overs')


    if st.button('Predict Score'):
        balls_left = 120 - (overs * 6)
        wickets_left = 10 - wickets
        crr = current_score / overs

        input_df = pd.DataFrame({
            'batting_team': [batting_team],
            'bowling_team': [bowling_team],
            'city': city,
            'current_score': [current_score],
            'balls_left': [balls_left],
            'wickets_left': [wickets_left],
            'crr': [crr],
            'last_three_runs': [last_three_run],
            'last_three_wickets': [last_three_wickets]
        })
        result = pipe.predict(input_df)
        st.header("Predicted Score - " + str(int(result[0])))
