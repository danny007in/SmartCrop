import streamlit as st
import pandas as pd
import numpy as np
import os
import pickle
import warnings

warnings.filterwarnings("ignore", message="Trying to unpickle estimator")

st.set_page_config(page_title="Farm", page_icon="", layout='centered', initial_sidebar_state="collapsed")

def load_model(modelfile):
	loaded_model = pickle.load(open(modelfile, 'rb'))
	return loaded_model

def main():
    # title
    html_temp = """
    <div>
    <h1 style="color:MEDIUMSEAGREEN;text-align:center;"> Farm Easy - Crop Recommendation System </h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    col = st.columns(1)[0]

    with col:
        st.subheader("Crop Recommendation on Random Values")

        if st.button('Random Prediction'):
            loaded_model = load_model('model.pkl')
            val = [
            np.random.randint(0, 150),  # Nitrogen
            np.random.randint(0, 150),  # Phosporus
            np.random.randint(0, 250),  # Potassium
            np.random.randint(5, 50),   # Temperature
            np.random.randint(10, 100),  # Humidity
            np.random.randint(0, 14),   # Ph
            np.random.randint(20, 300)  # Rainfall
            ]

            # Display title for each random value
            col.write('''### Random Values Are:''')
            col.write(f"Nitrogen: {val[0]}")
            col.write(f"Phosporus: {val[1]}")
            col.write(f"Potassium: {val[2]}")
            col.write(f"Temperature: {val[3]}")
            col.write(f"Humidity: {val[4]}")
            col.write(f"Ph: {val[5]}")
            col.write(f"Rainfall: {val[6]}")
            prediction = loaded_model.predict(np.array(val).reshape(1,-1))
            col.write('''### Results for Random Prediction''')
            col.success(f"{prediction.item().title()} are recommended by the A.I for your farm.")



        st.subheader("Crop Recommendation based on User Input")

        N = st.number_input("Nitrogen", 0, 10000)
        P = st.number_input("Phosporus", 0, 10000)
        K = st.number_input("Potassium", 0, 10000)
        temp = st.number_input("Temperature", 0, 100)
        humidity = st.number_input("Humidity in %", 0, 100)
        ph = st.number_input("Ph", 0, 14)
        rainfall = st.number_input("Rainfall in mm", 0, 1000)

        feature_list = [N, P, K, temp, humidity, ph, rainfall]
        single_pred = np.array(feature_list).reshape(1,-1)

        if st.button('Predict'):

            loaded_model = load_model('model.pkl')
            prediction = loaded_model.predict(single_pred)
            col.write('''
		    ## Results 🔍
		    ''')
            col.success(f"{prediction.item().title()} are recommended by the A.I for your farm.")
    #code for html
    hide_menu_style = """
    <style>
    .block-container {padding: 2rem 1rem 3rem;}
    #MainMenu {visibility: hidden;}
    </style>
    """

hide_menu_style = """
        <style>
        .block-container {padding: 2rem 1rem 3rem;}
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

if __name__ == '__main__':
	main()