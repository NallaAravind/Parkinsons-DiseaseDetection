import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models


parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu(' Disease Prediction System',
                          
                          [
                           'Parkinsons Prediction'],
                          icons=['person'],
                          default_index=0)
    
    




   
    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    # col1, col2, col3, col4, col5 = st.columns(5)  
    
    # with col1:
    #     fo = st.text_input('MDVP:Fo(Hz)')
        
    # with col2:
    #     fhi = st.text_input('MDVP:Fhi(Hz)')
        
    # with col3:
    #     flo = st.text_input('MDVP:Flo(Hz)')
        
    # with col4:
    #     Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    # with col5:
    #     Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    # with col1:
    #     RAP = st.text_input('MDVP:RAP')
        
    # with col2:
    #     PPQ = st.text_input('MDVP:PPQ')
        
    # with col3:
    #     DDP = st.text_input('Jitter:DDP')
        
    # with col4:
    #     Shimmer = st.text_input('MDVP:Shimmer')
        
    # with col5:
    #     Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    # with col1:
    #     APQ3 = st.text_input('Shimmer:APQ3')
        
    # with col2:
    #     APQ5 = st.text_input('Shimmer:APQ5')
        
    # with col3:
    #     APQ = st.text_input('MDVP:APQ')
        
    # with col4:
    #     DDA = st.text_input('Shimmer:DDA')
        
    # with col5:
    #     NHR = st.text_input('NHR')
        
    # with col1:
    #     HNR = st.text_input('HNR')
        
    # with col2:
    #     RPDE = st.text_input('RPDE')
        
    # with col3:
    #     DFA = st.text_input('DFA')
        
    # with col4:
    #     spread1 = st.text_input('spread1')
        
    # with col5:
    #     spread2 = st.text_input('spread2')
        
    # with col1:
    #     D2 = st.text_input('D2')
        
    # with col2:
    #     PPE = st.text_input('PPE')
    def parse_input(input_string):
        try:
            # Split the string by commas and convert each element to a float
            input_list = [float(i) for i in input_string.split(',')]
            return tuple(input_list)
        except ValueError:
            st.error("Please enter a valid comma-separated list of numbers.")
            return None

# Create a text input widget to read the input as a comma-separated string
    input_string = st.text_input("Enter a list of floating-point numbers separated by commas:", "197.07600,206.89600,192.05500,0.00289,0.00001,0.00166,0.00168,0.00498,0.01098,0.09700,0.00563,0.00680,0.00802,0.01689,0.00339,26.77500,0.422229,0.741367,-7.348300,0.177551,1.743867,0.085569")

    # Parse the input string into a tuple of floats
    input_data = parse_input(input_string)

# If the input is valid, display the parsed tuple

    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([input_data])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)
