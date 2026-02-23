import streamlit as st


def styles():
    st.markdown(
        """
    <style>
    .nav {
        display: flex;
        gap: 1.5rem;
        margin-bottom: 1.5rem;
        background-color: #1b1925;
        border-radius: 8px;
        padding: 0.5rem 1rem;
    }
    .nav-link {
        text-decoration: none;
        color: #4CAF50;
        font-weight: 600;
        padding: 0.3rem 0.6rem;
        border-radius: 4px;
    }
    .nav-link:hover {
        background-color: #211d32;
        color: #fff;
        transition: background-color 0.3s ease, color 0.3s ease;
    }
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
    .folder-link {
        text-decoration: none;
        color: #4CAF50;
        font-weight: 600;
    }
    .links-more {
        text-decoration: none;
        color: #f24f4f;
        cursor: pointer;
    }
    .links-contatos{
        display: flex;
        flex-direction: column;
    }
    .links-contatos a {
        text-decoration: none;
    }
    .links-contatos a img {
        margin: 0.5rem;
        border-radius: 8px;
    }
    .btn-links {
        display: inline-block;
        padding: 0.4rem 0.8rem;
        border-radius: 4px;
        font-size: 0.9rem;
        margin-top: 0.5rem;
        background-color: #4CAF50;
        color: #fff;
        text-decoration: none;
    }
    .btn-links:hover {
        background-color: #45a049;
        transition: background-color 0.3s ease;
    }
    .card-container {
        display: flex;
        gap: 30px;
        justify-content: start;
        flex-wrap: wrap;
    }
    .card {
        background-color: #1b1925;
        border-radius: 8px;
        padding: 20px;
        width: 300px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
    }
    .card a {
        text-decoration: none;
    }
    .card-title {
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 10px;    
    }
    .card-description {
        font-size: 1rem;
        color: #888;
        margin-bottom: 15px;
    }
    .card-link {
        text-decoration: none;
        color: #4CAF50;
        font-weight: 600;
    }
    .card-link:hover {
            color: #45a049;
            transition: color 0.3s ease;
    "}
    .card-image {
        width: 100%;
        border-radius: 4px;
        margin-bottom: 15px;
    }
    .card-button {
        display: inline-block;
        padding: 10px 20px;
        background-color: #4CAF50;
        color: white;
        border-radius: 4px;
        text-decoration: none;
        font-weight: 600;
    }
    .card-button:hover {
        background-color: #45a049;
        transition: background-color 0.3s ease;
    } 
    .card-link-button {
        display: inline-block;
        padding: 10px 20px;
        background-color: transparent;
        color: #4CAF50;
        border: 2px solid #4CAF50;
        border-radius: 4px;
        text-decoration: none;
        font-weight: 600;
    }
    .card-link-button:hover {
        background-color: #4CAF50;
        color: white;
        border-color: #4CAF50;
        transition: all 0.3s ease;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )
