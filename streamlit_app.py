import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt

# Setting page layout
st.set_page_config(
    page_title="Generate Pixelized Art",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Sidebar for API Key and User Info
st.sidebar.header("About App")
st.sidebar.markdown('This is an app to convert rasterized images (jpeg, png) to a pixelized format created by <a href="https://ai.jdavis.xyz" target="_blank">0xjdavis</a>.', unsafe_allow_html=True)
 
# Calendly
st.sidebar.markdown("""
    <hr />
    <center>
    <div style="border-radius:8px;padding:8px;background:#fff";width:100%;">
    <img src="https://avatars.githubusercontent.com/u/98430977" alt="Oxjdavis" height="100" width="100" border="0" style="border-radius:50%"/>
    <br />
    <span style="height:12px;width:12px;background-color:#77e0b5;border-radius:50%;display:inline-block;"></span> <b>I'm available for new projects!</b><br />
    <a href="https://calendly.com/0xjdavis" target="_blank"><button style="background:#126ff3;color:#fff;border: 1px #126ff3 solid;border-radius:8px;padding:8px 16px;margin:10px 0">Schedule a call</button></a><br />
    </div>
    </center>
    <br />
""", unsafe_allow_html=True)

# Copyright
st.sidebar.caption("©️ Copyright 2024 J. Davis")


st.title('Generate Pixelized Art')
st.caption('Covert your jpg/png images in to a pixelized version.')

uploaded_file = st.file_uploader("Upload an image.", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
  img = Image.open(uploaded_file)
  with st.status('Uploaded!', expanded=True):
    h, w = img.size
    c = st.slider('Number of Colors', 1, 256, 25)
    g = st.slider('Grid Size', 1, min([h,w]), 75)
    img = img.convert('P', palette=Image.ADAPTIVE, colors=c)
    img=img.resize((g, int(g / h * w)),Image.BILINEAR)
    res=img.resize((640,int(640/ h * w)), Image.NEAREST)
    st.image(res, caption="It's pixelized!", width=640)
