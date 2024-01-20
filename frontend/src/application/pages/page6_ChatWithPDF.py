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
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

set_env_vars()
footer.hide_footer(st)

backend = os.environ['backend']

st.markdown("# Chat with PDF")
st.write("""This is an LLM powered chatbot built using:         
    - [Streamlit](https://streamlit.io/)         
    - [LangChain](https://python.langchain.com/)         
    - [OpenAI](https://platform.openai.com/docs/models) LLM Model """
)
st.markdown("---")

api_key = st.text_input("OpenAI API Key",
                        'Paste your OpenAI Api Key',
                            type="password")
os.environ['OPENAI_API_KEY'] = api_key
# Upload a PDF File
pdf = st.file_uploader("Upload your PDF File", type='pdf', )

if pdf is not None:
    pdf_reader = PdfReader(pdf)
    text=""
    for page in pdf_reader.pages:
        text+=page.extract_text()
    #st.write(text)
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len

    )
    chunks = text_splitter.split_text(text=text)
    #st.write(chunks[0])
    store_name = pdf.name[:-4]
    embeddings = OpenAIEmbeddings()
    VectorStore = FAISS.from_texts(chunks, embeddings)
    query = st.text_input("Ask Question from your PDF File")
    if query:
        docs = VectorStore.similarity_search(query=query, k=3)
        llm = OpenAI()
        chain = load_qa_chain(llm = llm, chain_type='stuff')
        with get_openai_callback() as cb:
            response = chain.run(input_documents=docs, question=query)
            print(cb)
        st.write(response)
