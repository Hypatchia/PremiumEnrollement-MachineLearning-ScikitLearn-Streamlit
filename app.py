# Import necessary libraries
import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib
import tempfile
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Title
st.title('Premium Enrollement Prediction App')

# Upload CSV file
uploaded_file = st.file_uploader("Upload a CSV file to make its predictions", type=["csv"])

# Upload pre-trained logistic regression model
model_file = st.file_uploader("Upload the Pre-Trained model", type=["pkl"])


if uploaded_file is not None and model_file is not None:
    predict_button = st.button("Predict")
    
    if predict_button:
        # Read the test dataset
        data = pd.read_csv(uploaded_file)

        # Display the test dataset
        st.subheader('Test Dataset')
        st.write(data)

        # Save the uploaded model to a temporary file
        with tempfile.NamedTemporaryFile(delete=False) as temp_model_file:
            temp_model_file.write(model_file.read())

        # Load the pre-trained model using joblib
        model = joblib.load(temp_model_file.name)

        # StandardScaler for scaling input data
        scaler = StandardScaler()
        preprocessed_data = pd.DataFrame(scaler.fit_transform(data),columns=data.columns)
        
        
        # Make predictions using the pre-trained model directly on the uploaded test data
        predictions = model.predict(preprocessed_data)  # Assuming your model can predict on the entire DataFrame
        
        # Add the predictions as a new column to the test data
        data['Predicted'] = predictions


        # Display the combined DataFrame with predictions
        st.subheader('Test Data (Standardized) with Predictions')
        st.write(data)


        # Add a download button for the DataFrame
        download_button = st.button("Download Predictions CSV")
        if download_button:
            st.write("Downloaded!")
            csv = preprocessed_data.to_csv(index=False)
            st.markdown(f'<a href="data:file/csv;base64,{b64encode(csv.encode()).decode()}" download="predictions.csv">Click here to download predictions</a>', unsafe_allow_html=True)

