from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="recitations", page_icon= ":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return  None
    return r.json()


lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_from = Image.open("images/asas.jpg")
img_lottie_animation = Image.open("images/asasas.jpg")

with st.container():
    st.subheader("Hello, lovers of the Holy Quran :wave:")
    st.title("A special site for listening to the Holy Quran")
    st.write("We put in your hands the most beautiful Quranic readings for the readers of this era")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What do we specialize in? ")
        st.write("##")
        st.write(
            """
            On this site we will show:
            - Quranic recitations for new readers.
            - Quranic recitations in the mihrabs.
            - Famous Quranic recitations.
            
            pray for us well
            """
        )

    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

with st.container():
    st.write("---")
    st.header("Our selection of Quranic recitations")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.write(
            """
            Surah Taha (complete) || Quiet recitation in a beautiful and humble tone || Isolate yourself from the noise of the world for a bit
            """
        )
    st.markdown("[watch video...](https://youtu.be/5LBD5jPHGrA)")

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_contact_from)
    with text_column:
        st.write(
            """
            Surah Fussilat - Complete | Reciter Islam Sobhi | Calm your heart
            """
        )
    st.markdown("[watch video...](https://youtu.be/CfUyuODfdLQ )")