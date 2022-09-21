import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.title('Aplicación: predicción de salario a partir de educación y experiencia')

# Ingresar datos de educación
educ = st.slider('Educación', 0, 30)
# Ingresar datos de experiencia
exper = st.slider('Experiencia', 0, 50)

model = pickle.load(open('model.pickle'), 'rb')
pred = model.predict(np.array([[educ, exper]]))
                     
st.text(f'Su salario es de ${pred} por hora')
