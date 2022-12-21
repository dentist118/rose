import streamlit as st

from PIL import Image


#def test_st_image_PIL_array(self):
"""Test st.image with a PIL array."""
imgs = [
            Image.new("RGB", (32, 32), color="orange"),
            Image.new("RGB", (32, 32), color="pink"),
            Image.new("RGB", (64, 64), color="yellow"),
        ]
        # Manually calculated by letting the test fail and copying and
        # pasting the result.

st.image(
            Image.open('medo1.png'),
            
            caption=["some caption"] * 1,
            width=30,
            use_column_width=True,
            clamp=True,
           
            
        )

