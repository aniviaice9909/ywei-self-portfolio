mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"your-email@domain.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[theme]\n\
primarycolor = "#C29AF5"\n\
backgroundColor = "#003C7F"\n\
secondaryBackgroundColor = "#040404"\n\
textColor = "#FAFAFA"\n\
[params.background]\n\
color = "#003C7F"\n\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml