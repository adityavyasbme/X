import streamlit as st
from src.domain import footer
from src.infrastructure.backendHealthCheck import add_health_check_button
import os
import requests
from src.domain.pageConfig import set_env_vars

# LLM Specific
import pickle
from PyPDF2 import PdfReader
from langchain.llms import OpenAI
from langchain.document_loaders import YoutubeLoader
from langchain.llms import OpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter

set_env_vars()
footer.hide_footer(st)

backend = os.environ['backend']

st.markdown("# Summarize Youtube Video(s)")
st.markdown("---")

api_key = st.text_input("OpenAI API Key",
                        'Paste your OpenAI Api Key',
                            type="password")
os.environ['OPENAI_API_KEY'] = api_key

# Choose an option

ots = ('Short Video Duration',
     'Long Video Duration',
     'Multiple Videos')

option = st.selectbox(
    'Choose Option',
    ots
)

from langchain.llms import OpenAI

if option == ots[0]:
    link = st.text_input("Youtube Link", 'Paste your link here')
    try:
        loader = YoutubeLoader.from_youtube_url(link, add_video_info=True)
        submit = st.button('Submit')
        if submit:
            result = loader.load()
            st.write(f"Found Video from {result[0].metadata['author']} that is {result[0].metadata['length']} seconds long")
            llm=OpenAI(temperature=0.6)
            chain = load_summarize_chain(llm=llm, chain_type = 'stuff', verbose=True)            
            ans = chain.run(result)
            st.markdown("---")
            st.write(ans)
            st.markdown("---")
    except: 
        st.markdown("---")
        st.write("Need API Key")
        st.markdown("---")

if option == ots[1]:
    link = st.text_input("Youtube Link", 'Paste your link here')
    try:
        loader = YoutubeLoader.from_youtube_url(link, add_video_info=True)
        submit = st.button('Submit')
        if submit:
            result = loader.load()
            st.write(f"Found Video from {result[0].metadata['author']} that is {result[0].metadata['length']} seconds long")
            llm=OpenAI(temperature=0.6)            
            chain = load_summarize_chain(llm=llm, chain_type = 'map_reduce', verbose=False)            
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            texts = text_splitter.split_documents(result)
            ans = chain.run(texts)
            st.markdown("---")
            st.write(ans)
            st.markdown("---")
    except: 
        st.markdown("---")
        st.write("Need API Key")
        st.markdown("---")

if option == ots[2]:
    link = st.text_input("Youtube Links", 'Separate links by comma ', help = 'separate by comma only; no space please; e.g., Link1,Link2')
    try:
        youtube_url_list = link.split(',')
        submit = st.button('Submit')        
        if submit:
            text = []
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap = 200)
            for url in youtube_url_list:
                loader = YoutubeLoader.from_youtube_url(url, add_video_info=True)
                result=loader.load()
                text.extend(text_splitter.split_documents(result))        
                st.write(f"Found Video from {result[0].metadata['author']} that is {result[0].metadata['length']} seconds long")
            llm=OpenAI(temperature=0.6)            
            chain = load_summarize_chain(llm=llm, chain_type = 'map_reduce', verbose=False)
            ans = chain.run(text)
            st.markdown("---")
            st.write(ans)
            st.markdown("---")
    except Exception as e: 
        st.markdown("---")
        st.write(e)
        st.write("Need API Key")
        st.markdown("---")    
