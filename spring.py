
import streamlit as st

from PIL import Image



"""Test st.image with a PIL array."""
imgs = [
            Image.new("RGB", (64, 64), color="pink"),
            
        ]
        # Manually calculated by letting the test fail and copying and
        # pasting the result.
url = "https://bgremoval.streamlit.app/~/+/media/c4e5367c557d51b94574671c91778cff53fb5aff96f31ed81ece3e63.jpg"
caption = "ahoy!"

        
st.image([url] * 1, caption=[caption] * 1)
st.image(
            imgs,
            caption=["some caption"] * 1,
            width=200,
            use_column_width=True,
            clamp=True,
            
)

       
