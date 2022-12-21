
import streamlit as st

from PIL import Image



"""Test st.image with a PIL array."""
imgs = [
            Image.new("RGB", (64, 64), color="red"),
            
        ]
        # Manually calculated by letting the test fail and copying and
        # pasting the result.
url = "https://bgremoval.streamlit.app/~/+/media/e41ef1cefe668882972d74a560811abe2134ebe7cdf41d69e50f5ae8.png"
caption = "ahoy!"

        
st.image([url] * 1, caption=[caption] * 1)
st.image(
            imgs,
            caption=["some caption"] * 1,
            width=200,
            use_column_width=True,
            clamp=True,
            
)

       
