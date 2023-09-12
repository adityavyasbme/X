import streamlit as st
from src.infrastructure import googleAnalytics as ga
from src.domain import pageConfig, footer, socialLinks

# interact with FastAPI endpoint
api_url = 'https://work.adityavyas.co.in/docs'
backend_url = "http://fastapi:8000/api/"

ga.inject_ga(st)
pageConfig.set_page_config(st)
footer.hide_footer(st)


# Introduction
st.title("Hello! I'm Aditya Vyas")
st.write(
    """
    Welcome to my corner of the web! I'm delighted to have you here.
    
    I'm an engineer with a passion for technology and a love for turning ideas 
    into reality through coding. 
    This website serves as a digital playground where I showcase my journey, 
    skills, and most importantly, my pet projects.
    """
)

st.title("What to expect here?")
st.write(
    """
    This website is more than just an online presence; it's a window into my 
    world of innovation and creativity. 

    Here, you'll find a collection of my pet projects that reflect my passion 
    for Machine Learning and Software Development. 
    These projects are more than just code; they are my way of exploring new 
    horizons and pushing the boundaries of what's possible.
    """
)

st.title("Explore My Projects")
st.write(
    """
    Feel free to dive into the Projects section on the left side of the 
    navigation bar. 
    Each project tells a unique story, from inception to completion. 
    I encourage you to explore, learn, and maybe even find inspiration 
    for your next endeavor.
    """
)


st.title("Connect with me")
st.write(
    """
    I'm not just about code; I'm about connecting with fellow enthusiasts, 
    sharing knowledge, and collaborating on exciting ventures. Don't hesitate 
    to reach out if you have any questions or just want to chat about 
    technology, innovation, or life in general.

    Once again, thank you for visiting my website. I hope you enjoy your 
    time here and find something that piques your curiosity.

    Let's embark on this digital journey together!

    Warm regards,

    Aditya Vyas
    """
)

socialLinks.create_social_links(st)
