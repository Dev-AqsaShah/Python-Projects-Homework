import streamlit as st 

st.title("BMI calculator")

weight = st.number_input("enter your weight in kg.")
height = st.number_input("enter your height in cm")
final_height = height ** 2
if st.button("calculate BMI"):
    bmi = weight / final_height
    st.success(f'your BMI is: {bmi:.2f}')
    
    if bmi < 18.5:
        st.warning("you are underweight")
    elif 18.5 <= bmi < 24.9:
        st.info("you have a normal weight.")
    elif 25 <= bmi < 29.9:
        st.warning("you are  overweight")
    else:
        st.error("you are obeses")
        
