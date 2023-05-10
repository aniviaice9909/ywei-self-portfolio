from pathlib import Path
import streamlit as st
from PIL import Image
import base64


# --- GENERAL SETTINGS ---
PAGE_TITLE = "FFmpeg | Yew Wei's Portfolio"
PAGE_ICON = "🗒️"

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent.parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
pic = current_dir / "assets" / "Screenshot_46.png"
pic_2 = current_dir / "assets" / "043647.png"

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

DESCRIPTION = f"""
When I have spare time, I work on adding subtitles to videos using ffmpeg. As an anime lover, I enjoy collecting and keeping the anime I watch. However, most of the time, the anime I download does not come with subtitles. Therefore, some work is required to embed subtitles into the anime in the form of soft-coded subtitles. The command for embedding is shown as follows:

"""
code = ''''ffmpeg -i '1 (2).mp4' -i '1 (1).mp4' -i '1 (1).srt' -c:v copy -c copy -c:s mov_text '1.mp4'''''
DESCRIPTION_2 = """
In this case :- \n
'1 (2).mp4' is the audio source, \n
'1 (1).mp4' is the video source and \n
'1 (1).srt' is the subtitle required to be embedded. \n
Whereby the output video would be '1.mp4'. \n

Using FFmpeg is a much faster and easier way to embed a subtitle into a video, by just writing a particular code to the terminal, instead of using a video editor software.
"""

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True) # open css file for style
st.markdown("<h1 style='text-align: center; color: white;'>FFmpeg</h1>", unsafe_allow_html=True)
html_content = f"""<h1 style='text-align: justify;'><div><p style='font-size: 16px; line-height: 1.5;'>{DESCRIPTION}</p></div></h1>"""
st.markdown(html_content, unsafe_allow_html=True)
st.code(code, language='terminal')

html_content_2 = f"""<h1 style='text-align: justify;'><div><p style='font-size: 16px; line-height: 1.5;'>{DESCRIPTION_2}</p></div></h1>"""
st.markdown(html_content_2, unsafe_allow_html=True)

st.write(" ")
st.write("Before...")

file_2 = open(pic_2, "rb")
contents_2 = file_2.read()
data_url_2 = base64.b64encode(contents_2).decode("utf-8")
file_2.close()

st.markdown(f'<div style="text-align: center;"><img src="data:image/gif;base64,{data_url_2}" alt="biomechanics gif" style="max-width: 100%; width: 900px; height: auto;"></div>', unsafe_allow_html=True)

st.write(" ")
st.write("After...")

file = open(pic, "rb")
contents = file.read()
data_url = base64.b64encode(contents).decode("utf-8")
file.close()

st.markdown(f'<div style="text-align: center;"><img src="data:image/gif;base64,{data_url}" alt="biomechanics gif" style="max-width: 100%; width: 900px; height: auto;"></div>', unsafe_allow_html=True)