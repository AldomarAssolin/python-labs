import streamlit as st

def styles():
    st.markdown(
         """
    <style>
    .big-title {
        font-size: 2.4rem;
        font-weight: 700;
        margin-bottom: 0.2rem;
    }
    .subtitle {
        font-size: 1.1rem;
        color: #888;
        margin-bottom: 1.5rem;
    }
    .title-highlight {
        color: #4CAF50;
        font-weight: 700;
    }
    .section-title {
        font-size: 1.3rem;
        font-weight: 600;
        margin-top: 1.5rem;
        margin-bottom: 0.3rem;
    }
    .tag {
        display: inline-block;
        padding: 0.2rem 0.6rem;
        border-radius: 999px;
        font-size: 0.8rem;
        margin-right: 0.4rem;
        background-color: #222;
        color: #fff;
    }
    .links-contatos{
        margin-right: 0.5rem;
        display: inline-block;
        margin-top: 0.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
    )