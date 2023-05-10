from pathlib import Path
import streamlit as st
from PIL import Image
import base64

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent.parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
pic = current_dir / "assets" / "Biomechanics.gif"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Biomechanics | Yew Wei's Portfolio"
PAGE_ICON = "🗒️"
DESCRIPTION = """
This is my current research project, where I mainly work on simulating a few running models to evaluate running biomechanics in terms of kinematics, kinetics, muscular activation, etc. Eventually, these analyses will be presented through graphical diagrams. Using these running models, I am also responsible for assessing the effects of wearing hard and soft cushion pads in shoes while running. The effects will also be evaluated in terms of biomechanics, by analyzing the changes in those runners' kinematics and kinetics. I have also been analyzing the differences in running patterns between Western and Asian people. Since this is an ongoing project, unfortunately, I am unable to publish any more detailed information online.
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
st.markdown("<h1 style='text-align: center; color: white;'>Biomechanics</h1>", unsafe_allow_html=True)

file = open(pic, "rb")
contents = file.read()
data_url = base64.b64encode(contents).decode("utf-8")
file.close()

st.markdown(f'<div style="text-align: center;"><img src="data:image/gif;base64,{data_url}" alt="biomechanics gif" style="max-width: 100%; width: 1000px; height: auto;"></div>', unsafe_allow_html=True)


html_content = f"""<h1 style='text-align: justify;'><div><p style='font-size: 16px; line-height: 1.5;'>{DESCRIPTION}</p></div></h1>"""


st.markdown(html_content, unsafe_allow_html=True)