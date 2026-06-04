import streamlit as st

home_page = st.Page("home.py", title="Home", icon=":material/home:")
faq_page = st.Page("faq.py", title="FAQ", icon=":material/help:")
pg = st.navigation([home_page, faq_page])
st.set_page_config(initial_sidebar_state="collapsed")
pg.run()