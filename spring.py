import streamlit as st

from PIL import Image


#def test_st_image_PIL_array(self):
"""DR.MAHMOUD ABD ELAZIZ."""
imgs = [
            Image.new("RGB", (32, 32), color="red"),
            Image.new("RGB", (32, 32), color="blue"),
            Image.new("RGB", (64, 64), color="green"),
        ]
        # Manually calculated by letting the test fail and copying and
        # pasting the result.
imgs_b32 = [
            "medo1.png",
            "medo1.png",
            "medo1.png",
        ]
st.image(
            imgs,
            caption=["some caption"] * 3,
            width=30,
            use_column_width=True,
            clamp=True,
            
        )

