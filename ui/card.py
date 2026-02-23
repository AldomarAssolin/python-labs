import streamlit as st
from typing import List

def card_html(title: str, text: str, image: str, url: str) -> str:
    return f"""
    <a href="{url}" class="card-link" target="_blank" rel="noopener noreferrer">
        <div class="card">
            <img src="{image}" alt="{title}" class="card-image">
            <div class="card-title">{title}</div>
            <div class="card-description">{text}</div>
        </div>
    </a>
    """

def card_container(cards_html: List[str]):
    html = """
    <div class="card-container">
    """
    html += "\n".join(cards_html)
    html += """
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)