import os

import streamlit as st
from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import OpenAI

API_KEY = "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"
model_id = "gpt-3.5-turbo"

os.environ["OPENAI_API_KEY"] = API_KEY
loaders = PyPDFLoader('/Users/chaitanyadua/Desktop/Health Portal/ADR11.pdf')

index = VectorstoreIndexCreator().from_loaders([loaders])
st.title(' Talk to your PDF document! ')
prompt = st.text_input("Enter your query")

if prompt:

    response = index.query(llm=OpenAI(model_name="gpt-3.5-turbo", temperature=0.2), question = prompt, chain_type = 'stuff')

    st.write("<b>" + prompt + "</b><br><i>" + response + "</i><hr>", unsafe_allow_html=True )
