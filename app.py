import os

import streamlit as st
from main import ocr_predict
file=st.file_uploader("Upload the image ")
if file:
    st.image(file)
    data=file.read()
    with open('temp.png','wb') as f:
        f.write(data)

    if st.button('Start OCR'):
        with st.spinner('Loading....'):
            extractedText=ocr_predict('temp.png')
            with open('text.txt','w') as f:
                f.write(extractedText)

        st.write(extractedText)
    os.remove('temp.png')


