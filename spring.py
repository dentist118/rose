
import streamlit as st

from PIL import Image

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2019/04/24/11/27/flowers-4151900_960_720.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 



"""NEW PROJECT."""
#imgs = [
          #  Image.new("RGB", (64, 64), color="pink"),
            
     #   ]
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

       
