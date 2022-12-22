import numpy as np
import pickle

# loading the saved model
loaded_model = pickle.load(open('C:/Users/Marlene/Documents/Europe/TCCM/M2/Electives/1 QSAR and MachineLearning/HW_2_Ceccarelli/heartapp/trained_model.sav', 'rb'))

input_data = (67,1,0,120,229,1,129,1)

# Change the input data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

# Reshape the numpy array as we are predicting for only one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('Healthy patient')
else:
  print('Patient with Heart Disease')