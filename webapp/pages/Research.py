import streamlit as st 
import pandas as pd
import numpy as np

st.markdown("Research 👩‍🔬")
st.sidebar.markdown('# Research 👩‍🔬')

st.header("Some Research WorldWide")
st.write("G.A. Mensah, G.A. Roth, V. Fuster The global burden of cardiovascular diseases and risk factors: 2020 and beyond J Am Coll Cardiol, 74 (2019), pp. 2529-2532")

st. write("C.J.L. Murray, A.Y. Aravkin, P. Zheng, et al. Global burden of 87 risk factors in 204 countries and territories, 1990 to 2019: a systematic analysis for the Global Burden of Disease Study 2019 Lancet, 396 (2020), pp. 1223-1249")

st.write("GBD 2017 Risk Factor Collaborators Global, regional, and national comparative risk assessment of 84 behavioural, environmental and occupational, and metabolic risks or clusters of risks for 195 countries and territories, 1990 to 2017: a systematic analysis for the Global Burden of Disease Study 2017 Lancet, 392 (2018), pp. 1923-1994")

st.write("M.J. Husain, B.K. Datta, D. Kostova, et al. Access to cardiovascular disease and hypertension medicines in developing countries: an analysis of essential medicine lists, price, availability, and affordability J Am Heart Assoc, 9 (2020), Article e015302")

st.write("I. Reynolds, R.L. Page, R.S. Boxer Cardiovascular health and healthy aging P.P. Coll (Ed.), Healthy Aging: A Complete Guide to Clinical Management, Springer International Publishing, Cham, Switzerland (2019), pp. 31-51")

st.write("V. Fuster Global burden of cardiovascular disease: time to implement feasible strategies and to monitor results J Am Coll Cardiol, 64 (2014), pp. 520-522")

df = pd.DataFrame(
    np.random.randn(1000,2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(df)