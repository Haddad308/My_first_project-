import streamlit as st 
import joblib 
import sklearn

st.title("Insuarnce Prediction")


def get_region (reg):
    if (reg == 'northwest'):
        return [1,0,0]
    elif (reg == 'southwest'):
        return [0,0,1]
    elif (reg == 'northeast'):
        return [0,0,0]
    else :
        return [0,1,0]



age = st.number_input("Age",0,50)
bmi = st.number_input("BMI")
children = st.number_input("Children")
region = st.selectbox("region",['northwest','southwest','northeast','southeast'])
sex = st.radio("Gender",["male","female"])
smoker = st.checkbox("Smoker")

if sex == "male":
    sex = 1 
else :
    sex= 0 

row_data = [age, bmi, children, sex, smoker]
row_data.extend(get_region(region))

model = joblib.load("model.h5")
scalar = joblib.load("scalar.h5")

predicted_value = round(model.predict(scalar.transform([row_data]))[0],2)

button = st.button("Predict")
if button :
    st.markdown(f"{predicted_value}$")
    st.balloons()