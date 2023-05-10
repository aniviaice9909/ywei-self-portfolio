from pathlib import Path
import streamlit as st
from PIL import Image
import base64

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent.parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
pic = current_dir / "assets" / "210909.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Medical Imaging | Yew Wei's Portfolio"
PAGE_ICON = "🗒️"
DESCRIPTION = """
Although it is quite rare for students to publish their assignment work as part of their portfolio, I want to present this assignment because it is interesting and meaningful from my perspective. It was an assignment for my Medical Imaging course at university, where I was instructed to generate perfusion maps according to the pulse arterial spin labeling (ASL) kinetic model. After generating the perfusion maps, a comparison was performed to diagnose the patient's health.
The important Matlab code is shown as follows:
"""
code = '''
total = 0;
h = Subject_A(:, :, 1, k);
% The first two parameters are the pixels in x- and y- axes, 1 is the voxel's component for the perfusion map and k is the time frame.
g = M2(a, h, 0.8, 0.5, 1.0); 
% a is time frame, h is the subject frame at the particular of time, by default h_0 is setting to 1
% M2 is the ASL algorithm, where 0.8, 0.5, and 1.0 are the particular parameters according to the kinetic model.
total = total + g;
imagesc(total); % display the image 
colormap jet;
axis equal; % equal axes
'''

DESCRIPTION_2 ="""
This can be achieved by inserting the subject's perfusion map of each frame into the kinetic model algorithm. 
On the perfusion map, the colour warmness indicates a linear relationship with the amount of blood delivered to the tissue per unit of time and per unit of volume. This shows that the redness area shows higher blood flow as compared to others which are relatively dull or bluey.

Reference:
    Richard B. Buxton et al. (1998), 'A General Kinetic Model for Quantitative Perfusion Imaging with Arterial Spin Labeling', MRM, 40: 383-396.
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
st.markdown("<h1 style='text-align: center; color: white;'>Medical Imaging</h1>", unsafe_allow_html=True)

file = open(pic, "rb")
contents = file.read()
data_url = base64.b64encode(contents).decode("utf-8")
file.close()

st.markdown(f'<div style="text-align: center;"><img src="data:image/gif;base64,{data_url}" alt="biomechanics gif" style="max-width: 100%; width: 1000px; height: auto;"></div>', unsafe_allow_html=True)


html_content = f"""<h1 style='text-align: justify;'><div><p style='font-size: 16px; line-height: 1.5;'>{DESCRIPTION}</p></div></h1>"""
st.markdown(html_content, unsafe_allow_html=True)
st.code(code, language='matlab')
html_content_2 = f"""<h1 style='text-align: justify;'><div><p style='font-size: 16px; line-height: 1.5;'>{DESCRIPTION_2}</p></div></h1>"""
st.markdown(html_content_2, unsafe_allow_html=True)
