from pathlib import Path
import streamlit as st

current_dir = Path(__file__).parent.parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Discord Music Bot | Yew Wei's Portfolio"
PAGE_ICON = "🗒️"

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

link_url = "https://replit.com/join/rorwmbavex-aniviaice"
link_text = "https://replit.com/join/rorwmbavex-aniviaice"
link_1 = f'<a href="{link_url}">{link_text}</a>'

link_url_2 = "https://github.com/yt-dlp/yt-dlp"
link_text_2 = "https://github.com/yt-dlp/yt-dlp"
link_2 = f'<a href="{link_url_2}">{link_text_2}</a>'

link_url_3 = "https://youtu.be/SPTfmiYiuok"
link_text_3 = "https://youtu.be/SPTfmiYiuok"
link_3 = f'<a href="{link_url_3}">{link_text_3}</a>'

DESCRIPTION = f"""
During the last COVID-19 pandemic period, my friends and I often chatted on Discord due to the lockdown situation. We talked about everything. However, in order to make our chat room more enjoyable and interesting, I decided to help my friends create a Discord bot that can play music from YouTube and Bilibili. Special thanks to the creators of “yt-dlp” Python library {link_2} and the “freeCodeCamp.org” Youtube tutorial {link_3} for guiding me on how to make this Discord bot.
Some important code is shown as following:

"""
code = '''
async def play_song(self, ctx, song):
    info = yt_dlp.YoutubeDL({'format': 'bestaudio', 'noplaylist': 'True'}).extract_info(song, download=False)
    url = info['url']
    await ctx.send(self.song_queue[ctx.guild.id])
    ctx.voice_client.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(url, before_options="-reconnect 1 -reconnect_delay_max 3")), after=lambda error: self.bot.loop.create_task(self.check_queue(ctx)))
    ctx.voice_client.source.volume = 0.5

async def play_bilibili(self, ctx, song):
    url1 = song.split('https://www.bilibili.com/video/')
    urls = url1[1].split('/?')
    url_api_view = "https://api.bilibili.com/x/web-interface/view"
    bvid = {"bvid": urls[0]}
    print(bvid)
    api_requests = requests.get(url_api_view, bvid).json()
    cid = api_requests["data"]["cid"]
    print(cid)
    url_2 = "https://api.bilibili.com/x/player/playurl"
    sum = {"bvid": urls[0], "cid": cid}
    requests_2 = requests.get(url_2, sum).json()
    durl = requests_2["data"]["durl"][0]
    url_k = durl["url"]
    print(url_k)
    await ctx.send(self.song_queue[ctx.guild.id])
    ctx.voice_client.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(url_k, before_options="-reconnect 1 -reconnect_delay_max 3")), after=lambda error: self.bot.loop.create_task(self.check_queue(ctx)))
    ctx.voice_client.source.volume = 0.5'''
DESCRIPTION_2 = """
Please note that there are some rude words used in the error messages when replying to users, but this was a special design requested by my chit-chatting friends. Although it may seem lacking in professionalism to some extent, creating a product according to users' preferences is also a core responsibility for me as an engineer, as long as it does not conflict with any ethical issues.
"""

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True) # open css file for style
st.markdown("<h1 style='text-align: center; color: white;'>Discord Music Bot</h1>", unsafe_allow_html=True)
html_content = f"""<h1 style='text-align: justify;'><div><p style='font-size: 16px; line-height: 1.5;'>{DESCRIPTION}</p></div></h1>"""
st.markdown(html_content, unsafe_allow_html=True)
st.code(code, language='python')
html_content_3 = f"""<h1 style='text-align: justify;'><div><p style='font-size: 16px; line-height: 1.5;'>The full code is shown at here: {link_1}</p></div></h1>"""
st.markdown(html_content_3, unsafe_allow_html=True)
html_content_2 = f"""<h1 style='text-align: justify;'><div><p style='font-size: 16px; line-height: 1.5;'>{DESCRIPTION_2}</p></div></h1>"""
st.markdown(html_content_2, unsafe_allow_html=True)