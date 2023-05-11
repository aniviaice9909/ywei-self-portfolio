from pathlib import Path
import streamlit as st
from PIL import Image
import base64

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Resume_YewWei.pdf"
portfolio_file = current_dir / "assets" / "PortfolioSummary_YewWei.pdf"
profile_pic = current_dir / "assets" / "1681049288110.jpg"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Portfolio Website | YWei"
PAGE_ICON = "🗒️"
NAME = "Yew Wei Teh"
DESTRIPTION = """
A 3rd Year biomedical engineering student in Universiti Tunku Abdul Rahman (UTAR)
"""
EMAIL = "mailto:yewwei9909@hotmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/ywei-teh/"
}
PORTFOLIO = {
    "Statement": "Statement",
    "Biomechanics": "Biomechanics",
    "Discord": "Discord",
    "Biomaterials": "Biomaterials",
    "SOLIDWORKS & 3D CAD": "SOLIDWORKS_3D_CAD",
    "Medical Imaging": "Medical_Imaging",
    "FFmpeg": "FFmpeg"
}

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

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True) # open css file for style
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read() # read resume
with open(portfolio_file, "rb") as ppdf_file:
    PPDFbyte = ppdf_file.read() # read resume
# profile_pic = Image.open(profile_pic) # open image


# --- HERO SECTION ---
col1, col2 = st.columns([1,2], gap="small")
with col1:
    file = open(profile_pic, "rb")
    contents = file.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file.close()

    st.markdown(f'<div style="text-align: center;"><img src="data:image/gif;base64,{data_url}" alt="profile picture" style="max-width: 00%; width="500px"; height="500px"></div>', unsafe_allow_html=True)

with col2:
    st.title(NAME)
    st.write(DESTRIPTION)
    st.download_button(
        label="📑 Resume",
        data=PDFbyte,
        file_name="Resume_YewWei.pdf",
        mime="application/octet-stream"
    )

    st.download_button(
        label="📓 Portfolio Summary",
        data=PPDFbyte,
        file_name="PortfolioSummary_YewWei.pdf",
        mime="application/octet-stream"
    )

    st.write(f"[E-mail]({EMAIL})")
    st.write(f"[LinkedIn]({SOCIAL_MEDIA['LinkedIn']})")

st.write('')
st.write('')
st.write('')

# --- PORTFOLIO SETTINGS ---
STATEMENT_ICON = current_dir / "images" / "1680673778592.jpg"
STATEMENT_ICON = open(STATEMENT_ICON, "rb")

BIOMECHANICS_ICON = current_dir / "images" / "Screenshot.png"
BIOMECHANICS_ICON = open(BIOMECHANICS_ICON, "rb")

MEDICAL_ICON = current_dir / "images" / "Task3.png"
MEDICAL_ICON = open(MEDICAL_ICON, "rb")

DISCORD_ICON = current_dir / "images" / "Screenshot3.png"
DISCORD_ICON = open(DISCORD_ICON, "rb")

FFmpeg_ICON = current_dir / "images" / "223052.png"
FFmpeg_ICON = open(FFmpeg_ICON, "rb")

# --- PORTFOLIO SECTION ---
col3, col4, col5 = st.columns(3, gap="small")
with col3:
    contents = STATEMENT_ICON.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    STATEMENT_ICON.close()

    st.markdown(f'''<div style="text-align: center;"><a href="{PORTFOLIO['Statement']}" target="_self"><img src="data:image/gif;base64,{data_url}" alt="ffmpeg" style="max-width: 100%; width: 400px; height: 550px;"></a></div>''', unsafe_allow_html=True)
    html_mark = f'''<a href={PORTFOLIO['Statement']} target="_self" style="display: block; text-align: center;"><p style='font-size: 25px;'>{PORTFOLIO['Statement']}</p></a>'''

    st.markdown(html_mark, unsafe_allow_html=True)
with col4:
    contents = BIOMECHANICS_ICON.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    BIOMECHANICS_ICON.close()

    st.markdown(f'''<div style="text-align: center;"><a href="{PORTFOLIO['Biomechanics']}" target="_self"><img src="data:image/gif;base64,{data_url}" alt="ffmpeg" style="max-width: 100%; width: 350px; height: 550px;"></a></div>''', unsafe_allow_html=True)
    html_mark = f'''<a href={PORTFOLIO['Biomechanics']} target="_self" style="display: block; text-align: center;"><p style='font-size: 25px;'>{PORTFOLIO['Biomechanics']}</p></a>'''

    st.markdown(html_mark, unsafe_allow_html=True)
with col5:
    contents = MEDICAL_ICON.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    MEDICAL_ICON.close()

    st.markdown(f'''<div style="text-align: center;"><a href="{PORTFOLIO['Medical Imaging']}" target="_self"><img src="data:image/gif;base64,{data_url}" alt="ffmpeg" style="max-width: 100%; width: 350px; height: 550px;"></a></div>''', unsafe_allow_html=True)
    html_mark = f'''<a href={PORTFOLIO['Medical Imaging']} target="_self" style="display: block; text-align: center;"><p style='font-size: 25px;'>Medical Imaging</p></a>'''
    st.markdown(html_mark, unsafe_allow_html=True)

st.write('')
st.write('')
st.write('')

col9, col10 = st.columns(2, gap="small")
with col9:
    contents = DISCORD_ICON.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    DISCORD_ICON.close()

    st.markdown(f'''<div style="text-align: center;"><a href="{PORTFOLIO['Discord']}" target="_self"><img src="data:image/gif;base64,{data_url}" alt="ffmpeg" style="max-width: 100%; width: 350px; height: 400px;"></a></div>''', unsafe_allow_html=True)
    html_mark = f'''<a href={PORTFOLIO['Discord']} target="_self" style="display: block; text-align: center;"><p style='font-size: 25px;'>Discord Music Bot</p></a>'''
    st.markdown(html_mark, unsafe_allow_html=True)

with col10:
    contents = FFmpeg_ICON.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    FFmpeg_ICON.close()

    st.markdown(f'''<div style="text-align: center;"><a href="{PORTFOLIO['FFmpeg']}" target="_self"><img src="data:image/gif;base64,{data_url}" alt="ffmpeg" style="max-width: 100%; width: 350px; height: 400px;"></a></div>''', unsafe_allow_html=True)
    html_mark = f'''<a href={PORTFOLIO['FFmpeg']} target="_self" style="display: block; text-align: center;"><p style='font-size: 25px;'>FFmpeg</p></a>'''
    st.markdown(html_mark, unsafe_allow_html=True)