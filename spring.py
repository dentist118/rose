
import streamlit as st

from PIL import Image



"""Test st.image with a PIL array."""
imgs = [
            Image.new("RGB", (64, 64), color="red"),
            Image.new("RGB", (64, 64), color="blue"),
            Image.new("RGB", (64, 64), color="green"),
        ]
        # Manually calculated by letting the test fail and copying and
        # pasting the result.
url = "https://streamlit.io/an_image.png"
caption = "ahoy!"

        
st.image([url] * 2, caption=[caption] * 2)

       
