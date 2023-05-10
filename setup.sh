mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"your-email@domain.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
\n\
[theme]\n\
primarycolor = "#C29AF5"\n\
backgroundColor = "#003C7F"\n\
secondaryBackgroundColor = "#040404"\n\
textColor = "#FAFAFA"\n\
\n\
[params.background]\n\
color = "#003C7F"\n\
" > ~/.streamlit/config.toml