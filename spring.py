
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
imgs_b64 = [
            "A1oDWgNaA9oFUoUBf3Xr7AgAAAAASUVORK5CYII=",
            "WgNaA1oDWgPaBVCHAX/y3CvgAAAAAElFTkSuQmCC",
            "NaA1oDWgNaBdYVwBALVjUB8AAAAASUVORK5CYII=",
        ]
st.image(
            imgs,
            caption=["some caption"] * 3,
            width=200,
            use_column_width=True,
            clamp=True,
            
        )

       
