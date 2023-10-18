# Premium Service Enrollment Prediction

This project is about Predictive Analytics for Premium Service Enrollment. It aims to predict whether an app user will purchase a premium offer based on their interactions with the app.

## Project Overview

In today's dynamic business landscape, understanding customer behavior and optimizing service offerings is a primary goal. Knowing the intentions of your clients as a business gives insights about your next moves, driving decision-making.

The "Premium Service Enrollment Prediction" project represents an attempt to predict whether an app user will purchase the premium offer or not based on their interactions with the app.

### Project Components

- Analyzed and preprocessed data to ensure data quality and integrity.
- Built a Machine Learning Model to predict the probability of a user purchasing the premium offer.
- Evaluated and deployed the model as a web app.

### Tools and Technology

- Python, Scikit Learn, Pandas, Numpy, Matplotlib, Seaborn
- Streamlit Web App
- Jupyter Notebook, Visual Studio Code, Git, GitHub

## Sample Data

A sample of the used dataset can be found [here](#) (Replace with your dataset link). The dataset includes 143 features and a target feature. It represents user demographics, user interactions with app features, user engagement with premium features, and user subscription to the premium service.

## Metrics and Results

The project evaluation metrics include Confusion Matrix, Precision and Recall, and ROC AUC Curves. Here are some of the results:

| Metric          | Score               |
|-----------------|---------------------|
| Precision Score | 0.9128              |
| Recall Score    | 0.8239              |
| F1 Score        | 0.8661              |


## Demo

You can try the app using the Streamlit view from [here](https://premiumenrollement.streamlit.app/).




* The full streamlit app is fully available on this link: https://premiuemenrollmentprediction.streamlit.app/

#### Dependencies:
- Python 3.10.11
- streamlit 

#### Instructions to Try the Project:

* Clone Repo:
~~~ 
git clone https://github.com/Hypatchia/premiuemenrollmentprediction
~~~

* Navigate to Repo's directory
~~~
cd PremiumEnrollementPrediction
~~~
* Create virtual environment
~~~
python -m venv myenv
~~~

* Activate venv
~~~
source <path_to_environmeent>/myenv/activate
~~~
* Install requirements.txt
~~~
pip install -r requirements.txt
~~~

* Run Streamlit Server:
~~~
streamlit run app.py
~~~

* Navigate to saved_models
- Copy and past.pkl saved model to root directory (where app.py is)
* Navigate to Processed_dataset
- Upload the test_data.csv to app.

## Contact

