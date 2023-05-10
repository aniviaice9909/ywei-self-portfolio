from pathlib import Path
import streamlit as st
from PIL import Image
import base64

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent.parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
pic = current_dir / "images" / "1680673778592.jpg"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Testinomial | Yew Wei's Portfolio"
PAGE_ICON = "🗒️"
DESCRIPTION = """
Welcome to my mini world! Here I would show what I've done and what I'm doing right now. I am an optimistic person, who loves to watch anime, travel, adventure and also taking challenges. I'm a biomedical engineering student, passionate and proficient in bionic, biocomputing, artificial intelligence, biomechanics, python and C++, and also make games with Unreal Engine and Unity. I am also good at video quality analysis. I strive and continue to learn and advance myself in terms of knowledge, skills and mindset, hoping that I such an inability person will have an opportunity to contribute something to the world's advancement. \n

(ps: Since my laptop was spilt by coffee before 😢, I lose a bunch of data, including the game I have created before 😭. I will try to recover them and post at here gradually.)
"""

st.set_page_config(
    page_title=PAGE_TITLE, 
    page_icon=PAGE_ICON,
    layout="wide",
    initial_sidebar_state="collapsed")

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True) # open css file for style
st.markdown("<h1 style='text-align: center; color: white;'>Testinomial</h1>", unsafe_allow_html=True)

file = open(pic, "rb")
contents = file.read()
data_url = base64.b64encode(contents).decode("utf-8")
file.close()

st.markdown(f'<div style="text-align: center;"><img src="data:image/gif;base64,{data_url}" alt="biomechanics gif" style="max-width: 100%; width: 500px; height: 650px;"></div>', unsafe_allow_html=True)
html_content = f"""<h1 style='text-align: justify;'><div><p style='font-size: 16px; line-height: 1.5;'>{DESCRIPTION}</p></div></h1>"""
st.markdown(html_content, unsafe_allow_html=True)