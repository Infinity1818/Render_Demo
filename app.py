import streamlit as st
from pages.Scr_pre import run_score_predictor_page
from pages.winner import run_winner_predictor_page

# App title
st.title("IPL Predictor App")

# Navigation buttons
if st.button("Go to Score Predictor"):
    st.session_state['page'] = "Score Predictor"
if st.button("Go to Winner Predictor"):
    st.session_state['page'] = "Winner Predictor"

# Determine which page to display
if 'page' not in st.session_state:
    st.session_state['page'] = "Score Predictor"

if st.session_state['page'] == "Score Predictor":
    run_score_predictor_page()
elif st.session_state['page'] == "Winner Predictor":
    run_winner_predictor_page()





