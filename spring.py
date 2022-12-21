
import streamlit as st

from PIL import Image



"""Test st.image with a PIL array."""
imgs = [
            Image.new("RGB", (64, 64), color="red"),
            
        ]
        # Manually calculated by letting the test fail and copying and
        # pasting the result.
url = "https://streamlit.io/cat.png"
caption = "ahoy!"

        
st.image([url] * 1, caption=[caption] * 1)
st.image(
            imgs,
            caption=["some caption"] * 3,
            width=200,
            use_column_width=True,
            clamp=True,
            
        )

       
