import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt

st.title('Generate Pixelized Art')
st.subheader('Covert your jpg/png images in to a pixelized version.')

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
    st.image(res, caption="It's pixelized!", width=600)
