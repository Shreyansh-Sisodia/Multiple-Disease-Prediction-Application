# import necessary libraries
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Loading Models
dia_model=pickle.load(open("C:\\Users\\ssisodi3\\OneDrive - Cal State LA\\Desktop\\Projects\\Multiple Disease Prediction\\Diabetes.sav",'rb'))
heart_model=pickle.load(open("C:\\Users\\ssisodi3\\OneDrive - Cal State LA\\Desktop\\Projects\\Multiple Disease Prediction\\Heart.sav",'rb'))
par_model=pickle.load(open("C:\\Users\\ssisodi3\\OneDrive - Cal State LA\\Desktop\\Projects\\Multiple Disease Prediction\\Parkinsons.sav",'rb'))

# Sidebar for navigation
with st.sidebar:

    selected= option_menu('E - Doctor Multiple Disease Prediction System', 
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinson Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
# Diabetes Prediction Page
if (selected== 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML') 

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies=st.text_input('Number of pregnancies')

    with col2:
        Glucose=st.text_input('Glucose Level')

    with col3:
        BloodPressure=st.text_input('Blood Pressure Value')

    with col1:
        SkinThickness=st.text_input('Skin Thickness Value')

    with col2:
        Insulin=st.text_input('Insulin Level')

    with col3:
        BMI=st.text_input('BMI Level')

    with col1:
        DiabetesPredegreeFunction=st.text_input('Diabetes Predegree Function Value')

    with col2:
        Age=st.text_input('Age of the person')

    #code for prediction
    diab_diagnosis=''

    # creating a button for prediction

    if st.button('Diabetes Test Result'):
        diab_prediction=dia_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPredegreeFunction,Age]])

        if(diab_prediction[0]==1):
            diab_diagnosis= "The person is diabetic"
        else:
            diab_diagnosis= "The person is not diabetic"

    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected== 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML') 

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        age=st.text_input('Age')

    with col2:
        sex=st.text_input('Sex')

    with col3:
        cp=st.text_input('Chest Pain Types')

    with col1:
        trestbps=st.text_input('Resting Blood Pressure')

    with col2:
        chol=st.text_input('Serum Cholestrol in mg/dl')

    with col3:
        fbs=st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg=st.text_input('Resting Electrocardiographic Results')

    with col2:
        thalach=st.text_input('Maximum heart rate achieved')

    with col3:
        exang=st.text_input('Excercised Induced Angina')

    with col1:
        oldpeak=st.text_input('ST depression induced by exercise')

    with col2:
        slope=st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca=st.text_input('Major vessels colored by fluorosopy')

    with col1:
        thal=st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    #code for prediction
    heart_diagnosis=''

    # creating a button for prediction

    if st.button('Heart Disease Test Result'):
        heart_prediction=heart_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])

        if(heart_prediction[0]==1):
            heart_diagnosis= "The person is having heart disease"
        else:
            heart_diagnosis= "The person does not have any heart disease"

    st.success(heart_diagnosis)
    

    # Parkinson's Prediction Page
if (selected == "Parkinson Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML") 

    # getting the input data from the user
    col1, col2, col3, col4, col5= st.columns(5)

    with col1:
        fo=st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi=st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo=st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent=st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs=st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP=st.text_input('MDVP:RAP')

    with col2:
        PPQ=st.text_input('MDVP:PPQ')

    with col3:
        DDP=st.text_input('Jitter:DDP')

    with col4:
        Shimmer=st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB=st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3=st.text_input('Shimmer:APQ3')

    with col2:
        APQ5=st.text_input('Shimmer:APQ5')

    with col3:
        APQ=st.text_input('MDVP:APQ')

    with col4:
        DDA=st.text_input('Shimmer:DDA')

    with col5:
        NHR=st.text_input('NHR')

    with col1:
        HNR=st.text_input('HNR')

    with col2:
        RPDE=st.text_input('RPDE')

    with col3:
        DFA=st.text_input('DFA')
    
    with col4:
        spread1=st.text_input('spread1')

    with col5:
        spread2=st.text_input('spread2')

    with col1:
        D2=st.text_input('D2')
    
    with col2:
        PPE=st.text_input('PPE')

    #code for prediction
    parkinsons_diagnosis=''

    # creating a button for prediction

    if st.button("Parkinson's Test Result"):
        parkinsons_prediction=par_model.predict([[fo,fhi,flo,Jitter_percent,Jitter_Abs,RAP,PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])

        if(parkinsons_prediction[0]==1):
            parkinsons_diagnosis= "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis= "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)