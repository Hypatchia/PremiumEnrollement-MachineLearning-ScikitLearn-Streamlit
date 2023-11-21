# Import necessary libraries
import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib
import tempfile
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from base64 import b64encode
# Title
import streamlit as st
import time

import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(layout='centered')
model_path = "saved_models/enrollment_classifier.pkl"
sample_data = pd.read_csv('streamlit/sample_data.csv')



if 'clicked' not in st.session_state:
    st.session_state.clicked = False


def click_button():
    st.session_state.clicked = True




def make_predictions(data):
    
    st.write(data)
  
    # StandardScaler for scaling input data
    scaler = StandardScaler()
    preprocessed_data = pd.DataFrame(scaler.fit_transform(data),columns=data.columns)
    
    
    # Make predictions using the pre-trained model directly on the uploaded test data
    predictions = loaded_model.predict(preprocessed_data)  # Assuming your model can predict on the entire DataFrame
    
    # Add the predictions as a new column to the test data
    data['Predicted'] = predictions


    # Display the combined DataFrame with predictions
    st.subheader('Test Data with Predictions')
    st.write(data)
    return data

def display_eda(data):

    st.subheader('Exploratory Data Analysis')
    st.write('1. Data Features')
    st.write(data.columns)
    st.write('2. Data shape')
    st.write(data.shape)
 
    st.write('3. Data head')
    st.write(data.head())
    st.write('4. Summary Statistics')
    st.write(data.describe())
    st.write('5. Correlation matrix')
    st.write(data.corr())

    

    return None



# load the model from disk
loaded_model = joblib.load(model_path)
# Centered text
st.markdown("<h3 style='text-align: center;'>Customer Premium Purchase: Machine Learning</h3>", unsafe_allow_html=True)

st.markdown("<h4 style='text-align: center;'>Get inference on whether users will purchase the premium offer using a pre-trained model</h4>", unsafe_allow_html=True)

st.markdown("<h6 style='text-align: center;'>In working environemnt:</h6>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center;'>to get insights about new users and whether they will purchase the premium offer of the app in the future, the marketing individual would upload a dataset of information about the user behavior, and get the predictions on whether or not they will enroll. </p>",
             unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;'>For the purpose of this demo:</h6>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center;'>A sample dataset with user behavior features is provided by clicking the use sample dataset button , the rest flows.</p>",
             unsafe_allow_html=True)

st.markdown("<h6 style='text-align: center;'>How to use:</h6>", unsafe_allow_html=True)


st.markdown("<p style='text-align: center;'>1. Upload (or use sample) of the user behavior data in csv file<br> 2. A pretrained Random Forest Classifier model with 91% precision is loaded <br> 3. After processing in the backend, the predictions are made <br> 4. You will be able to view the file containing the data you input and predictions in the last column.<br> 5. You can then download the file for further use.</p>",
             unsafe_allow_html=True)

# Upload CSV file
uploaded_file = st.file_uploader("Upload a CSV file to get insights on enrollment", type=["csv"])
# Centered button
# Create three columns with specified widths
col1, col2, col3 = st.columns((2.2 , 3, 1))

# Calculate the padding for the center column to center its content

with col2:
  
    st.button("Using Upload Dataset",on_click=click_button)
    st.button("Using Sample Dataset",on_click=click_button)
# Create three columns with specified widths
col1, col2, col3 = st.columns((1.5 , 3, 1))

# Calculate the padding for the center column to center its content

with col2:
    if st.session_state.clicked and uploaded_file is not None:
        st.write('You selected your data')

       
        # Read the test dataset
        data = pd.read_csv(uploaded_file)
        display_eda(data)
        predictions = make_predictions(data)

        download_button = st.download_button(
            label="Download Predictions CSV",
            data=data.to_csv(index=False).encode('utf-8'),
            key="download_button",
            file_name="predictions.csv",
            mime="text/csv",
            
        )


    elif st.session_state.clicked:

        data = sample_data
        
        display_eda(data)
        predictions = make_predictions(data)
            
    # Add a download button for the DataFrame
        download_button = st.download_button(
            label="Download Predictions CSV",
            data=data.to_csv(index=False).encode('utf-8'),
            key="download_button",
            file_name="predictions.csv",
            mime="text/csv",
            
        )
