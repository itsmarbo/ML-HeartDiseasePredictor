import numpy as np
import pickle
import streamlit as st
import pandas as pd

# loading the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))

# creating a function for Prediction

def heart_prediction(input_data):
    
    names = ['age', 'sex', 'cp', 'trestbps', 'chol', 'restecg', 'thalch', 'exang']
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data).reshape(1,len(names))

    input_data_reshaped = pd.DataFrame(input_data_as_numpy_array, columns=names)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'Healthy person'
    else:
      return 'Person with Heart Disease' 
    
def main():
    # giving a title
    st.title('Heart Predictor 🩺')
    st.subheader("Kindly provide your medical information using numbers only")
    
    # getting the input data from the user
    age = st.text_input('How old are you?')
    sex = st.text_input('Gender ( 0 = female , 1 = male) ')
    cp = st.text_input('Chest pain type ( 0 = asymptomatic, 1 = typical angina, 2 = non-anginal )')
    trestbps = st.text_input('Resting blood pressure')
    chol = st.text_input('Cholesterol measure')
    restecg = st.text_input('ECG at rest ( 0 = normal, 1 = lv hypertrophy, 2 = other )')
    thalch = st.text_input('Maximum heart rate')
    exang = st.text_input('Do you present exercise induced angina? ( 0 = No, 1 = Yes )')
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Predictor 👈'):
        diagnosis = heart_prediction([age, sex, cp, trestbps, chol, restecg, thalch, exang])
         
    st.success(diagnosis)
     
if __name__ == '__main__':
    main()