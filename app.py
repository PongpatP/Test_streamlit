import streamlit as st
from PIL import Image
from function import *
import os 


# Setting page
st.set_page_config(
    page_title="[DEMO] CXR project",
    page_icon="🧊", #แก้เป็น icon touch 
    layout="centered")

# Session state (Share variable btw rerun)
if 'image' not in st.session_state:
    bg_img_path = os.path.join(os.getcwd(),'images','bg.png')
    st.session_state['image'] = Image.open(bg_img_path)
    st.session_state['upload_status'] = None
    st.session_state['temp_image_path'] = None
    st.session_state['save_path'] = None

#https://discuss.streamlit.io/t/alignment-of-content/29894/2
#https://developer.mozilla.org/en-US/docs/Web/CSS/:nth-of-type
st.markdown(
    """
    <style>
        div[data-testid="column"]:nth-of-type(1)
        {
            border:1px solid red;
        } 

        div[data-testid="column"]:nth-of-type(2)
        {
            border:1px solid blue;
            text-align: end;
        } 

        div[data-testid="column"]:nth-of-type(3)
        {
            border:1px solid green;
        } 

        
    </style>
    """,unsafe_allow_html=True
)


# Title
st.title('Chest X-ray Project (DEMO)')

# Display Image (Center)
col1, col2, col3 = st.columns([1,3,1])
with col2:
    st.image(st.session_state['image'].resize((300, 300)), use_column_width='always')

col1, col2, col3 = st.columns([1,6,1])
with col2:
    uploaded_file = st.file_uploader("Choose a x-ray file", type=['jpg','png'])
    st.write(uploaded_file)
    if uploaded_file != None: 
        if uploaded_file != st.session_state['upload_status']:
            st.session_state['upload_status'] = uploaded_file
            st.session_state['image'] = Image.open(uploaded_file)
            st.session_state['image'].thumbnail((300, 300))  
            st.session_state['save_path'] = os.path.join(os.getcwd(), 'predict_image.'+str(uploaded_file.name).split('.')[-1])
            st.session_state['image'].save(st.session_state['save_path']) 
            st.experimental_rerun()
   
        if st.button('Predict'):
            test = test_function()
            st.write(uploaded_file.name)
            st.write(st.session_state['save_path'])
            st.write(os.path.isfile(st.session_state['save_path']))
        

