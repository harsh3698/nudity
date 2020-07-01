# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 13:41:11 2020

@author: harsh
"""
from nudity import Nudity
import streamlit as st
from PIL import Image
st.title("obsenity filter")
def nudity_filter(file):
    nudity = Nudity()
    if nudity.has(file) == True:
        statement = 'image is above obscenity threshold'
        return(nudity.score(file), statement)
        
URL = st.text_input('link to picture')    
#uploaded_file = st.file_uploader("Choose an image...", type="jpg")
#filename = file_selector()
#st.write('You selected `%s`' % filename)

#image = Image.open(uploaded_file)
#image = Image.open(uploaded_file)
#st.image(image, caption='Uploaded Image.', use_column_width=True)
#st.markdown('![Alt Text]' + URL)
st.write("")
st.write("Classifying...")
#a, m = nudity_filter(uploaded_file)
a, m = nudity_filter(URL)
st.write(a*100)
st.write(m)

        
